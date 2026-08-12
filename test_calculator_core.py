import unittest
from decimal import Decimal

from calculator_core import CalculationError, calculate, format_result


class CalculateTests(unittest.TestCase):
    def test_decimal_addition_is_exact(self):
        self.assertEqual(calculate("+", "0.1", "0.2"), Decimal("0.3"))

    def test_division_by_zero_has_a_user_friendly_error(self):
        with self.assertRaisesRegex(CalculationError, "Cannot divide by zero"):
            calculate("/", "5", "0")

    def test_modulo_by_zero_has_a_user_friendly_error(self):
        with self.assertRaisesRegex(CalculationError, "Cannot divide by zero"):
            calculate("%", "5", "0")

    def test_malformed_number_has_a_user_friendly_error(self):
        with self.assertRaisesRegex(CalculationError, "Enter a valid number"):
            calculate("+", "not a number", "2")

    def test_non_finite_number_is_rejected(self):
        with self.assertRaisesRegex(CalculationError, "finite number"):
            calculate("+", "NaN", "2")

    def test_square_root_does_not_require_a_second_operand(self):
        self.assertEqual(calculate("^", "9"), Decimal("3"))

    def test_negative_square_root_has_a_user_friendly_error(self):
        with self.assertRaisesRegex(CalculationError, "negative number"):
            calculate("^", "-1")

    def test_unknown_operation_is_rejected(self):
        with self.assertRaisesRegex(CalculationError, "Choose a valid operation"):
            calculate("?", "1", "2")

    def test_result_format_removes_decimal_noise(self):
        self.assertEqual(format_result(Decimal("12.3400")), "12.34")
        self.assertEqual(format_result(Decimal("0.000")), "0")


if __name__ == "__main__":
    unittest.main()
