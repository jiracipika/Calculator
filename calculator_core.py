"""Validated, decimal-based calculation logic shared by calculator interfaces."""

from decimal import Decimal, InvalidOperation, localcontext
from typing import Optional


class CalculationError(ValueError):
    """An error that can be displayed directly to a calculator user."""


def _parse_number(value: str) -> Decimal:
    try:
        number = Decimal(value.strip())
    except (AttributeError, InvalidOperation):
        raise CalculationError("Enter a valid number.") from None

    if not number.is_finite():
        raise CalculationError("Enter a finite number.")
    return number


def calculate(operation: str, first: str, second: Optional[str] = None) -> Decimal:
    """Calculate an operation from user-entered decimal strings.

    ``^`` represents square root and ignores the second operand. All expected
    input failures are normalized to ``CalculationError`` for safe UI display.
    """

    if operation not in {"+", "-", "*", "/", "%", "^"}:
        raise CalculationError("Choose a valid operation.")

    left = _parse_number(first)
    if operation == "^":
        if left < 0:
            raise CalculationError("Cannot take the square root of a negative number.")
        with localcontext() as context:
            context.prec = 28
            return left.sqrt()

    if second is None:
        raise CalculationError("Enter a second number.")
    right = _parse_number(second)

    if operation in {"/", "%"} and right == 0:
        raise CalculationError("Cannot divide by zero.")

    if operation == "+":
        return left + right
    if operation == "-":
        return left - right
    if operation == "*":
        return left * right
    if operation == "/":
        return left / right
    return left % right


def format_result(value: Decimal) -> str:
    """Return a readable non-exponential representation of a result."""

    if value == 0:
        return "0"
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text
