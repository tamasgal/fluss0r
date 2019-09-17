#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fluss0r.

Usage:
  fluss0r.py
  fluss0r.py [-i -s]
  fluss0r.py -h | --help
  fluss0r.py --version

Options:
  -i            Interactive session.
  -s            Activate speech output.
  -h --help     Show this screen.
  --version     Show version.

"""
from __future__ import unicode_literals

import os
from docopt import docopt


FROM_MAP = "abcdefghijklmnopqrstuvwxyzäöüß"
TO_MAP = "ökpgihdfeßbvszücwtmrälqyxnuaoj"


def translate(text, map1, map2):
    map1 += map1.upper()
    map2 += map2.upper()
    def translate_char(c):
        try: return map2[map1.index(c)]
        except ValueError: return c
    return "".join(translate_char(c) for c in text)


class UniversalTranslator(object):
    def __init__(self, from_map, to_map):
        self.from_map = from_map + from_map.upper()
        self.to_map = to_map + to_map.upper()

    def __call__(self, text, decrypt=False):
        if decrypt:
            return self.decrypt(text)
        return self.encrypt(text)

    def encrypt(self, text):
        return self._project(text, self.from_map, self.to_map)

    def decrypt(self, text):
        return self._project(text, self.to_map, self.from_map)

    def _project(self, text, code1, code2):
        return "".join(self._project_char(c, code1, code2) for c in text)

    def _project_char(self, char, code1, code2):
        try:
            return code2[code1.index(char)]
        except ValueError:
            return char


def run_loop(prompt, say=False):
    translator = UniversalTranslator(FROM_MAP, TO_MAP)
    try:
        while True:
            text = input(prompt)
            encrypted = translator.encrypt(text)
            print(encrypted)
            if say:
                os.system("say {0}".format(encrypted).encode('utf-8'))
    except (KeyboardInterrupt, EOFError):
        raise SystemExit


if __name__ == '__main__':
    arguments = docopt(__doc__, version='fluss0r 0.0')
    prompt = ""
    if arguments['-i']:
        prompt = "> "
    run_loop(prompt, arguments['-s'])
