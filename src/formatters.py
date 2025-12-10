"""
Output Formatter Module

Single Responsibility: Format calculation results for display to users.
This module only handles formatting output, not calculations or parsing.
"""

from typing import Any, Dict, List


class OutputFormatter:
    """
    Formats calculation results and messages for user-friendly display.
    
    Responsibilities:
    - Format numeric results
    - Create user-friendly messages
    - Format error messages
    - Format history displays
    
    Does NOT:
    - Parse input
    - Perform calculations
    - Store history
    """
    
    def __init__(self):
        """Initialize the output formatter."""
        pass
    
    def format_result(self, result: Any, query: str = "") -> str:
        """
        Format a calculation result for display.
        
        Args:
            result: The calculation result (number or string)
            query: The original query (optional, for context)
            
        Returns:
            Formatted result string
            
        Example:
            >>> formatter = OutputFormatter()
            >>> formatter.format_result(42, "What's 2 + 2?")
            "The answer is 42"
        """
        if result is None:
            return "I couldn't calculate that. Please try again."
        
        # Format numeric results
        if isinstance(result, (int, float)):
            result = self._format_number(result)
        
        return f"The answer is {result}"
    
    def format_error(self, error_message: str) -> str:
        """
        Format an error message for display.
        
        Args:
            error_message: The error message
            
        Returns:
            Formatted error message
            
        Example:
            >>> formatter = OutputFormatter()
            >>> formatter.format_error("Division by zero")
            "Error: Division by zero"
        """
        return f"Error: {error_message}"
    
    def format_welcome(self) -> str:
        """
        Format a welcome message.
        
        Returns:
            Welcome message string
        """
        return """
╔════════════════════════════════════════════════════════════╗
║          Welcome to Calculator Agent!                      ║
║                                                            ║
║  I can help you with mathematical calculations.            ║
║  Just ask me naturally, like:                              ║
║    • "What's 25 + 17?"                                     ║
║    • "Calculate square root of 144"                        ║
║    • "What's 5 squared?"                                   ║
║    • "sin of 30 degrees"                                   ║
║                                                            ║
║  Type 'help' for more examples                             ║
║  Type 'history' to see past calculations                   ║
║  Type 'quit' to exit                                       ║
╚════════════════════════════════════════════════════════════╝
"""
    
    def format_help(self) -> str:
        """
        Format a help message with examples.
        
        Returns:
            Help message string
        """
        return """
Available Operations:
─────────────────────

Basic Arithmetic:
  • Addition: "What's 5 + 3?", "Add 10 and 20"
  • Subtraction: "10 minus 3", "What's 15 - 7?"
  • Multiplication: "5 times 4", "Multiply 6 and 7"
  • Division: "Divide 20 by 5", "What's 100 / 4?"

Powers and Roots:
  • Power: "2 to the power of 3", "5 squared", "4 cubed"
  • Square root: "Square root of 81", "sqrt(144)"
  • Nth root: "Cube root of 27"

Trigonometry:
  • "sin of 30 degrees", "cos(45)", "tan of 60"
  • Note: Input angles in degrees

Logarithms:
  • "log of 100", "natural log of 10", "ln(5)"

Factorials:
  • "5 factorial", "factorial of 7"

Special Commands:
  • 'history' - Show calculation history
  • 'clear' - Clear calculation history
  • 'help' - Show this help message
  • 'quit' - Exit the program
"""
    
    def format_history(self, history: List[Dict]) -> str:
        """
        Format calculation history for display.
        
        Args:
            history: List of calculation entries
            
        Returns:
            Formatted history string
            
        Example:
            >>> formatter = OutputFormatter()
            >>> history = [{'query': '2+2', 'result': '4'}]
            >>> print(formatter.format_history(history))
        """
        if not history:
            return "No calculation history yet."
        
        output = "\nCalculation History:\n"
        output += "─" * 60 + "\n"
        
        for i, entry in enumerate(history, 1):
            query = entry.get('query', 'Unknown')
            result = entry.get('result', 'N/A')
            output += f"{i}. {query} = {result}\n"
        
        return output
    
    def format_goodbye(self) -> str:
        """
        Format a goodbye message.
        
        Returns:
            Goodbye message string
        """
        return "\nThank you for using Calculator Agent! Goodbye! 👋\n"
    
    def _format_number(self, number: float) -> str:
        """
        Format a number for display (remove unnecessary decimals).
        
        Args:
            number: Number to format
            
        Returns:
            Formatted number string
            
        Example:
            >>> formatter = OutputFormatter()
            >>> formatter._format_number(4.0)
            "4"
            >>> formatter._format_number(3.14159)
            "3.14159"
        """
        # If it's a whole number, display without decimals
        if isinstance(number, float) and number.is_integer():
            return str(int(number))
        
        # Otherwise, format with reasonable precision
        return str(round(number, 6)).rstrip('0').rstrip('.')
    
    def format_parsing_error(self) -> str:
        """
        Format a message when input cannot be parsed.
        
        Returns:
            Error message string
        """
        return """
I couldn't understand that question. Please try again.

Examples of questions I can answer:
  • "What's 2 + 2?"
  • "Calculate square root of 144"
  • "What's 5 squared?"

Type 'help' for more examples.
"""
