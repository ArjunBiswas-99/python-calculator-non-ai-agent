# Python Calculator Non-AI Agent

A professional calculator agent built with SOLID principles, demonstrating how to create intelligent agents without using AI/machine learning models.

## Table of Contents

- [What is This Project?](#what-is-this-project)
- [What is an AI Agent?](#what-is-an-ai-agent)
- [Why "Non-AI"?](#why-non-ai)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [SOLID Principles](#solid-principles)
- [Extending the Agent](#extending-the-agent)
- [Examples](#examples)
- [Learning Guide](#learning-guide)

---

## What is This Project?

This is a **scientific calculator agent** that can:
- Understand natural language questions like "What's 25 + 17?"
- Perform mathematical calculations
- Remember calculation history
- Work through both terminal and web interfaces
- Demonstrate professional software architecture patterns

It's designed as a learning tool to understand:
1. What AI agents are and how they work
2. Software design principles (SOLID)
3. How to build autonomous programs
4. Clean code architecture

---

## What is an AI Agent?

An **AI agent** is a software program that can:
1. **Perceive** its environment (receive input)
2. **Think** and make decisions (process information)
3. **Act** autonomously (take actions to achieve goals)

### Real-World Analogy
Think of a personal assistant who:
- Listens to your request (perception)
- Figures out how to help you (reasoning)
- Takes action to complete the task (action)
- Remembers what worked before (memory)

### Agent Types
1. **Simple Reflex Agents** - React to current input (like a thermostat)
2. **Goal-Based Agents** - Work towards achieving specific goals
3. **Utility-Based Agents** - Choose actions that maximize "happiness"
4. **Learning Agents** - Improve over time from experience

**This project is a goal-based agent** - it works to calculate the answer to your math question.

---

## Why "Non-AI"?

This agent doesn't use AI/machine learning models because:

1. **Easier to understand** - You can see exactly how decisions are made
2. **Predictable** - Same input always gives same output
3. **No dependencies** - No API keys or model downloads needed
4. **Faster** - Instant responses
5. **Free** - No API costs
6. **Full control** - You write every rule

The agent uses:
- Pattern matching (regular expressions)
- Rule-based logic (if/else statements)
- Algorithms (mathematical operations)
- Data structures (for memory)

This is still considered an "agent" because it acts autonomously to achieve goals!

---

## Features

### Mathematical Operations

**Basic Arithmetic:**
- Addition: "What's 5 + 3?"
- Subtraction: "10 minus 7"
- Multiplication: "6 times 4"
- Division: "Divide 20 by 5"

**Powers and Roots:**
- Power: "2 to the power of 3"
- Square: "5 squared"
- Cube: "4 cubed"
- Square root: "Square root of 144"
- Cube root: "Cube root of 27"

**Trigonometry:**
- Sine: "sin of 30 degrees"
- Cosine: "cos of 45 degrees"
- Tangent: "tan of 60 degrees"

**Logarithms:**
- Base 10: "log of 100"
- Natural: "natural log of 10"

**Factorials:**
- "5 factorial"
- "factorial of 7"

### Agent Features

- **Natural Language Processing** - Understands conversational input
- **Calculation History** - Remembers past calculations
- **Error Handling** - Gracefully handles invalid input
- **Multiple Interfaces** - Terminal and web browser
- **Special Commands** - help, history, clear

---

## Project Structure

```
python-calculator-non-ai-agent/
├── src/                           # Core agent components
│   ├── agent.py                   # Main agent orchestrator
│   ├── input_processor.py         # Input validation
│   ├── memory_manager.py          # Calculation history
│   └── formatters.py              # Output formatting
├── parsers/                       # Natural language parsing
│   ├── base_parser.py            # Abstract parser interface
│   └── natural_language_parser.py # Concrete implementation
├── calculators/                   # Calculation engines
│   ├── base_calculator.py        # Abstract calculator interface
│   └── scientific_calculator.py   # Concrete implementation
├── interfaces/                    # User interfaces
│   ├── base_interface.py         # Abstract interface
│   ├── terminal_interface.py     # Command-line interface
│   └── web_interface.py          # Web browser interface
├── run_terminal.py               # Launch terminal version
├── run_web.py                    # Launch web version
├── examples.py                   # Usage examples
├── requirements.txt              # Python dependencies
└── README.txt                    # This file
```

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd python-calculator-non-ai-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   - `sympy` - For advanced mathematical operations
   - `flask` - For the web interface

---

## Usage

### Terminal Interface (Command Line)

Run the terminal version:
```bash
python run_terminal.py
```

Then interact with the agent:
```
You: What's 25 + 17?
Agent: The answer is 42

You: Calculate square root of 144
Agent: The answer is 12

You: quit
```

### Web Interface (Browser)

1. Start the web server:
   ```bash
   python run_web.py
   ```

2. Open your browser to:
   ```
   http://localhost:5000
   ```

3. Type your questions in the web interface

### Running Examples

See various usage examples:
```bash
python examples.py
```

This demonstrates:
- Basic usage
- Working with history
- Error handling
- Custom configuration
- Programmatic access
- Special commands

---

## Architecture

### Agent Flow

```
USER INPUT
    ↓
[Input Processor] ← Validates and cleans input
    ↓
[Parser] ← Understands natural language
    ↓
[Agent] ← Decides what to do
    ↓
[Calculator] ← Performs calculation
    ↓
[Memory] ← Stores result
    ↓
[Formatter] ← Formats output
    ↓
RESPONSE TO USER
```

### Component Responsibilities

**Agent (agent.py)**
- Orchestrates the entire process
- Coordinates between components
- Handles special commands
- Main "brain" of the system

**Input Processor (input_processor.py)**
- Validates input
- Cleans whitespace
- Checks for exit commands

**Parser (natural_language_parser.py)**
- Converts text to structured data
- Extracts operations and operands
- Pattern matching with regex

**Calculator (scientific_calculator.py)**
- Performs mathematical operations
- Uses sympy for advanced math
- Error handling for edge cases

**Memory Manager (memory_manager.py)**
- Stores calculation history
- Retrieves past calculations
- Limits history size

**Formatter (formatters.py)**
- Formats results for display
- Creates user-friendly messages
- Formats errors and help text

**Interfaces (terminal_interface.py, web_interface.py)**
- Handle user interaction
- Display output
- Manage interaction loop

---

## SOLID Principles

This project demonstrates all five SOLID principles:

### 1. Single Responsibility Principle (SRP)
Each class has ONE clear purpose:
- `InputProcessor` - Only validates input
- `Parser` - Only parses natural language
- `Calculator` - Only performs calculations
- `MemoryManager` - Only manages history
- `Formatter` - Only formats output

### 2. Open/Closed Principle (OCP)
Open for extension, closed for modification:
- New parsers can be added by extending `BaseParser`
- New calculators can be added by extending `BaseCalculator`
- New interfaces can be added by extending `BaseInterface`
- Existing code doesn't need to change

### 3. Liskov Substitution Principle (LSP)
Any implementation can replace another:
- Any `BaseParser` subclass works in the agent
- Any `BaseCalculator` subclass works in the agent
- Any `BaseInterface` implementation works

### 4. Interface Segregation Principle (ISP)
Clients only depend on methods they use:
- `BaseInterface` has minimal methods (get_input, display_output, run)
- Components aren't forced to implement unused methods

### 5. Dependency Inversion Principle (DIP)
Depend on abstractions, not concretions:
- Agent depends on `BaseParser`, not specific implementations
- Agent depends on `BaseCalculator`, not specific implementations
- Easy to swap implementations for testing

---

## Extending the Agent

### Adding New Operations

1. **Add pattern to parser** (parsers/natural_language_parser.py):
   ```python
   self.patterns = {
       # ... existing patterns ...
       'percentage': [
           r'(\d+\.?\d*)\s*percent\s*of\s*(\d+\.?\d*)',
       ],
   }
   ```

2. **Add calculation method** (calculators/scientific_calculator.py):
   ```python
   def _percentage(self, operands: list) -> float:
       """Calculate percentage."""
       if len(operands) != 2:
           raise ValueError("Percentage requires 2 operands")
       return float((operands[0] / 100) * operands[1])
   ```

3. **Add operation to supported list**:
   ```python
   self.supported_operations = {
       # ... existing operations ...
       'percentage',
   }
   ```

### Creating a New Calculator Type

1. Create new file: `calculators/basic_calculator.py`
2. Extend `BaseCalculator`
3. Implement required methods
4. Use in agent:
   ```python
   calculator = BasicCalculator()  # Instead of ScientificCalculator()
   ```

### Creating a New Interface

1. Create new file: `interfaces/voice_interface.py`
2. Extend `BaseInterface`
3. Implement `get_input()`, `display_output()`, `run()`
4. Run your custom interface

---

## Examples

### Example 1: Basic Usage
```python
from src.agent import CalculatorAgent
# ... import other components ...

# Create agent
agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)

# Use agent
result = agent.process_query("What's 25 + 17?")
print(result)  # Output: The answer is 42
```

### Example 2: Custom Configuration
```python
# Create agent with small history
memory = MemoryManager(max_history=5)
agent = CalculatorAgent(parser, calculator, input_processor, memory, formatter)

# History will only keep last 5 calculations
```

### Example 3: Direct Component Access
```python
# Use parser directly
parser = NaturalLanguageParser()
parsed_data = parser.parse("What's 5 times 3?")
print(parsed_data)
# Output: {'operation': 'multiply', 'operands': [5.0, 3.0], ...}

# Use calculator directly
calculator = ScientificCalculator()
result = calculator.calculate(parsed_data)
print(result)  # Output: 15.0
```

---

## Learning Guide

### For Complete Beginners

1. **Start with examples.py**
   - Run it to see how the agent works
   - Read through the code and comments
   - Understand the basic flow

2. **Try the terminal interface**
   - Run `python run_terminal.py`
   - Ask different questions
   - Type 'help' to see what's possible

3. **Read the core agent** (src/agent.py)
   - Understand the perceive-think-act cycle
   - See how components work together

4. **Explore individual components**
   - Start with `formatters.py` (simplest)
   - Then `memory_manager.py`
   - Then `input_processor.py`
   - Finally `parser.py` and `calculator.py`

### For Intermediate Developers

1. **Study the SOLID principles**
   - See how each principle is applied
   - Understand the abstractions

2. **Try extending the agent**
   - Add a new operation
   - Create a custom formatter
   - Modify the web interface

3. **Understand the architecture patterns**
   - Dependency Injection
   - Strategy Pattern
   - Template Method Pattern

### For Advanced Developers

1. **Analyze the design decisions**
   - Why this component structure?
   - What are the tradeoffs?

2. **Consider improvements**
   - How would you add learning capabilities?
   - How would you make it distributed?
   - How would you add authentication?

3. **Build something new**
   - Create a different type of agent
   - Apply these patterns to your projects

---

## Comparison: Agent vs Non-Agent

### Traditional Calculator
```python
def calculate(expression):
    return eval(expression)

result = calculate("2 + 2")
```
- No perception of natural language
- No decision-making
- No memory
- Just a function call

### Calculator Agent
```python
agent = CalculatorAgent(...)
result = agent.process_query("What's 2 + 2?")
```
- Perceives natural language
- Decides how to interpret
- Performs action (calculation)
- Remembers in history
- Formats response

**The agent is autonomous and goal-driven!**

---

## Common Questions

### Q: Is this really an agent if it doesn't use AI?
**A:** Yes! An agent is defined by its behavior (autonomous, goal-driven), not by whether it uses AI/ML. Many production agents use rule-based logic.

### Q: When should I use AI vs non-AI agents?
**A:** Use non-AI when:
- Rules are well-defined
- Predictability is important
- You need full control
- No learning from data needed

Use AI when:
- Rules are complex or unknown
- Natural language understanding needed
- Learning from data is beneficial
- Context and ambiguity handling required

### Q: Can I combine AI and non-AI approaches?
**A:** Absolutely! This is common in production:
- Use AI for understanding complex queries
- Use rule-based logic for calculations
- Use AI for learning user preferences
- Use rules for safety checks

### Q: How do I test this agent?
**A:** Each component can be tested independently:
```python
# Test parser
parser = NaturalLanguageParser()
result = parser.parse("2 + 2")
assert result['operation'] == 'add'

# Test calculator
calculator = ScientificCalculator()
result = calculator.calculate({'operation': 'add', 'operands': [2, 2]})
assert result == 4
```

---

## Troubleshooting

### Import Errors
```
ModuleNotFoundError: No module named 'sympy'
```
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Port Already in Use (Web Interface)
```
Address already in use
```
**Solution:** Either:
1. Stop the other process using port 5000
2. Or change the port in `run_web.py`:
   ```python
   interface = WebInterface(agent, host='0.0.0.0', port=5001)
   ```

### Parser Not Understanding Input
**Solution:** Check the patterns in `natural_language_parser.py` or try:
- Use numbers instead of words: "5 + 3" instead of "five plus three"
- Be more explicit: "Calculate 5 + 3" instead of just "5 + 3"
- Type 'help' to see example formats

---

## Next Steps

### Beginner Projects
1. Add percentage calculations
2. Add more natural language patterns
3. Customize the web interface colors
4. Add calculation timestamps

### Intermediate Projects
1. Create a basic calculator (only +, -, *, /)
2. Add equation solving (e.g., "solve x + 5 = 10")
3. Create a voice interface
4. Add unit conversions

### Advanced Projects
1. Add a learning component (tracks user preferences)
2. Create a mobile app interface
3. Add multi-step problem solving
4. Integrate with an AI model for better NLP

---

## Resources

### Learning About Agents
- "Artificial Intelligence: A Modern Approach" by Russell & Norvig
- "Clean Architecture" by Robert C. Martin
- "Design Patterns" by Gang of Four

### Python Resources
- Python official docs: https://docs.python.org/
- Real Python tutorials: https://realpython.com/
- Sympy documentation: https://docs.sympy.org/

### Software Architecture
- SOLID principles: https://en.wikipedia.org/wiki/SOLID
- Dependency Injection: https://en.wikipedia.org/wiki/Dependency_injection
- Design Patterns: https://refactoring.guru/design-patterns

---

## Contributing

Feel free to:
- Add new operations
- Improve the parser
- Create new interfaces
- Fix bugs
- Improve documentation

---

## License

This is an educational project. Feel free to use, modify, and learn from it!

---

## Summary

This project teaches you:
1. ✅ What AI agents are
2. ✅ How agents work (perceive-think-act)
3. ✅ SOLID principles in practice
4. ✅ Clean code architecture
5. ✅ How to build without AI/ML
6. ✅ Professional software design

You now understand that "AI agent" doesn't always mean machine learning - it means autonomous, goal-driven software that can perceive, think, and act!

---

**Happy Learning! 🎓**

For questions or issues, review the code comments - they're designed to teach!
