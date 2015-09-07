#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#

import time
import Queue
import os
import re


def gen_queue_basic_auth(self):
    f_user = open(self.args.basic[0], 'r')
    f_pass = open(self.args.basic[1], 'r')

    for str_user in f_user.xreadlines():
        f_pass.seek(0)    # Very important
        for str_pass in f_pass.xreadlines():
            auth_key = '%s:%s' % (str_user.strip(), str_pass.strip())
            while self.queue.qsize() >= self.args.t * 2 and not self.STOP_ME:
                time.sleep(0.001)
            self.queue.put(auth_key)

    f_user.close()
    f_pass.close()

    for i in range(self.args.t):
        self.queue.put(None)
