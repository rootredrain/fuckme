#!/usr/bin/env python
# encoding=utf-8
#
# do HTTP request
#
import copy    # deepcopy
import requests
from requests.auth import HTTPBasicAuth

def fake_ip(self, local_headers):
    if self.args.fip:    # Random IP
        local_headers['X-Forwarded-For'] = local_headers['Client-IP'] = \
            '.'.join(str(random.randint(1,255)) for _ in range(4))


def do_request(self):
    while not self.STOP_ME:
        try:
            origin_params = params = self.queue.get(timeout=1.0)
        except:
            thread_exit(self)
            return

        if params is None:
            self.queue.task_done()
            thread_exit(self)
            return

        local_headers = copy.deepcopy(self.http_headers)
        fake_ip(self, local_headers)

        # data = self.args.query
        