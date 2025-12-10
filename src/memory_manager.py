"""
Memory Manager Module

Single Responsibility: Manage calculation history and memory operations.
This module only handles storing and retrieving history, not processing or calculating.
"""

from typing import List, Dict, Optional
from datetime import datetime


class MemoryManager:
    """
    Manages the agent's memory of past calculations.
    
    Responsibilities:
    - Store calculation history
    - Retrieve past calculations
    - Clear history
    - Limit history size
    
    Does NOT:
    - Parse input
    - Perform calculations
    - Format output
    """
    
    def __init__(self, max_history: int = 100):
        """
        Initialize the memory manager.
        
        Args:
            max_history: Maximum number of calculations to store (default: 100)
        """
        self._history: List[Dict] = []
        self._max_history = max_history
    
    def add(self, query: str, result: str, operation_type: str = "calculation") -> None:
        """
        Add a calculation to history.
        
        Args:
            query: The user's original query
            result: The calculation result
            operation_type: Type of operation performed
            
        Example:
            >>> memory = MemoryManager()
            >>> memory.add("What's 2 + 2?", "4", "addition")
        """
        entry = {
            'query': query,
            'result': result,
            'operation_type': operation_type,
            'timestamp': datetime.now().isoformat()
        }
        
        self._history.append(entry)
        
        # Enforce maximum history size
        if len(self._history) > self._max_history:
            self._history.pop(0)  # Remove oldest entry
    
    def get_history(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Retrieve calculation history.
        
        Args:
            limit: Maximum number of recent entries to return (None for all)
            
        Returns:
            List of calculation entries (most recent first)
            
        Example:
            >>> memory = MemoryManager()
            >>> memory.add("2 + 2", "4")
            >>> history = memory.get_history(limit=5)
        """
        if limit is None:
            return list(reversed(self._history))
        
        return list(reversed(self._history[-limit:]))
    
    def get_last(self) -> Optional[Dict]:
        """
        Get the most recent calculation.
        
        Returns:
            Most recent calculation entry, or None if history is empty
            
        Example:
            >>> memory = MemoryManager()
            >>> memory.add("2 + 2", "4")
            >>> last = memory.get_last()
            >>> print(last['result'])
            "4"
        """
        if not self._history:
            return None
        
        return self._history[-1]
    
    def clear(self) -> None:
        """
        Clear all calculation history.
        
        Example:
            >>> memory = MemoryManager()
            >>> memory.add("2 + 2", "4")
            >>> memory.clear()
            >>> len(memory.get_history())
            0
        """
        self._history.clear()
    
    def count(self) -> int:
        """
        Get the number of calculations in history.
        
        Returns:
            Number of stored calculations
            
        Example:
            >>> memory = MemoryManager()
            >>> memory.add("2 + 2", "4")
            >>> memory.count()
            1
        """
        return len(self._history)
    
    def search(self, keyword: str) -> List[Dict]:
        """
        Search history for calculations containing a keyword.
        
        Args:
            keyword: Search term (case-insensitive)
            
        Returns:
            List of matching calculations
            
        Example:
            >>> memory = MemoryManager()
            >>> memory.add("What's the square root of 144?", "12")
            >>> results = memory.search("square root")
        """
        keyword_lower = keyword.lower()
        matches = []
        
        for entry in self._history:
            if (keyword_lower in entry['query'].lower() or 
                keyword_lower in entry['result'].lower()):
                matches.append(entry)
        
        return matches
