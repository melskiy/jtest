import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        f = open('answer.txt', 'r')

        f1 = open('answer1.txt', 'r')
        self.assertEqual(f.read(), f1.read())


if __name__ == '__main__':
    unittest.main()
