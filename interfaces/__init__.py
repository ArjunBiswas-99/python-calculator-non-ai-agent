"""
Interfaces Package

This package contains user interface implementations following the Interface Segregation principle.
Different UI types can be added without modifying existing code.
"""

from .base_interface import BaseInterface
from .terminal_interface import TerminalInterface
from .web_interface import WebInterface

__all__ = ['BaseInterface', 'TerminalInterface', 'WebInterface']
