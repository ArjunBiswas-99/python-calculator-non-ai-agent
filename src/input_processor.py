"""
Input Processor Module

Single Responsibility: Validate and pre-process user input before parsing.
This module only handles cleaning and validating input, not parsing meaning.
"""

import re
from typing import Optional


class InputProcessor:
    """
    Processes and validates user input before it's sent to the parser.
    
    Responsibilities:
    - Remove extra whitespace
    - Validate input is not empty
    - Basic sanitization
    
    Does NOT:
    - Parse the meaning of input (that's the Parser's job)
    - Perform calculations (that's the Calculator's job)
    """
    
    def __init__(self):
        """Initialize the input processor."""
        pass
    
    def process(self, raw_input: str) -> Optional[str]:
        """
        Process raw user input and return cleaned version.
        
        Args:
            raw_input: The raw string from user
            
        Returns:
            Cleaned string if valid, None if invalid
            
        Example:
            >>> processor = InputProcessor()
            >>> processor.process("  What's 2 + 2?  ")
            "What's 2 + 2?"
        """
        if not raw_input or not isinstance(raw_input, str):
            return None
        
        # Clean the input
        cleaned = self._clean(raw_input)
        
        # Validate
        if not self._validate(cleaned):
            return None
        
        return cleaned
    
    def _clean(self, text: str) -> str:
        """
        Clean the input text by removing extra whitespace.
        
        Args:
            text: Input text to clean
            
        Returns:
            Cleaned text
        """
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        
        return text
    
    def _validate(self, text: str) -> bool:
        """
        Validate that the cleaned input is usable.
        
        Args:
            text: Cleaned text to validate
            
        Returns:
            True if valid, False otherwise
        """
        # Check if empty
        if not text:
            return False
        
        # Check minimum length (at least 1 character)
        if len(text) < 1:
            return False
        
        return True
    
    def is_exit_command(self, text: str) -> bool:
        """
        Check if the input is an exit command.
        
        Args:
            text: Input text to check
            
        Returns:
            True if it's an exit command, False otherwise
        """
        exit_commands = ['quit', 'exit', 'bye', 'goodbye']
        return text.lower().strip() in exit_commands
