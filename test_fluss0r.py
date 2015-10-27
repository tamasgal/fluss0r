# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fluss0r import UniversalTranslator

import unittest

class TestUniversalTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = UniversalTranslator("abcäöü", "bcaüäö")

    def test_project_char(self):
        proj_char = self.translator._project_char("a", code1="a", code2="b")
        self.assertEqual("b", proj_char)

    def test_project(self):
        projected = self.translator._project("abc", code1="abcd", code2="dbca")
        self.assertEqual(projected, "dbc")

    def test_encrypt(self):
        encrypted = self.translator.encrypt("abc")
        self.assertEqual(encrypted, "bca")
        encrypted = self.translator.encrypt("cba")
        self.assertEqual(encrypted, "acb")

    def test_encrypt_unicode(self):
        encrypted = self.translator.encrypt(u"äöü")
        self.assertEqual(encrypted, u"üäö")

    def test_decrypt(self):
        decrypted = self.translator.decrypt("bca")
        self.assertEqual(decrypted, "abc")
        decrypted = self.translator.decrypt("bac")
        self.assertEqual(decrypted, "acb")

    def test_direct_call(self):
        encrypted = self.translator("abc")
        self.assertEqual(encrypted, "bca")

    def test_direct_call_decrypt(self):
        encrypted = self.translator("bca", decrypt=True)
        self.assertEqual(encrypted, "abc")

    def test_returns_char_if_not_listed(self):
        encrypted = self.translator("z")
        self.assertEqual("z", encrypted)

    def test_returns_mixed_translation_if_some_chars_arent_listed(self):
        encrypted = self.translator("az narf")
        self.assertEqual("bz nbrf", encrypted)

    def test_pick_first_hit_when_ambigous_definition(self):
        translator = UniversalTranslator("aab", "cde")
        encrypted = translator("aba")
        self.assertEqual("cec", encrypted)

    def test_mixed_case_encryptions(self):
        encrypted = self.translator("AbC")
        self.assertEqual("BcA", encrypted)

    def test_mixed_case_encryptions_with_unicode(self):
        encrypted = self.translator("ÄbCöÜ")
        self.assertEqual("ÜcAäÖ", encrypted)

    def test_mixed_case_decryptions(self):
        decrypted = self.translator("BcA", decrypt=True)
        self.assertEqual("AbC", decrypted)

    def test_mixed_case_decryptions_with_unicode(self):
        decrypted = self.translator("ÖcüÄ", decrypt=True)
        self.assertEqual("ÜbäÖ", decrypted)
