# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fl import translate

import unittest


class TestTranslate(unittest.TestCase):

    def test_translate_char(self):
        c2 = translate('a', 'abc', 'def')
        self.assertEqual('d', c2)

    def test_translate_uppercase_char(self):
        c2 = translate('A', 'abc', 'def')
        self.assertEqual('D', c2)

    def test_translate_digit(self):
        c2 = translate('5', 'abc', 'def')
        self.assertEqual('5', c2)

    def test_translate_unicode_char(self):
        c2 = translate('ä', 'äbc', 'def')
        self.assertEqual('d', c2)

    def test_translate_uppercase_unicode_char(self):
        c2 = translate('Ä', 'äbc', 'def')
        self.assertEqual('D', c2)

    def test_translate_keeps_unlisted_chars(self):
        c2 = translate('z', 'abc', 'def')
        self.assertEqual('z', c2)

    def test_tranlsate_keeps_whitespace(self):
        c2 = translate(' ', 'abc', 'def')
        self.assertEqual(' ', c2)

    def test_translate_keeps_special_chars(self):
        c2 = translate('\r\t\n', 'abc', 'def')
        self.assertEqual('\r\t\n', c2)

    def test_translate_string(self):
        c2 = translate('aabbcc', 'abc', 'def')
        self.assertEqual('ddeeff', c2)

    def test_translate_sentence(self):
        c2 = translate('Bac Cab bba ab!', 'abc', 'def')
        self.assertEqual('Edf Fde eed de!', c2)

