#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
fuckme
A simple HTTP(s) weak pass scanner
By redrain
'''


import threading
import time
from lib.cmdline import parse_args
from lib.request import do_request
from lib.colorama import init, Fore, Back, Style

class Scanner():
    def __init__(self):
        self.lock = threading.Lock()
        self.STOP_ME = False

    def print_s(self, s, color_red=False):
        self.lock.acquire()
        print Fore.MAGENTA + s if color_red else Fore.RESET + s
        self.lock.release()

    def now_time(self):
        return time.strftime('%H:%M:%S', time.localtime())

    def run(self):
        self.start_time = time.time()
        self.cracked_count = 0

s = Scanner()
s.run()