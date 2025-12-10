"""
Base Calculator Module

Defines the abstract interface for all calculators (Open/Closed Principle).
New calculator types can be added by extending this base class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseCalculator(ABC):
    """
    Abstract base class for all calculators.
    
    This follows the Open/Closed Principle:
    - Open for extension: Create new calculator types by subclassing
    - Closed for modification: Existing calculators don't need changes
    
    This also follows the Liskov Substitution Principle:
    - Any BaseCalculator subclass can be used interchangeably
    """
    
    @abstractmethod
    def calculate(self, parsed_data: Dict) -> Any:
        """
        Perform the calculation based on parsed data.
        
        Args:
            parsed_data: Dictionary containing:
                - 'operation': The operation to perform (e.g., 'add', 'sqrt')
                - 'operands': List of operands
                - 'original_text': The original user query
                
        Returns:
            The calculation result (usually a number)
            
        Raises:
            ValueError: If the operation is not supported
            ZeroDivisionError: If division by zero is attempted
            
        Example:
            >>> calc = ScientificCalculator()
            >>> result = calc.calculate({
            ...     'operation': 'add',
            ...     'operands': [2, 3]
            ... })
            >>> print(result)
            5
        
        This method must be implemented by all subclasses.
        """
        pass
    
    @abstractmethod
    def supports_operation(self, operation: str) -> bool:
        """
        Check if this calculator supports the given operation.
        
        Args:
            operation: The operation name (e.g., 'add', 'sqrt')
            
        Returns:
            True if the operation is supported, False otherwise
            
        This allows for calculator selection based on capabilities.
        """
        pass
