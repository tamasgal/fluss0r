#!/usr/bin/env python

from misc import BiDict

import unittest


class TestBiDict(unittest.TestCase):
    def setUp(self):
        self.data = {'a': 1, 'b': 2}
        self.bidict = BiDict(self.data)

    def test_bi_map(self):
        self.assertEqual(self.data, self.bidict.bi_map)

    def test_get_value_matches(self):
        self.assertEqual(1, self.bidict.get('a'))
        self.assertEqual(2, self.bidict.get('b'))

    def test_get_reversed_value_matches(self):
        self.assertEqual('a', self.bidict.get_reversed(1))
        self.assertEqual('b', self.bidict.get_reversed(2))

    def test_get_value_raises_keyerror_for_non_existent_value(self):
        with self.assertRaises(KeyError):
            self.bidict.get(3)




