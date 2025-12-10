"""
Scientific Calculator Module

Concrete implementation of BaseCalculator that performs scientific calculations.
Uses sympy library for advanced mathematical operations.
"""

from typing import Dict, Any
import math
from sympy import (
    sympify, sqrt, cbrt, sin, cos, tan, 
    log, ln, factorial, pi, E, N
)
from .base_calculator import BaseCalculator


class ScientificCalculator(BaseCalculator):
    """
    Scientific calculator that supports advanced mathematical operations.
    
    Supported operations:
    - Basic: add, subtract, multiply, divide
    - Powers: power, square, cube
    - Roots: sqrt, cbrt
    - Trigonometry: sin, cos, tan (in degrees)
    - Logarithms: log (base 10), ln (natural log)
    - Factorials: factorial
    
    This is a concrete implementation of BaseCalculator, demonstrating
    the Open/Closed principle in action.
    """
    
    def __init__(self):
        """Initialize the scientific calculator."""
        # Define supported operations
        self.supported_operations = {
            'add', 'subtract', 'multiply', 'divide',
            'power', 'square', 'cube',
            'sqrt', 'cbrt',
            'sin', 'cos', 'tan',
            'log', 'ln',
            'factorial'
        }
    
    def supports_operation(self, operation: str) -> bool:
        """
        Check if this calculator supports the given operation.
        
        Args:
            operation: The operation name
            
        Returns:
            True if supported, False otherwise
        """
        return operation in self.supported_operations
    
    def calculate(self, parsed_data: Dict) -> Any:
        """
        Perform the calculation based on parsed data.
        
        Args:
            parsed_data: Dictionary with 'operation' and 'operands'
            
        Returns:
            Calculation result
            
        Raises:
            ValueError: If operation is not supported or invalid operands
            ZeroDivisionError: If division by zero is attempted
            
        Example:
            >>> calc = ScientificCalculator()
            >>> calc.calculate({'operation': 'add', 'operands': [2, 3]})
            5.0
        """
        operation = parsed_data.get('operation')
        operands = parsed_data.get('operands', [])
        
        if not operation:
            raise ValueError("No operation specified")
        
        if not self.supports_operation(operation):
            raise ValueError(f"Operation '{operation}' is not supported")
        
        # Route to appropriate calculation method
        if operation == 'add':
            return self._add(operands)
        elif operation == 'subtract':
            return self._subtract(operands)
        elif operation == 'multiply':
            return self._multiply(operands)
        elif operation == 'divide':
            return self._divide(operands)
        elif operation in ['power', 'square', 'cube']:
            return self._power(operands)
        elif operation == 'sqrt':
            return self._sqrt(operands)
        elif operation == 'cbrt':
            return self._cbrt(operands)
        elif operation == 'sin':
            return self._sin(operands)
        elif operation == 'cos':
            return self._cos(operands)
        elif operation == 'tan':
            return self._tan(operands)
        elif operation == 'log':
            return self._log(operands)
        elif operation == 'ln':
            return self._ln(operands)
        elif operation == 'factorial':
            return self._factorial(operands)
        else:
            raise ValueError(f"Operation '{operation}' not implemented")
    
    def _add(self, operands: list) -> float:
        """Add two or more numbers."""
        if len(operands) < 2:
            raise ValueError("Addition requires at least 2 operands")
        return float(sum(operands))
    
    def _subtract(self, operands: list) -> float:
        """Subtract second number from first."""
        if len(operands) != 2:
            raise ValueError("Subtraction requires exactly 2 operands")
        return float(operands[0] - operands[1])
    
    def _multiply(self, operands: list) -> float:
        """Multiply two or more numbers."""
        if len(operands) < 2:
            raise ValueError("Multiplication requires at least 2 operands")
        result = 1
        for num in operands:
            result *= num
        return float(result)
    
    def _divide(self, operands: list) -> float:
        """Divide first number by second."""
        if len(operands) != 2:
            raise ValueError("Division requires exactly 2 operands")
        if operands[1] == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return float(operands[0] / operands[1])
    
    def _power(self, operands: list) -> float:
        """Raise first number to the power of second."""
        if len(operands) != 2:
            raise ValueError("Power operation requires exactly 2 operands")
        return float(operands[0] ** operands[1])
    
    def _sqrt(self, operands: list) -> float:
        """Calculate square root."""
        if len(operands) != 1:
            raise ValueError("Square root requires exactly 1 operand")
        if operands[0] < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return float(sqrt(operands[0]))
    
    def _cbrt(self, operands: list) -> float:
        """Calculate cube root."""
        if len(operands) != 1:
            raise ValueError("Cube root requires exactly 1 operand")
        return float(cbrt(operands[0]))
    
    def _sin(self, operands: list) -> float:
        """Calculate sine (input in degrees)."""
        if len(operands) != 1:
            raise ValueError("Sine requires exactly 1 operand")
        # Convert degrees to radians
        radians = math.radians(operands[0])
        return float(math.sin(radians))
    
    def _cos(self, operands: list) -> float:
        """Calculate cosine (input in degrees)."""
        if len(operands) != 1:
            raise ValueError("Cosine requires exactly 1 operand")
        # Convert degrees to radians
        radians = math.radians(operands[0])
        return float(math.cos(radians))
    
    def _tan(self, operands: list) -> float:
        """Calculate tangent (input in degrees)."""
        if len(operands) != 1:
            raise ValueError("Tangent requires exactly 1 operand")
        # Convert degrees to radians
        radians = math.radians(operands[0])
        return float(math.tan(radians))
    
    def _log(self, operands: list) -> float:
        """Calculate logarithm base 10."""
        if len(operands) != 1:
            raise ValueError("Logarithm requires exactly 1 operand")
        if operands[0] <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number")
        return float(math.log10(operands[0]))
    
    def _ln(self, operands: list) -> float:
        """Calculate natural logarithm."""
        if len(operands) != 1:
            raise ValueError("Natural logarithm requires exactly 1 operand")
        if operands[0] <= 0:
            raise ValueError("Cannot calculate natural logarithm of non-positive number")
        return float(math.log(operands[0]))
    
    def _factorial(self, operands: list) -> int:
        """Calculate factorial."""
        if len(operands) != 1:
            raise ValueError("Factorial requires exactly 1 operand")
        if operands[0] < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        if operands[0] != int(operands[0]):
            raise ValueError("Factorial requires an integer")
        return int(factorial(int(operands[0])))
