#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fluss0r.

Usage:
  fls.py [-s] [<text>...]
  fls.py -h | --help
  fls.py --version

Options:
  -s            Activate speech output.
  -h --help     Show this screen.
  --version     Show version.

"""
from __future__ import unicode_literals

import os
from docopt import docopt


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
                text = input()
            encrypted = translate(text, MAP1, MAP2)
            print(encrypted)
            if say:
                os.system("say {0}".format(encrypted).encode('utf-8'))
            if words:
                raise EOFError
    except (KeyboardInterrupt, EOFError):
        raise SystemExit

if __name__ == '__main__':
    arguments = docopt(__doc__, version='fluss0r 0.0')
    run_loop(arguments['-s'], arguments['<text>'])
