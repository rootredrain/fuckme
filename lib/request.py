#!/usr/bin/env python
# encoding=utf-8
#
# do HTTP request
#

import requests
from requests.auth import HTTPBasicAuth


def do_request(self):
    while not self.STOP_ME:
        try:
            origin_params = params = self.queue.get(timeout=1.0)
        except:
            thread_exit(self)
            return

