#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys

ndict = {
    '*)': '(*',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def is_nested(line):
    count = 0
    nlist = []
    while line:
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        if line.startswith("*)"):
            token = "*)"
        count += 1
        if token in ndict.values():
            nlist.append(token)
        elif token in ndict.keys():
            a = ndict[token]
            b = nlist.pop()
            if a != b:
                return "NO " + str(count)
        line = line[len(token):]
    if nlist:
        return "NO " + str(count)
    else:
        return "YES"


def main(args):
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as w:
            for line in f:
                result = is_nested(line)
                w.write(result+'\n')


if __name__ == '__main__':
    main(sys.argv[1:])
