# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import collections.abc
import asyncio
from itertools import groupby
from multidict import CIMultiDict
from ._http_response_impl_async import AsyncHttpResponseImpl, AsyncHttpResponseBackcompatMixin
from ..pipeline.transport._aiohttp import AioHttpStreamDownloadGenerator
from ..utils._pipeline_transport_rest_shared import _pad_attr_name, _aiohttp_body_helper
from ..exceptions import ResponseNotReadError

class _ItemsView(collections.abc.ItemsView):
    def __init__(self, ref):
        super().__init__(ref)
        self._ref = ref

    def __iter__(self):
        for key, groups in groupby(self._ref.__iter__(), lambda x: x[0]):
            yield tuple([key, ", ".join(group[1] for group in groups)])

    def __contains__(self, item):
        if not (isinstance(item, (list, tuple)) and len(item) == 2):
            return False
        for k, v in self.__iter__():
            if item[0].lower() == k.lower() and item[1] == v:
                return True
        return False

    def __repr__(self):
        return f"dict_items({list(self.__iter__())})"

class _KeysView(collections.abc.KeysView):
    def __init__(self, items):
        super().__init__(items)
        self._items = items

    def __iter__(self):
        for key, _ in self._items:
            yield key

    def __contains__(self, key):
        for k in self.__iter__():
            if key.lower() == k.lower():
                return True
        return False
    def __repr__(self):
        return f"dict_keys({list(self.__iter__())})"

class _ValuesView(collections.abc.ValuesView):
    def __init__(self, items):
        super().__init__(items)
        self._items = items

    def __iter__(self):
        for _, value in self._items:
            yield value

    def __contains__(self, value):
        for v in self.__iter__():
            if value == v:
                return True
        return False

    def __repr__(self):
        return f"dict_values({list(self.__iter__())})"


class _CIMultiDict(CIMultiDict):
    """Dictionary with the support for duplicate case-insensitive keys."""

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        """Return a new view of the dictionary's keys."""
        return _KeysView(self.items())

    def items(self):
        """Return a new view of the dictionary's items."""
        return _ItemsView(super().items())

    def values(self):
        """Return a new view of the dictionary's values."""
        return _ValuesView(self.items())

    def __getitem__(self, key: str) -> str:
        return ", ".join(self.getall(key, []))

    def get(self, key, default=None):
        values = self.getall(key, None)
        if values:
            values = ", ".join(values)
        return values or default

class _RestAioHttpTransportResponseBackcompatMixin(AsyncHttpResponseBackcompatMixin):
    """Backcompat mixin for aiohttp responses.

    Need to add it's own mixin because it has function load_body, which other
    transport responses don't have, and also because we need to synchronously
    decompress the body if users call .body()
    """

    def body(self) -> bytes:
        """Return the whole body as bytes in memory.

        Have to modify the default behavior here. In AioHttp, we do decompression
        when accessing the body method. The behavior here is the same as if the
        caller did an async read of the response first. But for backcompat reasons,
        we need to support this decompression within the synchronous body method.
        """
        return _aiohttp_body_helper(self)

    async def _load_body(self) -> None:
        """Load in memory the body, so it could be accessible from sync methods."""
        self._content = await self.read()  # type: ignore

    def __getattr__(self, attr):
        backcompat_attrs = ["load_body"]
        attr = _pad_attr_name(attr, backcompat_attrs)
        return super().__getattr__(attr)

class RestAioHttpTransportResponse(AsyncHttpResponseImpl, _RestAioHttpTransportResponseBackcompatMixin):
    def __init__(
        self,
        *,
        internal_response,
        decompress: bool = True,
        **kwargs
    ):
        headers = _CIMultiDict(internal_response.headers)
        super().__init__(
            internal_response=internal_response,
            status_code=internal_response.status,
            headers=headers,
            content_type=headers.get('content-type'),
            reason=internal_response.reason,
            stream_download_generator=AioHttpStreamDownloadGenerator,
            content=None,
            **kwargs
        )
        self._decompress = decompress
        self._decompressed_content = False

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        state['_internal_response'] = None  # aiohttp response are not pickable (see headers comments)
        state['headers'] = CIMultiDict(self.headers)  # MultiDictProxy is not pickable
        return state

    @property
    def content(self):
        # type: (...) -> bytes
        """Return the response's content in bytes."""
        if self._content is None:
            raise ResponseNotReadError(self)
        return _aiohttp_body_helper(self)

    async def read(self) -> bytes:
        """Read the response's bytes into memory.

        :return: The response's bytes
        :rtype: bytes
        """
        if not self._content:
            self._stream_download_check()
            self._content = await self._internal_response.read()
        await self._set_read_checks()
        return _aiohttp_body_helper(self)

    async def close(self) -> None:
        """Close the response.

        :return: None
        :rtype: None
        """
        if not self.is_closed:
            self._is_closed = True
            self._internal_response.close()
            await asyncio.sleep(0)
