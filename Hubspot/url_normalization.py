#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def repl_per(ch):
    ch = ch.group()
    #decode reserved characters
    if re.match('^[a-zA-Z0-9\-\._~]{1}$', chr(eval('0x' + ch[1:]))):
        return chr(eval('0x' + ch[1:])).lower()
    #capitalize letters in escape sequences
    return ch.upper()

#find 'percent-encoded octets' and process
def decode_percent(dir_string):
    pat_per = re.compile('%[0-9a-fA-F]{2}')
    return pat_per.sub(repl_per, dir_string)
    
def checkio(url):
    url = url.lower()
    #get 'scheme' and 'host', convert to lower case
    scheme = url.split(':')[0]
    host = url.split('//')[1].split('/')[0]
    #remove default port
    if ':' in host:
        port = int(host.split(':')[1])
        if 80 == port:
            host = host.split(':')[0]
    #remove '.'
    dirs = [d for d in url.split('/')[3:] if d != '.']
    #remove '..'
    while '..' in dirs:
        i = dirs.index('..')
        dirs = dirs[:i-1] + dirs[i+1:]
    
    #escape characters
    dirs = '/' + '/'.join(dirs) if dirs else ''
    return scheme + '://' + host + decode_percent(dirs)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')

