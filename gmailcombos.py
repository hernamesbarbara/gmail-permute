#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""gmailcombos.py
"""
import sys
import os

def get_combos(gmail_addr, sep="."):
    combos = []
    gmail_addr = "".join(ch for ch in gmail_addr if ch != ".")
    username = gmail_addr.split("@")[0]
    letters = list(username)
    for i, letter in enumerate(letters):
        if i == 0 or i == len(letters):
            continue
        perm = "".join(letters[:i])+sep+"".join(letters[i:])
        combos.append(perm+"@gmail.com")
    return combos

def main():
    gmail = sys.argv[1]
    for perm in get_combos(gmail):
        print perm
    sys.exit(0)

if __name__ == '__main__':
    main()

