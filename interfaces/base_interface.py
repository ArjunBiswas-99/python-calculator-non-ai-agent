"""
Base Interface Module

Defines the abstract interface for all user interfaces (Interface Segregation Principle).
New interface types can be added by extending this base class.
"""

from abc import ABC, abstractmethod


class BaseInterface(ABC):
    """
    Abstract base class for all user interfaces.
    
    This follows the Interface Segregation Principle:
    - Clients only depend on methods they actually use
    - Minimal, clean interface contract
    
    Any interface (terminal, web, GUI, voice, etc.) must implement these methods.
    """
    
    @abstractmethod
    def get_input(self) -> str:
        """
        Get input from the user.
        
        Returns:
            User input as a string
            
        Implementation varies by interface:
        - Terminal: Uses input()
        - Web: Gets from HTTP request
        - GUI: Gets from text field
        - Voice: Uses speech recognition
        """
        pass
    
    @abstractmethod
    def display_output(self, message: str) -> None:
        """
        Display output to the user.
        
        Args:
            message: The message to display
            
        Implementation varies by interface:
        - Terminal: Uses print()
        - Web: Returns HTTP response
        - GUI: Updates UI element
        - Voice: Uses text-to-speech
        """
        pass
    
    @abstractmethod
    def run(self) -> None:
        """
        Start the interface and handle the main loop.
        
        This method contains the main interaction loop for the interface.
        It typically:
        1. Shows welcome message
        2. Gets input from user
        3. Processes input through agent
        4. Displays output
        5. Repeats until exit
        """
        pass
