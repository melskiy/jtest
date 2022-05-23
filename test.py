import unittest
import xmlrunner

class TestSum(unittest.TestCase):

    def test_sum(self):
        f = open('answer.txt', 'r')

        f1 = open('answer1.txt', 'r')
        self.assertEqual(f.read(), f1.read())

        output_file = open('result.xml', "w")

        testRunner = xmlrunner.XMLTestRunner(output=output_file)
        testRunner.run(unittest.main())


if __name__ == '__main__':
    unittest.main()
