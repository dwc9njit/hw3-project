"""
Unit tests for the Calculator class and its operations.
"""
from decimal import Decimal
import pytest
from calculator import Calculator
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide, exponent

@pytest.fixture(autouse=True)
def clear_history():
    """Fixture to clear calculation history before each test."""
    Calculations.clear_history()

def test_add():
    """Test addition operation."""
    result = Calculator.add(Decimal('1'), Decimal('1'))
    assert result == Decimal('2'), "Addition result should be 2"
    assert len(Calculations.history) == 1

def test_subtract():
    """Test subtraction operation."""
    result = Calculator.subtract(Decimal('2'), Decimal('1'))
    assert result == Decimal('1'), "Subtraction result should be 1"
    assert len(Calculations.history) == 1

def test_multiply():
    """Test multiplication operation."""
    result = Calculator.multiply(Decimal('2'), Decimal('2'))
    assert result == Decimal('4'), "Multiplication result should be 4"
    assert len(Calculations.history) == 1

def test_divide():
    """Test division operation."""
    result = Calculator.divide(Decimal('4'), Decimal('2'))
    assert result == Decimal('2'), "Division result should be 2"
    assert len(Calculations.history) == 1

def test_divide_by_zero():
    """Test division by zero handling."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        Calculator.divide(Decimal('1'), Decimal('0'))
    assert len(Calculations.history) == 0, "No calculation should be added on division by zero error"

def test_exponent():
    """Test exponentiation operation."""
    result = Calculator.exponent(Decimal('2'), Decimal('3'))
    assert result == Decimal('8'), "Exponentiation result should be 8"
    assert len(Calculations.history) == 1

@pytest.mark.parametrize("operation", [add, subtract, multiply, divide, exponent])
def test_perform_operation_error_handling(operation):
    """Test error handling in perform_operation for all operations."""
    # Simulate an error by passing invalid types
    result = Calculator.perform_operation(Decimal('1'), 'a', operation)
    assert result == Decimal('0'), "Expected result to be Decimal('0') on error"
    assert len(Calculations.history) == 0, "No calculation should be added on error"

def test_calculations_history():
    """Test calculations history."""
    Calculator.add(Decimal('1'), Decimal('1'))
    Calculator.subtract(Decimal('2'), Decimal('1'))
    Calculator.multiply(Decimal('2'), Decimal('2'))
    Calculator.divide(Decimal('4'), Decimal('2'))
    Calculator.exponent(Decimal('2'), Decimal('3'))

    assert len(Calculations.history) == 5, "Five calculations should be in history"

    latest_calc = Calculations.get_latest()
    assert latest_calc.perform_operation() == Decimal('8'), "Latest calculation result should be 8"

    first_calc = Calculations.history[0]
    assert first_calc.perform_operation() == Decimal('2'), "First calculation result should be 2"
