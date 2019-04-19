import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import unittest
from unittest.mock import Mock, patch
import json
import wordbook


class WordBookTest(unittest.TestCase):
    """Test to wordbook
    """

    def test_remove(self):
        expected = ["hogehoge"]
        actual = wordbook.remove(["as", "the", "hogehoge"], "input\\remove.txt")
        self.assertEqual(expected, actual)
        
    # def test_cut_sentence(self):
    #     expected = ["b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k", "b", "c", "d", "e", "f", "g", "h", "j", "k"]
    #     actual = wordbook.cut_sentence("input\\sample.txt", "input\\remove.txt")
    #     self.assertEqual(expected, actual)

    def test_sort_format(self):
        expected  = [["g", 1000], ["k", 110], ["e", 100], ["i", 100], ["l", 99], ["h", 89], ["j", 53], ["d", 30], ["b", 15], ["a", 10]]
        test_case = {"a": 10, "b": 15, "c": 1, "d": 30, "e": 100, "f": 0, "g": 1000, "h": 89, "i": 100, "j": 53, "k": 110, "l": 99}
        actual = wordbook.sort_format(test_case)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()