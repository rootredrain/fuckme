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
from lib.consle_width import getTerminalSize
from lib.request import do_request
from lib.colorama import init, Fore, Back, Style


class Scanner():
    def __init__(self):
        init()
        self.console_width = getTerminalSize()[0] - 2
        self.lock = threading.Lock()
        self.STOP_ME = False
        parse_args(self)



    def print_s(self, s, color_red=False):
        self.lock.acquire()
        print Fore.MAGENTA + s if color_red else Fore.RESET + s
        self.lock.release()

    def now_time(self):
        return time.strftime('%H:%M:%S', time.localtime())

    def run(self):
        self.start_time = time.time()
        self.cracked_count = 0
        self.print_s('FUCK ME at %s' % self.now_time() + '\n' + '*' * s.console_width)
        
        while s.request_thread_count > 0:
            time.sleep(0.1)
        s.print_s('_' * s.console_width + '\nTask finished at %s. Cost %.2f seconds' %
                      (self.now_time(), time.time() - s.start_time) )


s = Scanner()
s.run()