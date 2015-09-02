#!/usr/bin/env python
# encoding=utf-8
#
# do HTTP request
#
import copy    # deepcopy
import httplib
import requests
from lib.encodings import system_encode


def fake_ip(self, local_headers):
    if self.args.fip:    # Random IP
        local_headers['X-Forwarded-For'] = local_headers['Client-IP'] = \
            '.'.join(str(random.randint(1,255)) for _ in range(4))

def get_proxy(self):
    self.lock.acquire()
    cur_proxy = self.proxy_list[self.proxy_index]
    self.proxy_index += 1
    if self.proxy_index > len(self.proxy_list) - 1: self.proxy_index = 0
    self.lock.release()
    return cur_proxy

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

        
        if self.args.basic:
            local_headers['Authorization'] = 'Basic ' + base64.b64encode(params)
        elif self.args.checkproxy:
            pass

        # conn_func = httplib.HTTPSConnection  if self.args.scm == 'https' else httplib.HTTPConnection
        # conn = conn_func(self.args.netloc, timeout=30)
        siteurl = sys.argv[1]
        if not siteurl.startswith('http://'):
            siteurl = 'http://%s' % siteurl
        elif not siteurl.startswith('https://'):
            siteurl = 'https://%s' % siteurl
        
        if self.args.get:
            response = requests.get(siteurl,headers=local_headers)
        else:
            response = requests.post(siteurl,headers=local_headers)

