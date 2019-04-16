import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import unittest
from unittest.mock import Mock, patch
import json
import wordbook


class WordBookTest(unittest.TestCase):
    """Test to wordbook
    """

    def test_print_txt(self):
        expected = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.\n"
        actual = wordbook.print_txt("sample.txt")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()