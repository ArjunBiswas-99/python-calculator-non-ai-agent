#!/usr/bin/env python3
"""
Web Interface Launcher

This script creates and runs the calculator agent with a web interface.
Run this file to start the browser-based version of the calculator.

Usage:
    python run_web.py
    
Then open your browser to: http://localhost:5000
"""

# Import all necessary components
from src.agent import CalculatorAgent
from src.input_processor import InputProcessor
from src.memory_manager import MemoryManager
from src.formatters import OutputFormatter
from parsers.natural_language_parser import NaturalLanguageParser
from calculators.scientific_calculator import ScientificCalculator
from interfaces.web_interface import WebInterface


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
    Main function to run the web interface.
    
    This demonstrates the complete agent lifecycle:
    1. Create agent with all dependencies
    2. Create interface with agent
    3. Run interface (starts the web server)
    """
    # Create the agent
    agent = create_agent()
    
    # Create web interface with agent
    # Host: 0.0.0.0 allows access from other devices on the network
    # Port: 5000 is the default Flask port
    interface = WebInterface(agent, host='0.0.0.0', port=5000)
    
    # Run the interface (starts the Flask server)
    interface.run()


if __name__ == '__main__':
    """
    Entry point when script is run directly.
    
    This allows the script to be run as:
        python run_web.py
    
    Or made executable and run as:
        ./run_web.py
    """
    main()
