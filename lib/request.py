#!/usr/bin/env python
# encoding=utf-8
#
# do HTTP request
#
import copy    # deepcopy
import httplib
import requests
from lib.encodings import system_encode
import base64

def thread_exit(self):
    self.lock.acquire()
    self.request_thread_count -= 1
    self.lock.release()


# def fake_ip(self, local_headers):
#     if self.args.fip:    # Random IP
#         local_headers['X-Forwarded-For'] = local_headers['Client-IP'] = \
#             '.'.join(str(random.randint(1,255)) for _ in range(4))


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

        local_headers = copy.deepcopy('Cookie')
        # fake_ip(self, local_headers)

        if self.args.basic:
            local_headers['Authorization'] = 'Basic ' + base64.b64encode(params)
        else:
            params = params.split('^^^')    # e.g. params = ['test', '{user}123456']
            i = 0
            for key in self.selected_params_keys:
                params_dict[key] = params[i]
                i += 1

        # conn_func = httplib.HTTPSConnection  if self.args.scm == 'https' else httplib.HTTPConnection
        # conn = conn_func(self.args.netloc, timeout=30)

            siteurl = self.args.u
            if not siteurl.startswith('http://'):
                siteurl = 'http://%s' % siteurl
            elif not siteurl.startswith('https://'):
                siteurl = 'https://%s' % siteurl
            
            if self.args.get:
                response = requests.get(siteurl,headers=local_headers)
            else:
                response = requests.post(siteurl,headers=local_headers)

