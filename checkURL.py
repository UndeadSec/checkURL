#!/usr/bin/python3

'''
BY: UNDEADSEC from BRAZIL :)

Visit:      https://www.youtube.com/c/UndeadSec
Github:     https://github.com/UndeadSec/checkURL
Telegram:   https://t.me/UndeadSec      
'''

from __future__ import print_function
from platform import python_version
from sys import exit, argv

version = python_version().startswith('2', 0, len(python_version()))
if version:
    print('Are you using python version {}\n'
          'Please, use version 3.X of python'.format(python_version()))
    exit(1)

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror

white, red, yellow, green, END = '\33[;97m', '\33[1;91m', '\33[1;93m', '\33[1;32m', '\33[0m'

def banner():
    '''
    Show banner of tool checkURL
    :return: banner
    '''

    msg = '''    
{3}       _               _     {1}{2} _    _ _____  _      
{3}      | |             | |    {1}{2}| |  | |  __ \| |           
{3}   ___| |__   ___  ___| | __ {1}{2}| |  | | |__) | |           
{3}  / __| '_ \ / _ \/ __| |/ / {1}{2}| |  | |  _  /| |           
{3} | (__| | | |  __| (__|   <  {1}{2}| |__| | | \ \| |____       
{3}  \___|_| |_|\___|\___|_|\_\ {1}{2} \____/|_|  \_|______|{1}
            
            {3}.. .UndeadSec from BRazil. ..{1}         
\n\n{3}Checking IDN Homograph Attack ... . {1}
    '''
    return msg.format(green,END,red,white)

def parse_args():

    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description='Check IDN Homograph Attack - UndeadSec',
        epilog=dedent('''\
            Examples:
                python3 {0} --url google.com
                python3 {0} --url google.com --check-url
                python3 {0} --url-list urls.txt
                python3 {0} --url-list urls.txt --check-url
                
            Telegram: https://t.me/UndeadSec'''.format(argv[0])))

    g = parser.add_mutually_exclusive_group()

    g.add_argument(
        '--url',
        dest='url',
        help='Enter to check if it is Evil URL',
        action='store',
        metavar='URL')

    g.add_argument(
        '--url-list',
        dest='url_list',
        help='Specify a file with a list of Evil URL',
        action='store',
        metavar='URL_list')

    parser.add_argument(
        '--check-url',
        dest='check_url',
        help='Check socket URL',
        action='store_true')

    args = parser.parse_args()

    return args, parser

def check_EVIL(url):

    '''
    Check evil chars in URL
    :param url: suspicious URL
    :return: result of check and the evil chars
    '''

    bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
    result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]

    if result:
        msg = '\n{0}[*] Evil URL detected: {1}{2}{3}{1}'.format(yellow,END,red,url)
        msg += '\n{0}[*] Evil characters used: {1}{2}{3}{1}'.format(yellow,END,red,result)
    else:
        msg = '\n{0}[*] Evil URL NOT detected:{1} {2}{3}{1}'.format(yellow, END, green, url)

    return msg

def urls_list(file):
    '''
    Read the file to verify Evil URL
    :param file: file with a list of Evil URLs 
    :return: file reading
    '''

    with open(file) as arq:
        urls = [f.strip() for f in arq]
    for i in range(len(urls)): print(check_EVIL(urls[i]))

def check_url(url):

    '''
    Check connection
    :param url: suspicious url
    :return: status of connection
    '''

    try:
        url = gethostbyname(url)
    except gaierror as err:
        error = '{1}[*] {0}{2}\n'.format(err,yellow,END)
        return error
        exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    check = s.connect_ex((url,80))

    if check == 0:
        msg = '{0}[*] Connection accepted{1}\n'.format(green,END)
    else:
        msg = '{0}[*] Connection refused{1}\n'.format(green, END)

    return msg

def check_list_url(file):

    '''
    Check Evil chars in list of suspicious Evil URL
    :param file: file with a list of Evil URLs
    :return: message with results
    '''

    with open(file) as arq:
        urls_arq = [u.strip() for u in arq]

    msg = ''
    for url in urls_arq:

        bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
        result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]
        check_result = check_url(url)

        if result:
            msg += '\n{0}[*] Evil URL detected: {1}{2}{3}{1}'.format(yellow, END, red, url)
            msg += '\n{0}[*] Evil characters used: {1}{2}{3}{1}\n'.format(yellow, END, red, result)
            msg += check_result

        else:
            msg += '\n{0}[*] Evil URL NOT detected:{1} {2}{3}{1}\n'.format(yellow, END, green, url)
            msg += check_result

    return msg

def main():

    '''
    Main
    :return: execution of the program 
    '''
    args = parse_args()[0]
    parse = parse_args()[1]

    if len(argv) < 2:
        parse.print_help()
        exit(1)

    print(banner())

    if args.url: print(check_EVIL(args.url))
    if args.url and args.check_url: print(check_url(args.url))
    if args.url_list and not args.check_url: urls_list(args.url_list)
    if args.url_list and args.check_url: print(check_list_url(args.url_list))

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: exit()
    except SystemExit: pass













