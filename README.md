# Python Calculator Non-AI Agent

A scientific calculator agent built with Python that understands natural language queries and performs mathematical calculations without using AI/machine learning models.

---

## Installation 

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Navigate to the project directory:
   ```bash
   cd python-calculator-non-ai-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Terminal Interface (Command Line)

Run the terminal version:
```bash
python3 run_terminal.py
```

Then interact with the agent:
```
You: What's 25 + 17?
Agent: The answer is 42

You: Calculate square root of 144
Agent: The answer is 12

You: quit
```

<img width="671" height="451" alt="image" src="https://github.com/user-attachments/assets/962bdf8c-481a-4d6f-af4a-839a0569e84a" />


### Web Interface (Browser)

1. Start the web server:
   ```bash
   python3 run_web.py
   ```

2. Open your browser to:
   ```
   http://localhost:5000
   ```

3. Type your questions in the web interface

### Running Examples

See various usage examples:
```bash
python3 examples.py
```

---

<img width="1775" height="963" alt="image" src="https://github.com/user-attachments/assets/ff80fecb-82ee-4013-afec-ecf8f29c8938" />


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

- Natural language understanding
- Calculation history with memory
- Error handling
- Multiple interfaces (terminal + web)
- Special commands: help, history, clear

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

### SOLID Principles

This project demonstrates all five SOLID principles:

**1. Single Responsibility Principle (SRP)**
- Each class has ONE clear purpose
- `InputProcessor` - Only validates input
- `Parser` - Only parses natural language
- `Calculator` - Only performs calculations
- `MemoryManager` - Only manages history
- `Formatter` - Only formats output

**2. Open/Closed Principle (OCP)**
- Open for extension, closed for modification
- New parsers can be added by extending `BaseParser`
- New calculators can be added by extending `BaseCalculator`
- New interfaces can be added by extending `BaseInterface`

**3. Liskov Substitution Principle (LSP)**
- Any implementation can replace another
- Any `BaseParser` subclass works in the agent
- Any `BaseCalculator` subclass works in the agent

**4. Interface Segregation Principle (ISP)**
- Clients only depend on methods they use
- `BaseInterface` has minimal methods
- Components aren't forced to implement unused methods

**5. Dependency Inversion Principle (DIP)**
- Depend on abstractions, not concretions
- Agent depends on `BaseParser`, not specific implementations
- Agent depends on `BaseCalculator`, not specific implementations

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
**Solution:** Try:
- Use numbers instead of words: "5 + 3" instead of "five plus three"
- Be more explicit: "Calculate 5 + 3" instead of just "5 + 3"
- Type 'help' to see example formats

---

## Learning Guide

### For Beginners

1. **Start with examples.py**
   - Run it to see how the agent works
   - Read through the code and comments

2. **Try the terminal interface**
   - Run `python3 run_terminal.py`
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

## License

This is an educational project. Feel free to use, modify, and learn from it!

---

**Happy Learning! 🎓**
