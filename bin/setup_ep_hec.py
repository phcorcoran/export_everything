#!/usr/bin/env python

# Copyright 2023 Deductiv Inc.
# REST endpoint for configuration
# Author: J.R. Murray <jr.murray@deductiv.net>
# Version: 2.3.0 (2023-08-11)

from deductiv_helpers import get_conf_stanza
import splunk.admin as admin
from setup_ep import SetupApp
import sys

log_level = get_conf_stanza('ep_general', 'settings')["log_level"]
options = ['stanza', 'default', 'alias', 'host', 'token', 'port', 'ssl', 'ssl_verify']
cloud_options = {
	'ssl': "1",
	'ssl_verify': "1"
}

handler = SetupApp(admin.ARG_SETUP, admin.CONTEXT_APP_AND_USER, log_level, 'ep_hec', options, cloud_options=cloud_options)
info = admin.ConfigInfo()
if sys.argv[1] == 'setup':
	handler.setup()
elif sys.argv[1] == 'execute':
    handler.execute(info)
admin.stdout_write(handler.toXml(info))
