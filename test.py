"""This file is for CSC770 Final Exam Question 1 testing purpose only."""

import unittest
from Question01 import Person, BlindPeople, FullTimeMilitary, FullTimeStudent, NormalTaxpayer


class TaxTest(unittest.TestCase):
    """Tax tests."""
    def test_mutation_value(self):
        """
        Test the tax calculation for mutation cases.
        Test A taxpayer with negative number of children,
        or negative number of income.
        """
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
        """
        Test the tax calculation for normal income cases,
        including multiple boundary values.
        The social security tax (6.5%) is required.
        """
        test_cases = [
            # Format: (income, children, expected_tax)
            # income: the income for a normal taxpayer.
            # children: the number of children the normal taxpayer has.
            # expected_tax: the expected total tax (income tax + social security tax)

            # Case Group 1
            # Income range: 0 <= income < 25,000
            (0, 0, 0),
            (20000, 1, 20000 * 0.08 + 20000 * 0.065),
            (24999.99, 2, 24999.99 * 0.06 + 24999.99 * 0.065),

            # Case Group 2
            # Income range: 25,000 <= income < 55,000
            (25000, 0, 25000 * 0.15 + 25000 * 0.065),
            (40000, 1, 40000 * 0.12 + 40000 * 0.065),
            (54999.99, 2, 54999.99 * 0.11 + 54999.99 * 0.065),

            # Case Group 3
            # Income range: 55,000 <= income < 105,000
            (55000, 0, 55000 * 0.25 + 55000 * 0.065),
            (80000, 1, 80000 * 0.23 + 80000 * 0.065),
            (104999.99, 2, 104999.99 * 0.2 + 104999.99 * 0.065),

            # Case Group 4
            # Income range: 105,000 <= income < 205,000
            (105000, 0, 105000 * 0.27 + 105000 * 0.065),
            (150000, 1, 150000 * 0.25 + 150000 * 0.065),
            (204999.99, 3, 204999.99 * 0.30 + 204999.99 * 0.065),

            # Case Group 5
            # Income range: 205,000 <= income < 255,000
            (205000, 0, 205000 * 0.30 + 205000 * 0.065),
            (220000, 1, 220000 * 0.28 + 220000 * 0.065),
            (254999.99, 3, 254999.99 * 0.30 + 254999.99 * 0.065),

            # Case Group 6
            # Income range: 255,000 <= income < 405,000
            (255000, 0, 255000 * 0.40 + 255000 * 0.065),
            (350000, 1, 350000 * 0.36 + 350000 * 0.065),
            (349999.99, 3, 349999.99 * 0.30 + 349999.99 * 0.065),

            # Case Group 7
            # Income range: income >= 405,000
            (405000, 0, 405000 * 0.5 + 405000 * 0.065),
            (800000, 1, 800000 * 0.5 + 800000 * 0.065),
            (800000, 3, 800000 * 0.5 + 800000 * 0.065),
        ]

        for income, children, expected_tax in test_cases:
            with self.subTest(income=income, children=children):
                normal_taxpayer = NormalTaxpayer(income=income, children=children)
                self.assertEqual(normal_taxpayer.calculate_tax(), expected_tax)

    def test_full_time_students(self):
        """
        Test the tax calculation for full-time students.
        Full-time students receive a 70% discount on income tax.
        The social security tax (6.5%) is required.
        """
        test_cases = [
            # Format: (income, children, expected_tax)
            # income: the income for a full-time student.
            # children: the number of children the full-time student has.
            # expected_tax: the expected total tax (income tax + social security tax)

            # Case Student 1
            (0, 0, 0),

            # Case Student 2
            # expected_tax: income tax = 5000 * 10% (income <= 25,000, 0 child) * 70% (discount)
            #               social security tax = 5000 * 6.5%
            #               total tax = income tax + social security tax
            (5000, 0, 5000 * 0.1 * 0.7 + 5000 * 0.065),

        ]

        for income, children, expected_tax in test_cases:
            with self.subTest(income=income, children=children):
                full_time_student = FullTimeStudent(income=income, children=children)
                self.assertEqual(full_time_student.calculate_tax(), expected_tax)

    def test_full_time_military(self):
        """
        Test the tax calculation for full-time military.
        Full-time militaries receive a 75% discount on both income tax and social security tax.
        The social security tax (6.5%) is required before discount applied.
        """
        test_cases = [
            # Format: (income, children, expected_tax)
            # income: the income for a full-time military.
            # children: the number of children the full-time military has.
            # expected_tax: the expected total tax (income tax + social security tax)

            # Case Military 1
            # expected_tax: income tax = 65000 * 20% (income <= 105,000, 3 children) * 75% (discount)
            #               social security tax = 65000 * 6.5% * 75% (discount)
            #               total tax = income tax + social security tax
            (65000, 3, 65000 * 0.2 * 0.75 + 65000 * 0.065 * 0.75),

            # Case Military 2
            (37800, 0, 37800 * 0.15 * 0.75 + 37800 * 0.065 * 0.75),

        ]

        for income, children, expected_tax in test_cases:
            with self.subTest(income=income, children=children):
                full_time_military = FullTimeMilitary(income=income, children=children)
                self.assertEqual(full_time_military.calculate_tax(), expected_tax)

    def test_blind_people(self):
        """
        Test the tax calculation for blind people.
        Blind people whose income are lower than 65,000 will not be tax but social security tax is required.
        The social security tax is 6.5%.
        """
        test_cases = [
            # Format: (income, children, expected_tax)
            # income: the income for a blind people.
            # children: the number of children the blind people has.
            # expected_tax: the expected total tax (income tax + social security tax)

            # Case Blind people 1
            # expected_tax: income tax = 0
            #               social security tax = 30,000 * 6.5%
            #               total tax = income tax + social security tax
            (30000, 1, 0 + 30000 * 0.065),

            # Case Blind people 2
            (125800, 0, 125800 * 0.27 + 125800 * 0.065),

        ]

        for income, children, expected_tax in test_cases:
            with self.subTest(income=income, children=children):
                blind_people = BlindPeople(income=income, children=children)
                self.assertEqual(blind_people.calculate_tax(), expected_tax)


if __name__ == '__main__':
    unittest.main()
