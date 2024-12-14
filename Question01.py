"""The code is for CSC770 Final Exam."""

# Question 1

# Definition of Social Security rate.
SOCIAL_SECURITY_RATE = 0.065


class Person:
    # Define the rate into a list based on an individual's income and number of descendents.
    TAX_RATES = [
        # 1. Mapping the income range into a tuple.
        # 2. Mapping the number of descents into the dictionary.
        # 0 -> No child, 1 -> one child, "more_than_2" -> having more than 2 children
        {"income_range": (0, 25000), "rates": {0: 0.1, 1: 0.08, "more_than_2": 0.06}},
        {"income_range": (25001, 55000), "rates": {0: 0.15, 1: 0.12, "more_than_2": 0.11}},
        {"income_range": (55001, 105000), "rates": {0: 0.25, 1: 0.23, "more_than_2": 0.2}},
        {"income_range": (105001, 205000), "rates": {0: 0.27, 1: 0.25, "more_than_2": 0.3}},
        {"income_range": (205001, 255000), "rates": {0: 0.3, 1: 0.28, "more_than_2": 0.3}},
        {"income_range": (255001, 405000), "rates": {0: 0.4, 1: 0.36, "more_than_2": 0.3}},
        {"income_range": (405000, float("inf")), "rates": {0: 0.5, 1: 0.5, "more_than_2": 0.5}},
    ]

    def __init__(self, income, children):
        if income < 0:
            raise ValueError("Invalid number of income")
        elif children < 0:
            raise ValueError("Invalid number of children")
        self.income = income
        self.children = children

    def get_children_key(self):
        """Determine the tax rate based on the number of children."""
        # No child in the household.
        if self.children == 0:
            return 0
        # Have 1 child in the household.
        elif self.children == 1:
            return 1
        # Have more than 2 children in the household.
        elif self.children >= 2:
            return "more_than_2"

    def calculate_base_tax(self):
        """Calculate the base tax based on the number of children and income level."""
        for rule in self.TAX_RATES:
            # e.g. for the income range (0, 5000), the left_income is 0, while the right_income is 5000.
            left_income, right_income = rule["income_range"]

            # If a person's income is within in the range.
            if left_income <= self.income <= right_income:
                tax_rate = rule["rates"].get(self.get_children_key())
                return self.income * tax_rate
        # raise ValueError("Invalid income range.")


class BlindPeople(Person):
    """Blind people will not pay income tax if income is lower than $65,000,
    but still need to pay Social Security Tax."""

    def calculate_tax(self):
        # Calculate the social security.
        social_security = SOCIAL_SECURITY_RATE * self.income

        if self.income < 65000:
            base_tax = 0  # Income tax will be waived of income is lower than 65,000.
        else:
            # Calculate the income tax.
            base_tax = self.calculate_base_tax()

        # Sum up the social security and income tax.
        total_tax = social_security + base_tax

        return total_tax


class FullTimeMilitary(Person):
    """Full time military people will apply 75% discount of Income tax rate and Social Security Tax."""

    def calculate_tax(self):
        SPECIAL_DISCOUNT = 0.75

        # Calculate the social security with a discount.
        social_security = SOCIAL_SECURITY_RATE * self.income * SPECIAL_DISCOUNT

        # Calculate the income tax with a discount.
        base_tax = self.calculate_base_tax() * SPECIAL_DISCOUNT

        # Sum up the social security and income tax.
        total_tax = social_security + base_tax

        return total_tax


# Definition of identity of the taxpayers.
class FullTimeStudent(Person):
    """Full time student will apply 70% discount of Income tax rate
    but no discount on Social Security Tax."""

    def calculate_tax(self):
        SPECIAL_DISCOUNT = 0.7

        # Calculate the social security and income tax.
        social_security = SOCIAL_SECURITY_RATE * self.income

        # Calculate the income tax and apply special discounts for Full Time Students.
        base_tax = self.calculate_base_tax() * SPECIAL_DISCOUNT

        # Sum up the social security and income tax.
        total_tax = social_security + base_tax

        return total_tax


class NormalTaxpayer(Person):
    """This is for normal taxpayer."""

    def calculate_tax(self):
        # Calculate the social security and income tax.
        social_security = SOCIAL_SECURITY_RATE * self.income

        # Calculate the income tax.
        base_tax = self.calculate_base_tax()

        # Sum up the social security and income tax.
        total_tax = social_security + base_tax

        return total_tax
