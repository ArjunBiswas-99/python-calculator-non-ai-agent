"""
Base Parser Module

Defines the abstract interface for all parsers (Open/Closed Principle).
New parser types can be added by extending this base class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseParser(ABC):
    """
    Abstract base class for all parsers.
    
    This follows the Open/Closed Principle:
    - Open for extension: Create new parser types by subclassing
    - Closed for modification: Existing parsers don't need changes
    
    This also follows the Liskov Substitution Principle:
    - Any BaseParser subclass can be used interchangeably
    """
    
    @abstractmethod
    def parse(self, input_text: str) -> Optional[Dict]:
        """
        Parse input text and extract mathematical operation.
        
        Args:
            input_text: The cleaned input text from user
            
        Returns:
            Dictionary with 'operation' and 'operands' keys, or None if parsing fails
            
        Example return format:
            {
                'operation': 'add',
                'operands': [2, 3],
                'original_text': 'What is 2 + 3?'
            }
        
        This method must be implemented by all subclasses.
        """
        pass
    
    @abstractmethod
    def can_handle(self, input_text: str) -> bool:
        """
        Check if this parser can handle the given input.
        
        Args:
            input_text: The input text to check
            
        Returns:
            True if this parser can handle the input, False otherwise
            
        This allows for parser chaining - try different parsers
        until one can handle the input.
        """
        pass
    
    def _extract_numbers(self, text: str) -> list:
        """
        Helper method to extract numbers from text.
        
        Args:
            text: Text containing numbers
            
        Returns:
            List of numbers found in text
            
        Example:
            >>> parser._extract_numbers("add 5 and 10")
            [5.0, 10.0]
        """
        import re
        # Match integers and decimals (including negative)
        pattern = r'-?\d+\.?\d*'
        matches = re.findall(pattern, text)
        return [float(num) for num in matches]
