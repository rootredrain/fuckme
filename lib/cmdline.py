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
                                     description='fuckme By redrain',
                                     usage='fuckme.py [options]')

    target = parser.add_argument_group('Target')
    target.add_argument('-u', metavar='REQUESTURL', type=str,
                        help='Explicitly set request URL, e.g.\n-u="https://www.test.com/login.php"')
    target.add_argument('-basic', metavar='',type=str, nargs='+',
                        help='HTTP Basic Auth brute, \ne.g. -basic users.dic pass.dic')

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()


    check_args(args)
    self.args = args

    self.args.t = 1

    self.request_thread_count = self.args.t


def check_args(args):
    if not args.u:
        msg = 'Both RequestFILE and RequestURL were not set!\n' + \
              ' ' * 11 + 'Use -u to set one'
        raise Exception(msg)

    if args.basic:
        if len(args.basic) != 2:
            msg = 'Two dict files are required. e.g. -basic users.dic pass.dic'
            raise Exception(msg)

        for df in args.basic:
            if not os.path.exists(df):
                raise Exception('Dict file not found: %s' % df)

            for df in args.basic:
                if not os.path.exists(df):
                    raise Exception('Dict file not found: %s' % df)

