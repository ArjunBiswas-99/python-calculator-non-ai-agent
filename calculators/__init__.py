"""
Calculators Package

This package contains calculator implementations following the Open/Closed principle.
New calculator types can be added without modifying existing code.
"""

from .base_calculator import BaseCalculator
from .scientific_calculator import ScientificCalculator

__all__ = ['BaseCalculator', 'ScientificCalculator']
