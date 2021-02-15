import unittest
import main


class TestMain(unittest.TestCase):

    def test_choose(self):
        result1 = main.choose("46732123453")
        result2 = main.choose("46734084452")
        result3 = main.choose("26875649874")
        result4 = main.choose("44732123457")
        result5 = main.choose("68123456789")

        self.assertEqual(result1, "OperatorB")
        self.assertEqual(result2, "OperatorA")
        self.assertEqual(result3, "OperatorA")
        self.assertEqual(result4, "OperatorB")
        self.assertEqual(result5, "No operator")


if __name__ == "__main__":
    unittest.main()
