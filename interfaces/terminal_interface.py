"""
Terminal Interface Module

Concrete implementation of BaseInterface for command-line interaction.
This is the simplest interface - perfect for learning and testing.
"""

from .base_interface import BaseInterface
from src.agent import CalculatorAgent


class TerminalInterface(BaseInterface):
    """
    Command-line interface for the calculator agent.
    
    Features:
    - Simple text-based interaction
    - Input/output in terminal
    - Colored output (optional, for better UX)
    - Command history accessible
    
    This is a concrete implementation of BaseInterface, demonstrating
    the Interface Segregation principle in action.
    """
    
    def __init__(self, agent: CalculatorAgent):
        """
        Initialize the terminal interface.
        
        Args:
            agent: The CalculatorAgent instance to use
        """
        self.agent = agent
        self.running = False
    
    def get_input(self) -> str:
        """
        Get input from the terminal.
        
        Returns:
            User input string
        """
        try:
            return input("You: ")
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+D or Ctrl+C gracefully
            return "quit"
    
    def display_output(self, message: str) -> None:
        """
        Display output to the terminal.
        
        Args:
            message: Message to display
        """
        print(f"Agent: {message}")
        print()  # Add blank line for readability
    
    def run(self) -> None:
        """
        Run the terminal interface main loop.
        
        This is the main interaction loop:
        1. Shows welcome message
        2. Gets user input
        3. Processes through agent
        4. Displays response
        5. Repeats until user quits
        """
        self.running = True
        
        # Display welcome message
        print(self.agent.get_welcome_message())
        
        # Main interaction loop
        while self.running:
            try:
                # Get user input
                user_input = self.get_input()
                
                # Check for exit command
                if self.agent.input_processor.is_exit_command(user_input):
                    self.display_output(self.agent.get_goodbye_message())
                    self.running = False
                    break
                
                # Process the query through the agent
                response = self.agent.process_query(user_input)
                
                # Display the response
                self.display_output(response)
                
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\n")
                self.display_output(self.agent.get_goodbye_message())
                self.running = False
                break
            
            except Exception as e:
                # Handle unexpected errors
                self.display_output(f"Error: {str(e)}")
    
    def stop(self) -> None:
        """
        Stop the terminal interface.
        
        This can be called to gracefully stop the interface.
        """
        self.running = False
