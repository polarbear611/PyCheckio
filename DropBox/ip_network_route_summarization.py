#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
def decimal_to_binary(ip):
    decimals = ip.split('.')
    ip_str = ''
    for d in decimals:
        ip_str += bin(int(d))[2:].zfill(8)
    return ip_str
    
def longest_common_prefix(ip_list):
    for i in range(len(ip_list[0])):
        for ip in ip_list:
            if ip[i] != ip_list[0][i]:
                return ip_list[0][:i]
    return ip_list[0]
    
def checkio(data):
    ip_list = [decimal_to_binary(ip) for ip in data]
    lcp = longest_common_prefix(ip_list)
    return ".".join([str(int(d, 2)) for d in re.findall('.{8}', lcp.ljust(32, '0'))]) + '/' + str(len(lcp))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"

