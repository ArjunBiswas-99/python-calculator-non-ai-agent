"""
Parsers Package

This package contains parser implementations following the Open/Closed principle.
New parsers can be added without modifying existing code.
"""

from .base_parser import BaseParser
from .natural_language_parser import NaturalLanguageParser

__all__ = ['BaseParser', 'NaturalLanguageParser']
