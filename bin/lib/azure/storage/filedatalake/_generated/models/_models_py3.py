# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, TYPE_CHECKING

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class AclFailedEntry(_serialization.Model):
    """AclFailedEntry.

    :ivar name:
    :vartype name: str
    :ivar type:
    :vartype type: str
    :ivar error_message:
    :vartype error_message: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "error_message": {"key": "errorMessage", "type": "str"},
    }

    def __init__(
        self, *, name: Optional[str] = None, type: Optional[str] = None, error_message: Optional[str] = None, **kwargs
    ):
        """
        :keyword name:
        :paramtype name: str
        :keyword type:
        :paramtype type: str
        :keyword error_message:
        :paramtype error_message: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.type = type
        self.error_message = error_message


class BlobHierarchyListSegment(_serialization.Model):
    """BlobHierarchyListSegment.

    All required parameters must be populated in order to send to Azure.

    :ivar blob_prefixes:
    :vartype blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
    :ivar blob_items: Required.
    :vartype blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
    """

    _validation = {
        "blob_items": {"required": True},
    }

    _attribute_map = {
        "blob_prefixes": {"key": "BlobPrefixes", "type": "[BlobPrefix]"},
        "blob_items": {"key": "BlobItems", "type": "[BlobItemInternal]", "xml": {"itemsName": "Blob"}},
    }
    _xml_map = {"name": "Blobs"}

    def __init__(
        self,
        *,
        blob_items: List["_models.BlobItemInternal"],
        blob_prefixes: Optional[List["_models.BlobPrefix"]] = None,
        **kwargs
    ):
        """
        :keyword blob_prefixes:
        :paramtype blob_prefixes: list[~azure.storage.filedatalake.models.BlobPrefix]
        :keyword blob_items: Required.
        :paramtype blob_items: list[~azure.storage.filedatalake.models.BlobItemInternal]
        """
        super().__init__(**kwargs)
        self.blob_prefixes = blob_prefixes
        self.blob_items = blob_items


class BlobItemInternal(_serialization.Model):
    """An Azure Storage blob.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar deleted: Required.
    :vartype deleted: bool
    :ivar snapshot: Required.
    :vartype snapshot: str
    :ivar version_id:
    :vartype version_id: str
    :ivar is_current_version:
    :vartype is_current_version: bool
    :ivar properties: Properties of a blob. Required.
    :vartype properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
    :ivar deletion_id:
    :vartype deletion_id: str
    """

    _validation = {
        "name": {"required": True},
        "deleted": {"required": True},
        "snapshot": {"required": True},
        "properties": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "Name", "type": "str"},
        "deleted": {"key": "Deleted", "type": "bool"},
        "snapshot": {"key": "Snapshot", "type": "str"},
        "version_id": {"key": "VersionId", "type": "str"},
        "is_current_version": {"key": "IsCurrentVersion", "type": "bool"},
        "properties": {"key": "Properties", "type": "BlobPropertiesInternal"},
        "deletion_id": {"key": "DeletionId", "type": "str"},
    }
    _xml_map = {"name": "Blob"}

    def __init__(
        self,
        *,
        name: str,
        deleted: bool,
        snapshot: str,
        properties: "_models.BlobPropertiesInternal",
        version_id: Optional[str] = None,
        is_current_version: Optional[bool] = None,
        deletion_id: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword name: Required.
        :paramtype name: str
        :keyword deleted: Required.
        :paramtype deleted: bool
        :keyword snapshot: Required.
        :paramtype snapshot: str
        :keyword version_id:
        :paramtype version_id: str
        :keyword is_current_version:
        :paramtype is_current_version: bool
        :keyword properties: Properties of a blob. Required.
        :paramtype properties: ~azure.storage.filedatalake.models.BlobPropertiesInternal
        :keyword deletion_id:
        :paramtype deletion_id: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.deleted = deleted
        self.snapshot = snapshot
        self.version_id = version_id
        self.is_current_version = is_current_version
        self.properties = properties
        self.deletion_id = deletion_id


class BlobPrefix(_serialization.Model):
    """BlobPrefix.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    _validation = {
        "name": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "Name", "type": "str"},
    }

    def __init__(self, *, name: str, **kwargs):
        """
        :keyword name: Required.
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.name = name


class BlobPropertiesInternal(_serialization.Model):  # pylint: disable=too-many-instance-attributes
    """Properties of a blob.

    All required parameters must be populated in order to send to Azure.

    :ivar creation_time:
    :vartype creation_time: ~datetime.datetime
    :ivar last_modified: Required.
    :vartype last_modified: ~datetime.datetime
    :ivar etag: Required.
    :vartype etag: str
    :ivar content_length: Size in bytes.
    :vartype content_length: int
    :ivar content_type:
    :vartype content_type: str
    :ivar content_encoding:
    :vartype content_encoding: str
    :ivar content_language:
    :vartype content_language: str
    :ivar content_md5:
    :vartype content_md5: bytes
    :ivar content_disposition:
    :vartype content_disposition: str
    :ivar cache_control:
    :vartype cache_control: str
    :ivar blob_sequence_number:
    :vartype blob_sequence_number: int
    :ivar copy_id:
    :vartype copy_id: str
    :ivar copy_source:
    :vartype copy_source: str
    :ivar copy_progress:
    :vartype copy_progress: str
    :ivar copy_completion_time:
    :vartype copy_completion_time: ~datetime.datetime
    :ivar copy_status_description:
    :vartype copy_status_description: str
    :ivar server_encrypted:
    :vartype server_encrypted: bool
    :ivar incremental_copy:
    :vartype incremental_copy: bool
    :ivar destination_snapshot:
    :vartype destination_snapshot: str
    :ivar deleted_time:
    :vartype deleted_time: ~datetime.datetime
    :ivar remaining_retention_days:
    :vartype remaining_retention_days: int
    :ivar access_tier_inferred:
    :vartype access_tier_inferred: bool
    :ivar customer_provided_key_sha256:
    :vartype customer_provided_key_sha256: str
    :ivar encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :vartype encryption_scope: str
    :ivar access_tier_change_time:
    :vartype access_tier_change_time: ~datetime.datetime
    :ivar tag_count:
    :vartype tag_count: int
    :ivar expires_on:
    :vartype expires_on: ~datetime.datetime
    :ivar is_sealed:
    :vartype is_sealed: bool
    :ivar last_accessed_on:
    :vartype last_accessed_on: ~datetime.datetime
    :ivar delete_time:
    :vartype delete_time: ~datetime.datetime
    """

    _validation = {
        "last_modified": {"required": True},
        "etag": {"required": True},
    }

    _attribute_map = {
        "creation_time": {"key": "Creation-Time", "type": "rfc-1123"},
        "last_modified": {"key": "Last-Modified", "type": "rfc-1123"},
        "etag": {"key": "Etag", "type": "str"},
        "content_length": {"key": "Content-Length", "type": "int"},
        "content_type": {"key": "Content-Type", "type": "str"},
        "content_encoding": {"key": "Content-Encoding", "type": "str"},
        "content_language": {"key": "Content-Language", "type": "str"},
        "content_md5": {"key": "Content-MD5", "type": "bytearray"},
        "content_disposition": {"key": "Content-Disposition", "type": "str"},
        "cache_control": {"key": "Cache-Control", "type": "str"},
        "blob_sequence_number": {"key": "x-ms-blob-sequence-number", "type": "int"},
        "copy_id": {"key": "CopyId", "type": "str"},
        "copy_source": {"key": "CopySource", "type": "str"},
        "copy_progress": {"key": "CopyProgress", "type": "str"},
        "copy_completion_time": {"key": "CopyCompletionTime", "type": "rfc-1123"},
        "copy_status_description": {"key": "CopyStatusDescription", "type": "str"},
        "server_encrypted": {"key": "ServerEncrypted", "type": "bool"},
        "incremental_copy": {"key": "IncrementalCopy", "type": "bool"},
        "destination_snapshot": {"key": "DestinationSnapshot", "type": "str"},
        "deleted_time": {"key": "DeletedTime", "type": "rfc-1123"},
        "remaining_retention_days": {"key": "RemainingRetentionDays", "type": "int"},
        "access_tier_inferred": {"key": "AccessTierInferred", "type": "bool"},
        "customer_provided_key_sha256": {"key": "CustomerProvidedKeySha256", "type": "str"},
        "encryption_scope": {"key": "EncryptionScope", "type": "str"},
        "access_tier_change_time": {"key": "AccessTierChangeTime", "type": "rfc-1123"},
        "tag_count": {"key": "TagCount", "type": "int"},
        "expires_on": {"key": "Expiry-Time", "type": "rfc-1123"},
        "is_sealed": {"key": "Sealed", "type": "bool"},
        "last_accessed_on": {"key": "LastAccessTime", "type": "rfc-1123"},
        "delete_time": {"key": "DeleteTime", "type": "rfc-1123"},
    }
    _xml_map = {"name": "Properties"}

    def __init__(  # pylint: disable=too-many-locals
        self,
        *,
        last_modified: datetime.datetime,
        etag: str,
        creation_time: Optional[datetime.datetime] = None,
        content_length: Optional[int] = None,
        content_type: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_language: Optional[str] = None,
        content_md5: Optional[bytes] = None,
        content_disposition: Optional[str] = None,
        cache_control: Optional[str] = None,
        blob_sequence_number: Optional[int] = None,
        copy_id: Optional[str] = None,
        copy_source: Optional[str] = None,
        copy_progress: Optional[str] = None,
        copy_completion_time: Optional[datetime.datetime] = None,
        copy_status_description: Optional[str] = None,
        server_encrypted: Optional[bool] = None,
        incremental_copy: Optional[bool] = None,
        destination_snapshot: Optional[str] = None,
        deleted_time: Optional[datetime.datetime] = None,
        remaining_retention_days: Optional[int] = None,
        access_tier_inferred: Optional[bool] = None,
        customer_provided_key_sha256: Optional[str] = None,
        encryption_scope: Optional[str] = None,
        access_tier_change_time: Optional[datetime.datetime] = None,
        tag_count: Optional[int] = None,
        expires_on: Optional[datetime.datetime] = None,
        is_sealed: Optional[bool] = None,
        last_accessed_on: Optional[datetime.datetime] = None,
        delete_time: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword creation_time:
        :paramtype creation_time: ~datetime.datetime
        :keyword last_modified: Required.
        :paramtype last_modified: ~datetime.datetime
        :keyword etag: Required.
        :paramtype etag: str
        :keyword content_length: Size in bytes.
        :paramtype content_length: int
        :keyword content_type:
        :paramtype content_type: str
        :keyword content_encoding:
        :paramtype content_encoding: str
        :keyword content_language:
        :paramtype content_language: str
        :keyword content_md5:
        :paramtype content_md5: bytes
        :keyword content_disposition:
        :paramtype content_disposition: str
        :keyword cache_control:
        :paramtype cache_control: str
        :keyword blob_sequence_number:
        :paramtype blob_sequence_number: int
        :keyword copy_id:
        :paramtype copy_id: str
        :keyword copy_source:
        :paramtype copy_source: str
        :keyword copy_progress:
        :paramtype copy_progress: str
        :keyword copy_completion_time:
        :paramtype copy_completion_time: ~datetime.datetime
        :keyword copy_status_description:
        :paramtype copy_status_description: str
        :keyword server_encrypted:
        :paramtype server_encrypted: bool
        :keyword incremental_copy:
        :paramtype incremental_copy: bool
        :keyword destination_snapshot:
        :paramtype destination_snapshot: str
        :keyword deleted_time:
        :paramtype deleted_time: ~datetime.datetime
        :keyword remaining_retention_days:
        :paramtype remaining_retention_days: int
        :keyword access_tier_inferred:
        :paramtype access_tier_inferred: bool
        :keyword customer_provided_key_sha256:
        :paramtype customer_provided_key_sha256: str
        :keyword encryption_scope: The name of the encryption scope under which the blob is encrypted.
        :paramtype encryption_scope: str
        :keyword access_tier_change_time:
        :paramtype access_tier_change_time: ~datetime.datetime
        :keyword tag_count:
        :paramtype tag_count: int
        :keyword expires_on:
        :paramtype expires_on: ~datetime.datetime
        :keyword is_sealed:
        :paramtype is_sealed: bool
        :keyword last_accessed_on:
        :paramtype last_accessed_on: ~datetime.datetime
        :keyword delete_time:
        :paramtype delete_time: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.creation_time = creation_time
        self.last_modified = last_modified
        self.etag = etag
        self.content_length = content_length
        self.content_type = content_type
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_md5 = content_md5
        self.content_disposition = content_disposition
        self.cache_control = cache_control
        self.blob_sequence_number = blob_sequence_number
        self.copy_id = copy_id
        self.copy_source = copy_source
        self.copy_progress = copy_progress
        self.copy_completion_time = copy_completion_time
        self.copy_status_description = copy_status_description
        self.server_encrypted = server_encrypted
        self.incremental_copy = incremental_copy
        self.destination_snapshot = destination_snapshot
        self.deleted_time = deleted_time
        self.remaining_retention_days = remaining_retention_days
        self.access_tier_inferred = access_tier_inferred
        self.customer_provided_key_sha256 = customer_provided_key_sha256
        self.encryption_scope = encryption_scope
        self.access_tier_change_time = access_tier_change_time
        self.tag_count = tag_count
        self.expires_on = expires_on
        self.is_sealed = is_sealed
        self.last_accessed_on = last_accessed_on
        self.delete_time = delete_time


class CpkInfo(_serialization.Model):
    """Parameter group.

    :ivar encryption_key: Optional. Specifies the encryption key to use to encrypt the data
     provided in the request. If not specified, encryption is performed with the root account
     encryption key.  For more information, see Encryption at Rest for Azure Storage Services.
    :vartype encryption_key: str
    :ivar encryption_key_sha256: The SHA-256 hash of the provided encryption key. Must be provided
     if the x-ms-encryption-key header is provided.
    :vartype encryption_key_sha256: str
    :ivar encryption_algorithm: The algorithm used to produce the encryption key hash. Currently,
     the only accepted value is "AES256". Must be provided if the x-ms-encryption-key header is
     provided. Default value is "AES256".
    :vartype encryption_algorithm: str
    """

    _attribute_map = {
        "encryption_key": {"key": "encryptionKey", "type": "str"},
        "encryption_key_sha256": {"key": "encryptionKeySha256", "type": "str"},
        "encryption_algorithm": {"key": "encryptionAlgorithm", "type": "str"},
    }

    def __init__(
        self,
        *,
        encryption_key: Optional[str] = None,
        encryption_key_sha256: Optional[str] = None,
        encryption_algorithm: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword encryption_key: Optional. Specifies the encryption key to use to encrypt the data
         provided in the request. If not specified, encryption is performed with the root account
         encryption key.  For more information, see Encryption at Rest for Azure Storage Services.
        :paramtype encryption_key: str
        :keyword encryption_key_sha256: The SHA-256 hash of the provided encryption key. Must be
         provided if the x-ms-encryption-key header is provided.
        :paramtype encryption_key_sha256: str
        :keyword encryption_algorithm: The algorithm used to produce the encryption key hash.
         Currently, the only accepted value is "AES256". Must be provided if the x-ms-encryption-key
         header is provided. Default value is "AES256".
        :paramtype encryption_algorithm: str
        """
        super().__init__(**kwargs)
        self.encryption_key = encryption_key
        self.encryption_key_sha256 = encryption_key_sha256
        self.encryption_algorithm = encryption_algorithm


class FileSystem(_serialization.Model):
    """FileSystem.

    :ivar name:
    :vartype name: str
    :ivar last_modified:
    :vartype last_modified: str
    :ivar e_tag:
    :vartype e_tag: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "last_modified": {"key": "lastModified", "type": "str"},
        "e_tag": {"key": "eTag", "type": "str"},
    }

    def __init__(
        self, *, name: Optional[str] = None, last_modified: Optional[str] = None, e_tag: Optional[str] = None, **kwargs
    ):
        """
        :keyword name:
        :paramtype name: str
        :keyword last_modified:
        :paramtype last_modified: str
        :keyword e_tag:
        :paramtype e_tag: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.last_modified = last_modified
        self.e_tag = e_tag


class FileSystemList(_serialization.Model):
    """FileSystemList.

    :ivar filesystems:
    :vartype filesystems: list[~azure.storage.filedatalake.models.FileSystem]
    """

    _attribute_map = {
        "filesystems": {"key": "filesystems", "type": "[FileSystem]"},
    }

    def __init__(self, *, filesystems: Optional[List["_models.FileSystem"]] = None, **kwargs):
        """
        :keyword filesystems:
        :paramtype filesystems: list[~azure.storage.filedatalake.models.FileSystem]
        """
        super().__init__(**kwargs)
        self.filesystems = filesystems


class LeaseAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar lease_id: If specified, the operation only succeeds if the resource's lease is active and
     matches this ID.
    :vartype lease_id: str
    """

    _attribute_map = {
        "lease_id": {"key": "leaseId", "type": "str"},
    }

    def __init__(self, *, lease_id: Optional[str] = None, **kwargs):
        """
        :keyword lease_id: If specified, the operation only succeeds if the resource's lease is active
         and matches this ID.
        :paramtype lease_id: str
        """
        super().__init__(**kwargs)
        self.lease_id = lease_id


class ListBlobsHierarchySegmentResponse(_serialization.Model):
    """An enumeration of blobs.

    All required parameters must be populated in order to send to Azure.

    :ivar service_endpoint: Required.
    :vartype service_endpoint: str
    :ivar container_name: Required.
    :vartype container_name: str
    :ivar prefix:
    :vartype prefix: str
    :ivar marker:
    :vartype marker: str
    :ivar max_results:
    :vartype max_results: int
    :ivar delimiter:
    :vartype delimiter: str
    :ivar segment: Required.
    :vartype segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
    :ivar next_marker:
    :vartype next_marker: str
    """

    _validation = {
        "service_endpoint": {"required": True},
        "container_name": {"required": True},
        "segment": {"required": True},
    }

    _attribute_map = {
        "service_endpoint": {"key": "ServiceEndpoint", "type": "str", "xml": {"attr": True}},
        "container_name": {"key": "ContainerName", "type": "str", "xml": {"attr": True}},
        "prefix": {"key": "Prefix", "type": "str"},
        "marker": {"key": "Marker", "type": "str"},
        "max_results": {"key": "MaxResults", "type": "int"},
        "delimiter": {"key": "Delimiter", "type": "str"},
        "segment": {"key": "Segment", "type": "BlobHierarchyListSegment"},
        "next_marker": {"key": "NextMarker", "type": "str"},
    }
    _xml_map = {"name": "EnumerationResults"}

    def __init__(
        self,
        *,
        service_endpoint: str,
        container_name: str,
        segment: "_models.BlobHierarchyListSegment",
        prefix: Optional[str] = None,
        marker: Optional[str] = None,
        max_results: Optional[int] = None,
        delimiter: Optional[str] = None,
        next_marker: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword service_endpoint: Required.
        :paramtype service_endpoint: str
        :keyword container_name: Required.
        :paramtype container_name: str
        :keyword prefix:
        :paramtype prefix: str
        :keyword marker:
        :paramtype marker: str
        :keyword max_results:
        :paramtype max_results: int
        :keyword delimiter:
        :paramtype delimiter: str
        :keyword segment: Required.
        :paramtype segment: ~azure.storage.filedatalake.models.BlobHierarchyListSegment
        :keyword next_marker:
        :paramtype next_marker: str
        """
        super().__init__(**kwargs)
        self.service_endpoint = service_endpoint
        self.container_name = container_name
        self.prefix = prefix
        self.marker = marker
        self.max_results = max_results
        self.delimiter = delimiter
        self.segment = segment
        self.next_marker = next_marker


class ModifiedAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar if_modified_since: Specify this header value to operate only on a blob if it has been
     modified since the specified date/time.
    :vartype if_modified_since: ~datetime.datetime
    :ivar if_unmodified_since: Specify this header value to operate only on a blob if it has not
     been modified since the specified date/time.
    :vartype if_unmodified_since: ~datetime.datetime
    :ivar if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype if_match: str
    :ivar if_none_match: Specify an ETag value to operate only on blobs without a matching value.
    :vartype if_none_match: str
    """

    _attribute_map = {
        "if_modified_since": {"key": "ifModifiedSince", "type": "rfc-1123"},
        "if_unmodified_since": {"key": "ifUnmodifiedSince", "type": "rfc-1123"},
        "if_match": {"key": "ifMatch", "type": "str"},
        "if_none_match": {"key": "ifNoneMatch", "type": "str"},
    }

    def __init__(
        self,
        *,
        if_modified_since: Optional[datetime.datetime] = None,
        if_unmodified_since: Optional[datetime.datetime] = None,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword if_modified_since: Specify this header value to operate only on a blob if it has been
         modified since the specified date/time.
        :paramtype if_modified_since: ~datetime.datetime
        :keyword if_unmodified_since: Specify this header value to operate only on a blob if it has not
         been modified since the specified date/time.
        :paramtype if_unmodified_since: ~datetime.datetime
        :keyword if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype if_match: str
        :keyword if_none_match: Specify an ETag value to operate only on blobs without a matching
         value.
        :paramtype if_none_match: str
        """
        super().__init__(**kwargs)
        self.if_modified_since = if_modified_since
        self.if_unmodified_since = if_unmodified_since
        self.if_match = if_match
        self.if_none_match = if_none_match


class Path(_serialization.Model):  # pylint: disable=too-many-instance-attributes
    """Path.

    :ivar name:
    :vartype name: str
    :ivar is_directory:
    :vartype is_directory: bool
    :ivar last_modified:
    :vartype last_modified: str
    :ivar e_tag:
    :vartype e_tag: str
    :ivar content_length:
    :vartype content_length: int
    :ivar owner:
    :vartype owner: str
    :ivar group:
    :vartype group: str
    :ivar permissions:
    :vartype permissions: str
    :ivar encryption_scope: The name of the encryption scope under which the blob is encrypted.
    :vartype encryption_scope: str
    :ivar creation_time:
    :vartype creation_time: str
    :ivar expiry_time:
    :vartype expiry_time: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "is_directory": {"key": "isDirectory", "type": "bool"},
        "last_modified": {"key": "lastModified", "type": "str"},
        "e_tag": {"key": "eTag", "type": "str"},
        "content_length": {"key": "contentLength", "type": "int"},
        "owner": {"key": "owner", "type": "str"},
        "group": {"key": "group", "type": "str"},
        "permissions": {"key": "permissions", "type": "str"},
        "encryption_scope": {"key": "EncryptionScope", "type": "str"},
        "creation_time": {"key": "creationTime", "type": "str"},
        "expiry_time": {"key": "expiryTime", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        is_directory: bool = False,
        last_modified: Optional[str] = None,
        e_tag: Optional[str] = None,
        content_length: Optional[int] = None,
        owner: Optional[str] = None,
        group: Optional[str] = None,
        permissions: Optional[str] = None,
        encryption_scope: Optional[str] = None,
        creation_time: Optional[str] = None,
        expiry_time: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword name:
        :paramtype name: str
        :keyword is_directory:
        :paramtype is_directory: bool
        :keyword last_modified:
        :paramtype last_modified: str
        :keyword e_tag:
        :paramtype e_tag: str
        :keyword content_length:
        :paramtype content_length: int
        :keyword owner:
        :paramtype owner: str
        :keyword group:
        :paramtype group: str
        :keyword permissions:
        :paramtype permissions: str
        :keyword encryption_scope: The name of the encryption scope under which the blob is encrypted.
        :paramtype encryption_scope: str
        :keyword creation_time:
        :paramtype creation_time: str
        :keyword expiry_time:
        :paramtype expiry_time: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.is_directory = is_directory
        self.last_modified = last_modified
        self.e_tag = e_tag
        self.content_length = content_length
        self.owner = owner
        self.group = group
        self.permissions = permissions
        self.encryption_scope = encryption_scope
        self.creation_time = creation_time
        self.expiry_time = expiry_time


class PathHTTPHeaders(_serialization.Model):
    """Parameter group.

    :ivar cache_control: Optional. Sets the blob's cache control. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype cache_control: str
    :ivar content_encoding: Optional. Sets the blob's content encoding. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype content_encoding: str
    :ivar content_language: Optional. Set the blob's content language. If specified, this property
     is stored with the blob and returned with a read request.
    :vartype content_language: str
    :ivar content_disposition: Optional. Sets the blob's Content-Disposition header.
    :vartype content_disposition: str
    :ivar content_type: Optional. Sets the blob's content type. If specified, this property is
     stored with the blob and returned with a read request.
    :vartype content_type: str
    :ivar content_md5: Specify the transactional md5 for the body, to be validated by the service.
    :vartype content_md5: bytes
    :ivar transactional_content_hash: Specify the transactional md5 for the body, to be validated
     by the service.
    :vartype transactional_content_hash: bytes
    """

    _attribute_map = {
        "cache_control": {"key": "cacheControl", "type": "str"},
        "content_encoding": {"key": "contentEncoding", "type": "str"},
        "content_language": {"key": "contentLanguage", "type": "str"},
        "content_disposition": {"key": "contentDisposition", "type": "str"},
        "content_type": {"key": "contentType", "type": "str"},
        "content_md5": {"key": "contentMD5", "type": "bytearray"},
        "transactional_content_hash": {"key": "transactionalContentHash", "type": "bytearray"},
    }

    def __init__(
        self,
        *,
        cache_control: Optional[str] = None,
        content_encoding: Optional[str] = None,
        content_language: Optional[str] = None,
        content_disposition: Optional[str] = None,
        content_type: Optional[str] = None,
        content_md5: Optional[bytes] = None,
        transactional_content_hash: Optional[bytes] = None,
        **kwargs
    ):
        """
        :keyword cache_control: Optional. Sets the blob's cache control. If specified, this property is
         stored with the blob and returned with a read request.
        :paramtype cache_control: str
        :keyword content_encoding: Optional. Sets the blob's content encoding. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype content_encoding: str
        :keyword content_language: Optional. Set the blob's content language. If specified, this
         property is stored with the blob and returned with a read request.
        :paramtype content_language: str
        :keyword content_disposition: Optional. Sets the blob's Content-Disposition header.
        :paramtype content_disposition: str
        :keyword content_type: Optional. Sets the blob's content type. If specified, this property is
         stored with the blob and returned with a read request.
        :paramtype content_type: str
        :keyword content_md5: Specify the transactional md5 for the body, to be validated by the
         service.
        :paramtype content_md5: bytes
        :keyword transactional_content_hash: Specify the transactional md5 for the body, to be
         validated by the service.
        :paramtype transactional_content_hash: bytes
        """
        super().__init__(**kwargs)
        self.cache_control = cache_control
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_disposition = content_disposition
        self.content_type = content_type
        self.content_md5 = content_md5
        self.transactional_content_hash = transactional_content_hash


class PathList(_serialization.Model):
    """PathList.

    :ivar paths:
    :vartype paths: list[~azure.storage.filedatalake.models.Path]
    """

    _attribute_map = {
        "paths": {"key": "paths", "type": "[Path]"},
    }

    def __init__(self, *, paths: Optional[List["_models.Path"]] = None, **kwargs):
        """
        :keyword paths:
        :paramtype paths: list[~azure.storage.filedatalake.models.Path]
        """
        super().__init__(**kwargs)
        self.paths = paths


class SetAccessControlRecursiveResponse(_serialization.Model):
    """SetAccessControlRecursiveResponse.

    :ivar directories_successful:
    :vartype directories_successful: int
    :ivar files_successful:
    :vartype files_successful: int
    :ivar failure_count:
    :vartype failure_count: int
    :ivar failed_entries:
    :vartype failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
    """

    _attribute_map = {
        "directories_successful": {"key": "directoriesSuccessful", "type": "int"},
        "files_successful": {"key": "filesSuccessful", "type": "int"},
        "failure_count": {"key": "failureCount", "type": "int"},
        "failed_entries": {"key": "failedEntries", "type": "[AclFailedEntry]"},
    }

    def __init__(
        self,
        *,
        directories_successful: Optional[int] = None,
        files_successful: Optional[int] = None,
        failure_count: Optional[int] = None,
        failed_entries: Optional[List["_models.AclFailedEntry"]] = None,
        **kwargs
    ):
        """
        :keyword directories_successful:
        :paramtype directories_successful: int
        :keyword files_successful:
        :paramtype files_successful: int
        :keyword failure_count:
        :paramtype failure_count: int
        :keyword failed_entries:
        :paramtype failed_entries: list[~azure.storage.filedatalake.models.AclFailedEntry]
        """
        super().__init__(**kwargs)
        self.directories_successful = directories_successful
        self.files_successful = files_successful
        self.failure_count = failure_count
        self.failed_entries = failed_entries


class SourceModifiedAccessConditions(_serialization.Model):
    """Parameter group.

    :ivar source_if_match: Specify an ETag value to operate only on blobs with a matching value.
    :vartype source_if_match: str
    :ivar source_if_none_match: Specify an ETag value to operate only on blobs without a matching
     value.
    :vartype source_if_none_match: str
    :ivar source_if_modified_since: Specify this header value to operate only on a blob if it has
     been modified since the specified date/time.
    :vartype source_if_modified_since: ~datetime.datetime
    :ivar source_if_unmodified_since: Specify this header value to operate only on a blob if it has
     not been modified since the specified date/time.
    :vartype source_if_unmodified_since: ~datetime.datetime
    """

    _attribute_map = {
        "source_if_match": {"key": "sourceIfMatch", "type": "str"},
        "source_if_none_match": {"key": "sourceIfNoneMatch", "type": "str"},
        "source_if_modified_since": {"key": "sourceIfModifiedSince", "type": "rfc-1123"},
        "source_if_unmodified_since": {"key": "sourceIfUnmodifiedSince", "type": "rfc-1123"},
    }

    def __init__(
        self,
        *,
        source_if_match: Optional[str] = None,
        source_if_none_match: Optional[str] = None,
        source_if_modified_since: Optional[datetime.datetime] = None,
        source_if_unmodified_since: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword source_if_match: Specify an ETag value to operate only on blobs with a matching value.
        :paramtype source_if_match: str
        :keyword source_if_none_match: Specify an ETag value to operate only on blobs without a
         matching value.
        :paramtype source_if_none_match: str
        :keyword source_if_modified_since: Specify this header value to operate only on a blob if it
         has been modified since the specified date/time.
        :paramtype source_if_modified_since: ~datetime.datetime
        :keyword source_if_unmodified_since: Specify this header value to operate only on a blob if it
         has not been modified since the specified date/time.
        :paramtype source_if_unmodified_since: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.source_if_match = source_if_match
        self.source_if_none_match = source_if_none_match
        self.source_if_modified_since = source_if_modified_since
        self.source_if_unmodified_since = source_if_unmodified_since


class StorageError(_serialization.Model):
    """StorageError.

    :ivar error: The service error response object.
    :vartype error: ~azure.storage.filedatalake.models.StorageErrorError
    """

    _attribute_map = {
        "error": {"key": "error", "type": "StorageErrorError"},
    }

    def __init__(self, *, error: Optional["_models.StorageErrorError"] = None, **kwargs):
        """
        :keyword error: The service error response object.
        :paramtype error: ~azure.storage.filedatalake.models.StorageErrorError
        """
        super().__init__(**kwargs)
        self.error = error


class StorageErrorError(_serialization.Model):
    """The service error response object.

    :ivar code: The service error code.
    :vartype code: str
    :ivar message: The service error message.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "Code", "type": "str"},
        "message": {"key": "Message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword code: The service error code.
        :paramtype code: str
        :keyword message: The service error message.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message