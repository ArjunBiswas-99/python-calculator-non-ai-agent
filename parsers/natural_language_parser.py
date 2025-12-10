"""
Natural Language Parser Module

Concrete implementation of BaseParser that understands natural language queries.
This parser converts conversational input into structured calculation data.
"""

import re
from typing import Dict, Optional
from .base_parser import BaseParser


class NaturalLanguageParser(BaseParser):
    """
    Parser that understands natural language mathematical queries.
    
    Examples it can handle:
    - "What's 2 + 2?"
    - "Calculate square root of 144"
    - "What's 5 squared?"
    - "sin of 30 degrees"
    
    This is a concrete implementation of BaseParser, demonstrating
    the Open/Closed principle in action.
    """
    
    def __init__(self):
        """Initialize the natural language parser with operation patterns."""
        # Define patterns for different operations
        # Each pattern maps to an operation type
        self.patterns = {
            # Basic arithmetic
            'add': [
                r'(?:what\'?s?|calculate|compute)?\s*(\d+\.?\d*)\s*(?:\+|plus|add)\s*(\d+\.?\d*)',
                r'(?:add|sum)\s*(\d+\.?\d*)\s*(?:and|to)\s*(\d+\.?\d*)',
            ],
            'subtract': [
                r'(?:what\'?s?|calculate)?\s*(\d+\.?\d*)\s*(?:-|minus|subtract)\s*(\d+\.?\d*)',
                r'(?:subtract)\s*(\d+\.?\d*)\s*from\s*(\d+\.?\d*)',
            ],
            'multiply': [
                r'(?:what\'?s?|calculate)?\s*(\d+\.?\d*)\s*(?:\*|×|times|multiply)\s*(\d+\.?\d*)',
                r'(?:multiply)\s*(\d+\.?\d*)\s*(?:by|and)\s*(\d+\.?\d*)',
            ],
            'divide': [
                r'(?:what\'?s?|calculate)?\s*(\d+\.?\d*)\s*(?:/|÷|divided by|divide)\s*(\d+\.?\d*)',
                r'(?:divide)\s*(\d+\.?\d*)\s*by\s*(\d+\.?\d*)',
            ],
            
            # Powers and roots
            'power': [
                r'(\d+\.?\d*)\s*(?:to the power of|raised to|power)\s*(\d+\.?\d*)',
                r'(\d+\.?\d*)\s*\*\*\s*(\d+\.?\d*)',
            ],
            'square': [
                r'(\d+\.?\d*)\s*squared',
                r'square\s*(?:of)?\s*(\d+\.?\d*)',
            ],
            'cube': [
                r'(\d+\.?\d*)\s*cubed',
                r'cube\s*(?:of)?\s*(\d+\.?\d*)',
            ],
            'sqrt': [
                r'(?:square root|sqrt)\s*(?:of)?\s*(\d+\.?\d*)',
                r'√\s*(\d+\.?\d*)',
            ],
            'cbrt': [
                r'(?:cube root|cbrt)\s*(?:of)?\s*(\d+\.?\d*)',
            ],
            
            # Trigonometry (assumes degrees)
            'sin': [
                r'(?:sin|sine)\s*(?:of)?\s*(\d+\.?\d*)\s*(?:degrees?)?',
            ],
            'cos': [
                r'(?:cos|cosine)\s*(?:of)?\s*(\d+\.?\d*)\s*(?:degrees?)?',
            ],
            'tan': [
                r'(?:tan|tangent)\s*(?:of)?\s*(\d+\.?\d*)\s*(?:degrees?)?',
            ],
            
            # Logarithms
            'log': [
                r'(?:log|logarithm)\s*(?:of)?\s*(\d+\.?\d*)',
            ],
            'ln': [
                r'(?:ln|natural log)\s*(?:of)?\s*(\d+\.?\d*)',
            ],
            
            # Factorial
            'factorial': [
                r'(\d+)\s*factorial',
                r'factorial\s*(?:of)?\s*(\d+)',
            ],
        }
    
    def can_handle(self, input_text: str) -> bool:
        """
        Check if this parser can handle the input.
        
        Args:
            input_text: The input text to check
            
        Returns:
            True if the input matches any known pattern
        """
        text_lower = input_text.lower()
        
        # Check if any pattern matches
        for operation, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower, re.IGNORECASE):
                    return True
        
        return False
    
    def parse(self, input_text: str) -> Optional[Dict]:
        """
        Parse natural language input into structured calculation data.
        
        Args:
            input_text: The user's question
            
        Returns:
            Dictionary with operation and operands, or None if parsing fails
            
        Example:
            >>> parser = NaturalLanguageParser()
            >>> parser.parse("What's 5 + 3?")
            {'operation': 'add', 'operands': [5.0, 3.0], 'original_text': "What's 5 + 3?"}
        """
        text_lower = input_text.lower()
        
        # Try to match each operation pattern
        for operation, patterns in self.patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text_lower, re.IGNORECASE)
                if match:
                    operands = [float(g) for g in match.groups() if g]
                    
                    # Handle special cases
                    operands = self._handle_special_cases(operation, operands)
                    
                    return {
                        'operation': operation,
                        'operands': operands,
                        'original_text': input_text
                    }
        
        # If no pattern matched, return None
        return None
    
    def _handle_special_cases(self, operation: str, operands: list) -> list:
        """
        Handle special cases for certain operations.
        
        Args:
            operation: The operation type
            operands: List of operands
            
        Returns:
            Modified operands list
        """
        # For square operation, add implicit power of 2
        if operation == 'square' and len(operands) == 1:
            return [operands[0], 2]
        
        # For cube operation, add implicit power of 3
        if operation == 'cube' and len(operands) == 1:
            return [operands[0], 3]
        
        return operands
