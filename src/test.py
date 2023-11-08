import unittest
from calc import apply_vat


class TestStringMethods(unittest.TestCase):
    def test_pr_100_pe_20(self):
        self.assertEqual(120, apply_vat(100.0, 20.0))

    def test_pr_55_25_pe_5_5(self):
        self.assertEqual(58.28875, apply_vat(55.25, 5.5))

    def test_pr_0_pe_10(self):
        self.assertEqual(0, apply_vat(0.0, 10.0),)

    def test_pr_n10_99_pe_10(self):
        self.assertRaises(ValueError, apply_vat, (-10.99), 10.0)

    def test_pr_WrValue_pe_10(self):
        self.assertRaises(ValueError, apply_vat, None, 10.0)

    def test_pr_100_pe_n10(self):
        self.assertRaises(ValueError, apply_vat, 100.0, (-10.0))

    def test_pr_100_pe_110(self):
        self.assertRaises(ValueError, apply_vat, 100.0, 110.0)


if __name__ == '__main__':
    unittest.main()