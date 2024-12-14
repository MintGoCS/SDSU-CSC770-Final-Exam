"""This file is for testing purpose only."""

import unittest
from Question01 import Person, BlindPeople, FullTimeMilitary, FullTimeStudent, NormalTaxpayer


class TaxTest(unittest.TestCase):
    """Tax tests."""
    def test_mutation_value(self):
        test_cases = [
            # Format: (income, children)
            (20000, -1),  # children=-1
            (-1, 0),  # income=-1
        ]
        for income, children in test_cases:
            with self.subTest(income=income, children=children):
                with self.assertRaises(ValueError):
                    NormalTaxpayer(income=income, children=children)

    def test_different_incomes(self):
        test_cases = [
            # Format: (income, children, expected_tax)

            # Income range: 0 <= income <= 25,000
            (0, 0, 0 * 0.1),
            (20000, 1, 20000 * 0.08),
            (25000, 2, 25000 * 0.06),

            # Income range: 25,001 <= income <= 55,000
            (25001, 0, 25001 * 0.15),
            (40000, 1, 40000 * 0.12),
            (55000, 2, 55000 * 0.11),

            # Income range: 55,001 <= income <= 105,000
            (55001, 0, 55001 * 0.25),
            (80000, 1, 80000 * 0.23),
            (105000, 2, 105000 * 0.2),

            # Income range: 105,001 <= income <= 205,000
            (105001, 0, 105001 * 0.27),
            (150000, 1, 150000 * 0.25),
            (150000, 3, 150000 * 0.3),

            # Income range: 205,001 <= income <= 255,000
            (205001, 0, 205001 * 0.3),
            (220000, 1, 220000 * 0.28),
            (255000, 3, 255000 * 0.3),

            # Income range: 255,001 <= income <= 405,000
            (255001, 0, 255001 * 0.4),
            (350000, 1, 350000 * 0.36),
            (350000, 3, 350000 * 0.3),

            # Income range: income >= 405,001
            (800000, 0, 800000 * 0.5),
            (800000, 1, 800000 * 0.5),
            (800000, 3, 800000 * 0.5),
        ]

        for income, children, expected_tax in test_cases:
            with self.subTest(income=income, children=children):
                normal_taxpayer = NormalTaxpayer(income=income, children=children)
                self.assertEqual(normal_taxpayer.calculate_tax(), expected_tax)


if __name__ == '__main__':
    unittest.main()
