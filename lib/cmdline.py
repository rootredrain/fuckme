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


    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()

    if args.err:
        for i in range(len(args.err)):
            args.err[i] = system_decode(args.err[i])
    if args.suc:
        for i in range(len(args.suc)):
            args.suc[i] = system_decode(args.suc[i])
    if args.rtxt:
        args.rtxt = system_decode(args.rtxt)
    if args.rntxt:
        args.rntxt = system_decode(args.rntxt)

    check_args(args)
    self.args = args

def check_args(args):
    if args.basic:
        if len(args.basic) != 2:
            msg = 'Two dict files are required. e.g. -basic users.dic pass.dic'
            raise Exception(msg)

        for df in args.basic:
            if not os.path.exists(df):
                raise Exception('Dict file not found: %s' % df)

