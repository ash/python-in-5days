# This is the test script with contains the code to test the 'factorial' functions.
# We moved all the testing code to this file.

import unittest
import factorial

class TC(unittest.TestCase):
    def test_fact_of_1(self):
        self.assertEqual(fact(1), 1)
    def test_fact_of_2(self):
        self.assertEqual(fact(2), 3)
    def test_fact_of_2(self):
        self.assertTrue(fact(2) == 3)
    def test_fact_of_5(self):
        self.assertEqual(fact(5), 120)


unittest.main()

# text fixture 
# test case
# test suite
# test runner
