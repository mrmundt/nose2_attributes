"""
Test_main:
    Tests the printWords function
"""

import unittest
from src.tests.utils import category
from src.main.main import printWords

class MyTestCase(unittest.TestCase):
    @category('normal', 'fun')
    def test_printWords(self):
        self.assertEqual(printWords(['hello']), ['hello'])
