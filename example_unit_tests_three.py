import unittest

class TestClassThree(unittest.TestCase):

    def test_correct_three(self):

        self.assertEqual("abc", "abc")


    def test_false_three(self):

        self.assertEqual("testing message 3", "empty")


if __name__ == '__main__':
    import sys
    sys.path.append("/home/diderik/cloud/dags/")
    unittest.main(verbosity=2)
