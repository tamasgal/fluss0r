#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys, os

MAP1, MAP2 = "abcdefghijklmnopqrstuvwxyzäöüß",\
             "ökpgihdfeßbvszücwtmrälqyxnuaoj"

def translate(text, map1, map2):
    map1 += map1.upper()
    map2 += map2.upper()
    def translate_char(c):
        try: return map2[map1.index(c)]
        except ValueError: return c
    return "".join(translate_char(c) for c in text)

def run_loop(say=False, words=None):
    try:
        while True:
            if words:
                text = " ".join(words)
            else:
                text = raw_input().decode('utf-8')
            encrypted = translate(text, MAP1, MAP2)
            print(encrypted)
            if say:
                os.system("say {0}".format(encrypted).encode('utf-8'))
            if words:
                raise EOFError
    except (KeyboardInterrupt, EOFError):
        raise SystemExit

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit("Usage: fl.py [-s] [<words>...]")
    say = '-s' in sys.argv[:2]
    words = [word for word in sys.argv[1:] if word != '-s']
    run_loop(say, words) 
