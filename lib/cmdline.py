#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Parse command line arguments and decode string
#

import argparse
import sys
from lib.encodings import system_decode
import os
import pprint


def parse_args(self):
    parser = argparse.ArgumentParser(prog='fuckme',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description='* fuckme By redrain *',
                                     usage='fuckme.py [options]')

    target = parser.add_argument_group('Target')
    target.add_argument('-u', metavar='REQUESTURL', type=str,
                        help='Set URL, e.g.\n-u="https://www.hackdog.me/login.php"')
    target.add_argument('-f', metavar='REQUESTFILE', type=str,
                        help='Load request file')
    target.add_argument('-https', default=False, action='store_true',
                        help='Load request file when the SSL enable')
    target.add_argument('-get', default=False,
                        action='store_true',
                        help='Set method GET. default: POST')    
    target.add_argument('-basic', metavar='',type=str, nargs='+',
                        help='HTTP Basic Auth, \ne.g. -basic users.dic pass.dic')

    dictionary = parser.add_argument_group('Dictionary')
    dictionary.add_argument('-d', metavar='Param=DictFile', type=str, nargs='+',
                        help='Set dict file for parameters, \n' + \
                        'support hash functions like md5, 16_md5. \n' + \
                        'e.g. -d user=users.dic pass=md5(pass.dic)')

    proxy_spoof = parser.add_argument_group('Spoof')
    proxy_spoof.add_argument('-fip', default=False, action='store_true',
                        help='random XFF')
    proxy_spoof.add_argument('-fsid', type=str,
                        help='random session')
    proxy_spoof.add_argument('-sleep', metavar='SECONDS', type=str, default='',
                        help='delay(防止server ban请求)')

    detect = parser.add_argument_group('爆破标记(编不下去英文了。。。)')
    detect.add_argument('-no302', default=False, action='store_true',
                        help='忽略302条转')
    detect.add_argument('-err', metavar='ERR', default='', type=str, nargs='+',
                        help='爆破失败标记, \ne.g. -err "密码错误"')
    detect.add_argument('-suc', metavar='SUC', default='', type=str, nargs='+',
                        help='爆破成功标记, \ne.g. -suc "登录成功"')
    detect.add_argument('-herr', metavar='HERR', default='', type=str,
                        help='http头中的失败标记')
    detect.add_argument('-hsuc', metavar='HSUC', default='', type=str,
                        help='http头中的成功标记')

    general = parser.add_argument_group('Other')
    general.add_argument('-t', metavar='THREADS', type=int, default=50,
                        help='Threads. default:50')
    general.add_argument('-o', metavar='OUTPUT', type=str, default='fucku.passwd.txt',
                        help='Output file. default: fucku.passwd.txt')
    general.add_argument('-debug', default=False, action='store_true',
                        help='Go to debug mode to check request and response')
    general.add_argument('-nov', default=False, action='store_true',
                        help='quiet mode')
    general.add_argument('-v', action='version', version='%(prog)s 0.0.3')


    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()

    if args.err:
        for i in range(len(args.err)):
            args.err[i] = system_decode(args.err[i])
    if args.suc:
        for i in range(len(args.suc)):
            args.suc[i] = system_decode(args.suc[i])

    check_args(args)
    self.args = args

    if self.args.debug:
        self.args.t = 1    # thread set to 1 in debug mode
        self.lock.acquire()
        print '*' * self.console_width
        print '[Parsed Arguments]\n'
        pprint.pprint(self.args.__dict__)
        print '\n' + '*' * self.console_width
        self.lock.release()

    self.request_thread_count = self.args.t


def check_args(args):
    if not args.f and not args.u:
        msg = 'Both RequestFILE and RequestURL were not set!\n' + \
              ' ' * 11 + 'Use -f or -u to set one'
        raise Exception(msg)

    if args.basic:
        if len(args.basic) != 2:
            msg = 'Two dict files are required. e.g. -basic users.dic pass.dic'
            raise Exception(msg)

        for df in args.basic:
            if not os.path.exists(df):
                raise Exception('Dict file not found: %s' % df)

    if not args.basic   and not args.d:
        raise Exception('Please check dict files. e.g. -d user=users.dic pass=md5(pass.dic)')

    if os.path.exists('fucku.passwd.txt'):
        os.remove('fucku.passwd.txt')

