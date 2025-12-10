#!/usr/bin/env python3
"""
Terminal Interface Launcher

This script creates and runs the calculator agent with a terminal interface.
Run this file to start the command-line version of the calculator.

Usage:
    python run_terminal.py
"""

# Import all necessary components
from src.agent import CalculatorAgent
from src.input_processor import InputProcessor
from src.memory_manager import MemoryManager
from src.formatters import OutputFormatter
from parsers.natural_language_parser import NaturalLanguageParser
from calculators.scientific_calculator import ScientificCalculator
from interfaces.terminal_interface import TerminalInterface


def create_agent() -> CalculatorAgent:
    """
    Create and configure the calculator agent.
    
    This function demonstrates Dependency Injection:
    - All dependencies are created and injected
    - Agent depends on abstractions, not concrete implementations
    - Easy to swap components for testing or different configurations
    
    Returns:
        Configured CalculatorAgent instance
    """
    # Create individual components
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    input_processor = InputProcessor()
    memory = MemoryManager(max_history=100)
    formatter = OutputFormatter()
    
    # Inject dependencies into agent
    agent = CalculatorAgent(
        parser=parser,
        calculator=calculator,
        input_processor=input_processor,
        memory=memory,
        formatter=formatter
    )
    
    return agent


def main():
    """
    Main function to run the terminal interface.
    
    This demonstrates the complete agent lifecycle:
    1. Create agent with all dependencies
    2. Create interface with agent
    3. Run interface (starts the interaction loop)
    """
    # Create the agent
    agent = create_agent()
    
    # Create terminal interface with agent
    interface = TerminalInterface(agent)
    
    # Run the interface (starts the main loop)
    interface.run()


if __name__ == '__main__':
    """
    Entry point when script is run directly.
    
    This allows the script to be run as:
        python run_terminal.py
    
    Or made executable and run as:
        ./run_terminal.py
    """
    main()
