#!/usr/bin/python
# -*- coding: utf-8 -*-

"""LogBack prints logs in backwards"""

__author__      = 'Leandro Abelin Noskoski'
__site__        = 'www.alternativalinux.net'
__projectpage__ = 'https://github.com/logback/collor'
__copyright__   = 'Copyright 2019, Alternativa Linux'
__license__     = 'GPL'
__version__     = '1.0'
__maintainer__  = 'Leandro Abelin Noskoski'
__email__       = 'leandro@alternativalinux.net'
__status__      = 'Production'

import sys, re, argparse
from file_read_backwards import FileReadBackwards
from datetime import date, timedelta, datetime

def testdate(line=None):

    x=(line.split(' ')[:4])
    now = datetime.now() #no Year on log, using actual Year
    old_str_dttm = str(now.year)+' '+ ' '.join(x)
    fmt = '%Y %b %d %H:%M:%S'
    try:
        curr = datetime.strptime(old_str_dttm, fmt) #try convert, if not, say good bye
    except:
        return(False)

    old_dttm = now - timedelta(minutes=int(args.time)) # get now minus arg.time
    if curr >= old_dttm :   #compare if string date are on arg.time interval
        return(True)
    else:
        return(False)


def print_matches(str=None):
        x = False
        for ar in args.only:
            if re.search(ar, str,re.IGNORECASE):
                x = True
        if x :
            print(str)


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Parse log file lines of the last X minutes',usage='%(prog)s [options] /path/logfile.log')
    parser.add_argument('-o', '--only',
                help='print only match strings',
                nargs='+')
    parser.add_argument('-t', '--time',
                help='match lines in this time interval (in minutes)')
    parser.add_argument('logfile',help='Log file to read')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    with FileReadBackwards(args.logfile, encoding='utf-8') as BigFile:
     for line in BigFile:
        if not testdate(line):
            break
        else:
            if args.only :
                print_matches(line)
            else:
                print(line)
