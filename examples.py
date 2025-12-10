#!/usr/bin/env python3
"""
Examples and Usage Guide

This file demonstrates how to use the calculator agent programmatically.
It shows various ways to interact with the agent and customize its behavior.
"""

from src.agent import CalculatorAgent
from src.input_processor import InputProcessor
from src.memory_manager import MemoryManager
from src.formatters import OutputFormatter
from parsers.natural_language_parser import NaturalLanguageParser
from calculators.scientific_calculator import ScientificCalculator


def example_1_basic_usage():
    """
    Example 1: Basic usage of the calculator agent.
    
    This shows the simplest way to create and use the agent.
    """
    print("="*60)
    print("EXAMPLE 1: Basic Usage")
    print("="*60)
    
    # Create components
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    input_processor = InputProcessor()
    memory = MemoryManager()
    formatter = OutputFormatter()
    
    # Create agent
    agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)
    
    # Process queries
    queries = [
        "What's 25 + 17?",
        "Calculate square root of 144",
        "What's 5 squared?",
        "sin of 30 degrees"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        result = agent.process_query(query)
        print(f"Result: {result}")
    
    print("\n")


def example_2_with_history():
    """
    Example 2: Using the agent with calculation history.
    
    This demonstrates how to access and display calculation history.
    """
    print("="*60)
    print("EXAMPLE 2: Working with History")
    print("="*60)
    
    # Create agent (same as example 1)
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    input_processor = InputProcessor()
    memory = MemoryManager(max_history=50)
    formatter = OutputFormatter()
    
    agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)
    
    # Perform several calculations
    calculations = [
        "2 + 2",
        "10 * 5",
        "square root of 100",
        "3 factorial"
    ]
    
    print("\nPerforming calculations...")
    for calc in calculations:
        result = agent.process_query(calc)
        print(f"{calc} = {result}")
    
    # Display history
    print("\n" + "="*60)
    print("Calculation History:")
    print("="*60)
    history = agent.get_history(limit=10)
    print(history)


def example_3_error_handling():
    """
    Example 3: Error handling in the agent.
    
    This shows how the agent handles various error conditions.
    """
    print("="*60)
    print("EXAMPLE 3: Error Handling")
    print("="*60)
    
    # Create agent
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    input_processor = InputProcessor()
    memory = MemoryManager()
    formatter = OutputFormatter()
    
    agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)
    
    # Test various error cases
    error_cases = [
        ("Division by zero", "10 / 0"),
        ("Invalid input", "hello world"),
        ("Unsupported operation", "something random"),
    ]
    
    for case_name, query in error_cases:
        print(f"\nTest: {case_name}")
        print(f"Query: {query}")
        result = agent.process_query(query)
        print(f"Result: {result}")
    
    print("\n")


def example_4_custom_configuration():
    """
    Example 4: Custom agent configuration.
    
    This demonstrates how to customize the agent's behavior
    by creating custom components or using different settings.
    """
    print("="*60)
    print("EXAMPLE 4: Custom Configuration")
    print("="*60)
    
    # Create agent with custom memory size
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    input_processor = InputProcessor()
    memory = MemoryManager(max_history=5)  # Only keep last 5 calculations
    formatter = OutputFormatter()
    
    agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)
    
    print("\nAgent configured with max_history=5")
    print("Performing 7 calculations...")
    
    # Perform more calculations than history limit
    for i in range(1, 8):
        query = f"{i} + {i}"
        agent.process_query(query)
    
    # Check history
    history_data = agent.memory.get_history()
    print(f"\nHistory contains {len(history_data)} items (should be 5)")
    print("\nStored calculations:")
    for item in history_data:
        print(f"  {item['query']} = {item['result']}")
    
    print("\n")


def example_5_programmatic_access():
    """
    Example 5: Programmatic access to agent components.
    
    This shows how to directly access and use individual components
    without going through the full agent pipeline.
    """
    print("="*60)
    print("EXAMPLE 5: Programmatic Component Access")
    print("="*60)
    
    # Create individual components
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    
    # Test parser directly
    print("\nDirect Parser Usage:")
    test_input = "What's 7 times 8?"
    parsed = parser.parse(test_input)
    print(f"Input: {test_input}")
    print(f"Parsed: {parsed}")
    
    # Test calculator directly
    print("\nDirect Calculator Usage:")
    calculation_data = {
        'operation': 'multiply',
        'operands': [7, 8]
    }
    result = calculator.calculate(calculation_data)
    print(f"Calculation: {calculation_data}")
    print(f"Result: {result}")
    
    print("\n")


def example_6_special_commands():
    """
    Example 6: Using special commands.
    
    This demonstrates the agent's built-in commands like 'help' and 'history'.
    """
    print("="*60)
    print("EXAMPLE 6: Special Commands")
    print("="*60)
    
    # Create agent
    parser = NaturalLanguageParser()
    calculator = ScientificCalculator()
    input_processor = InputProcessor()
    memory = MemoryManager()
    formatter = OutputFormatter()
    
    agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)
    
    # Perform some calculations first
    agent.process_query("5 + 5")
    agent.process_query("10 * 2")
    
    # Test help command
    print("\nCommand: help")
    print("-" * 60)
    help_text = agent.process_query("help")
    print(help_text)
    
    # Test history command
    print("\nCommand: history")
    print("-" * 60)
    history_text = agent.process_query("history")
    print(history_text)
    
    print("\n")


def main():
    """
    Run all examples.
    
    This demonstrates various ways to use the calculator agent.
    """
    print("\n" + "="*60)
    print("CALCULATOR AGENT - USAGE EXAMPLES")
    print("="*60 + "\n")
    
    # Run all examples
    example_1_basic_usage()
    example_2_with_history()
    example_3_error_handling()
    example_4_custom_configuration()
    example_5_programmatic_access()
    example_6_special_commands()
    
    print("="*60)
    print("All examples completed!")
    print("="*60)
    print("\nTo run the interactive versions:")
    print("  Terminal: python run_terminal.py")
    print("  Web:      python run_web.py")
    print("\n")


if __name__ == '__main__':
    """
    Entry point when script is run directly.
    
    Run this file to see all usage examples:
        python examples.py
    """
    main()
