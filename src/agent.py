"""
Calculator Agent Module

This is the main agent orchestrator that coordinates all components.
It follows the Dependency Inversion Principle by depending on abstractions.
"""

from typing import Optional
from parsers.base_parser import BaseParser
from calculators.base_calculator import BaseCalculator
from .input_processor import InputProcessor
from .memory_manager import MemoryManager
from .formatters import OutputFormatter


class CalculatorAgent:
    """
    Main calculator agent that orchestrates the calculation process.
    
    This is the core of the agent system. It follows SOLID principles:
    
    - Single Responsibility: Only orchestrates, doesn't do parsing/calculation
    - Open/Closed: Can work with any parser/calculator implementation
    - Liskov Substitution: Accepts any BaseParser/BaseCalculator subclass
    - Interface Segregation: Uses clean, minimal interfaces
    - Dependency Inversion: Depends on abstractions, not concretions
    
    Flow:
    1. PERCEIVE: Receives input from user
    2. PROCESS: Cleans and validates input
    3. PARSE: Understands what the user wants
    4. CALCULATE: Performs the calculation
    5. REMEMBER: Stores the result in memory
    6. RESPOND: Returns formatted result
    """
    
    def __init__(
        self,
        parser: BaseParser,
        calculator: BaseCalculator,
        input_processor: InputProcessor,
        memory: MemoryManager,
        formatter: OutputFormatter
    ):
        """
        Initialize the agent with its dependencies.
        
        Args:
            parser: Parser to understand user input (abstraction)
            calculator: Calculator to perform operations (abstraction)
            input_processor: Processor for input validation
            memory: Memory manager for history
            formatter: Formatter for output
            
        This is Dependency Injection - components are passed in,
        not created here. This makes the agent flexible and testable.
        """
        self.parser = parser
        self.calculator = calculator
        self.input_processor = input_processor
        self.memory = memory
        self.formatter = formatter
    
    def process_query(self, user_input: str) -> str:
        """
        Process a user query and return the result.
        
        This is the main method that demonstrates the agent's
        "perceive -> think -> act" cycle.
        
        Args:
            user_input: Raw input from the user
            
        Returns:
            Formatted response string
            
        Example:
            >>> agent = CalculatorAgent(...)
            >>> response = agent.process_query("What's 2 + 2?")
            >>> print(response)
            "The answer is 4"
        """
        # STEP 1: PERCEIVE - Process the input
        processed_input = self.input_processor.process(user_input)
        
        if not processed_input:
            return self.formatter.format_error("Invalid input")
        
        # Check for special commands
        if processed_input.lower() == 'help':
            return self.formatter.format_help()
        
        if processed_input.lower() == 'history':
            history = self.memory.get_history(limit=10)
            return self.formatter.format_history(history)
        
        if processed_input.lower() == 'clear':
            self.memory.clear()
            return "History cleared!"
        
        # STEP 2: PARSE - Understand what the user wants
        try:
            parsed_data = self.parser.parse(processed_input)
            
            if not parsed_data:
                return self.formatter.format_parsing_error()
            
        except Exception as e:
            return self.formatter.format_error(f"Parsing error: {str(e)}")
        
        # STEP 3: CALCULATE - Perform the calculation
        try:
            result = self.calculator.calculate(parsed_data)
            
        except ZeroDivisionError:
            return self.formatter.format_error("Cannot divide by zero")
        
        except ValueError as e:
            return self.formatter.format_error(str(e))
        
        except Exception as e:
            return self.formatter.format_error(f"Calculation error: {str(e)}")
        
        # STEP 4: REMEMBER - Store in memory
        operation_type = parsed_data.get('operation', 'unknown')
        self.memory.add(
            query=user_input,
            result=str(result),
            operation_type=operation_type
        )
        
        # STEP 5: RESPOND - Format and return the result
        return self.formatter.format_result(result, user_input)
    
    def get_welcome_message(self) -> str:
        """
        Get the welcome message for the agent.
        
        Returns:
            Formatted welcome message
        """
        return self.formatter.format_welcome()
    
    def get_goodbye_message(self) -> str:
        """
        Get the goodbye message for the agent.
        
        Returns:
            Formatted goodbye message
        """
        return self.formatter.format_goodbye()
    
    def get_history(self, limit: Optional[int] = None) -> str:
        """
        Get formatted calculation history.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            Formatted history string
        """
        history = self.memory.get_history(limit)
        return self.formatter.format_history(history)
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.memory.clear()
