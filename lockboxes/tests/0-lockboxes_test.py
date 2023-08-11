#!/usr/bin/python3
"""Unittest for canUnlockAll([..])
"""
import unittest
canUnlockAll = __import__('0-lockboxes').canUnlockAll


class TestCanUnlockAll(unittest.TestCase):

    def test_canUnlockAll(self):
        self.assertEqual(canUnlockAll([[1], [2], [3], [4], []]), True)
        self.assertTrue(canUnlockAll([[1], [2], [3], [4], []]))
        self.assertTrue(canUnlockAll([[1], [2, 28, 45], [3], [4], []]))

    def test_cannot_accept_str(self):
        with self.assertRaises(TypeError):
            canUnlockAll([[1], [2], [3], ['str'], []])

    def test_cannot_accept_float(self):
        with self.assertRaises(TypeError):
            canUnlockAll([[1], [2, 3.4], [3], [4], []])
