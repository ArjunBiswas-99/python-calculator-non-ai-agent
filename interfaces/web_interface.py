"""
Web Interface Module

Concrete implementation of BaseInterface for web browser interaction.
Uses Flask to create a REST API and serve a simple HTML interface.
"""

from flask import Flask, request, jsonify, render_template_string
from .base_interface import BaseInterface
from src.agent import CalculatorAgent


class WebInterface(BaseInterface):
    """
    Web-based interface for the calculator agent.
    
    Features:
    - Browser-based UI
    - RESTful API
    - JSON responses
    - Simple HTML/CSS/JavaScript frontend
    - Real-time calculations
    
    This is a concrete implementation of BaseInterface, demonstrating
    the Interface Segregation principle in action.
    """
    
    # HTML template for the web interface
    HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator Agent</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
        }
        
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 0.9em;
        }
        
        .input-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
        }
        
        input[type="text"] {
            width: 100%;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }
        
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        
        button:active {
            transform: translateY(0);
        }
        
        .result {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            display: none;
        }
        
        .result.show {
            display: block;
            animation: slideIn 0.3s ease;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .result-label {
            color: #667eea;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        .result-text {
            color: #333;
            font-size: 1.2em;
        }
        
        .history {
            margin-top: 30px;
        }
        
        .history-title {
            color: #333;
            font-weight: 600;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .clear-btn {
            background: #e74c3c;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9em;
            transition: background 0.3s;
        }
        
        .clear-btn:hover {
            background: #c0392b;
        }
        
        .history-list {
            list-style: none;
            max-height: 300px;
            overflow-y: auto;
        }
        
        .history-item {
            padding: 12px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 8px;
            border-left: 3px solid #667eea;
        }
        
        .examples {
            margin-top: 30px;
            padding: 20px;
            background: #fff8e1;
            border-radius: 10px;
            border-left: 4px solid #ffc107;
        }
        
        .examples-title {
            color: #f57c00;
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .example-item {
            color: #666;
            margin: 5px 0;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧮 Calculator Agent</h1>
        <p class="subtitle">Your Intelligent Mathematical Assistant</p>
        
        <div class="input-group">
            <label for="query">Ask a math question:</label>
            <input type="text" id="query" placeholder="e.g., What's 25 + 17?" autofocus>
        </div>
        
        <button onclick="calculate()">Calculate</button>
        
        <div id="result" class="result">
            <div class="result-label">Result:</div>
            <div id="result-text" class="result-text"></div>
        </div>
        
        <div class="history">
            <div class="history-title">
                <span>Recent Calculations</span>
                <button class="clear-btn" onclick="clearHistory()">Clear History</button>
            </div>
            <ul id="history-list" class="history-list"></ul>
        </div>
        
        <div class="examples">
            <div class="examples-title">💡 Example Questions:</div>
            <div class="example-item">• "What's 25 + 17?"</div>
            <div class="example-item">• "Calculate square root of 144"</div>
            <div class="example-item">• "What's 5 squared?"</div>
            <div class="example-item">• "sin of 30 degrees"</div>
            <div class="example-item">• "5 factorial"</div>
        </div>
    </div>
    
    <script>
        // Load history on page load
        window.onload = function() {
            loadHistory();
        };
        
        // Handle Enter key press
        document.getElementById('query').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                calculate();
            }
        });
        
        async function calculate() {
            const query = document.getElementById('query').value;
            if (!query.trim()) return;
            
            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ query: query })
                });
                
                const data = await response.json();
                
                // Display result
                document.getElementById('result-text').textContent = data.result;
                document.getElementById('result').classList.add('show');
                
                // Reload history
                loadHistory();
                
                // Clear input
                document.getElementById('query').value = '';
                
            } catch (error) {
                document.getElementById('result-text').textContent = 'Error: ' + error.message;
                document.getElementById('result').classList.add('show');
            }
        }
        
        async function loadHistory() {
            try {
                const response = await fetch('/history');
                const data = await response.json();
                
                const historyList = document.getElementById('history-list');
                historyList.innerHTML = '';
                
                data.history.forEach(item => {
                    const li = document.createElement('li');
                    li.className = 'history-item';
                    li.textContent = item.query + ' = ' + item.result;
                    historyList.appendChild(li);
                });
                
            } catch (error) {
                console.error('Error loading history:', error);
            }
        }
        
        async function clearHistory() {
            try {
                await fetch('/clear', { method: 'POST' });
                loadHistory();
            } catch (error) {
                console.error('Error clearing history:', error);
            }
        }
    </script>
</body>
</html>
    """
    
    def __init__(self, agent: CalculatorAgent, host: str = '0.0.0.0', port: int = 5000):
        """
        Initialize the web interface.
        
        Args:
            agent: The CalculatorAgent instance to use
            host: Host to bind to (default: 0.0.0.0)
            port: Port to listen on (default: 5000)
        """
        self.agent = agent
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self._setup_routes()
    
    def _setup_routes(self) -> None:
        """Set up Flask routes for the web interface."""
        
        @self.app.route('/')
        def index():
            """Serve the main HTML page."""
            return render_template_string(self.HTML_TEMPLATE)
        
        @self.app.route('/calculate', methods=['POST'])
        def calculate():
            """Handle calculation requests."""
            data = request.get_json()
            query = data.get('query', '')
            
            if not query:
                return jsonify({'error': 'No query provided'}), 400
            
            result = self.agent.process_query(query)
            return jsonify({'result': result})
        
        @self.app.route('/history', methods=['GET'])
        def get_history():
            """Get calculation history."""
            history = self.agent.memory.get_history(limit=10)
            return jsonify({'history': history})
        
        @self.app.route('/clear', methods=['POST'])
        def clear_history():
            """Clear calculation history."""
            self.agent.clear_history()
            return jsonify({'success': True})
    
    def get_input(self) -> str:
        """
        Get input from web request.
        
        Note: Not used in web interface as input comes via HTTP requests.
        
        Returns:
            Empty string
        """
        return ""
    
    def display_output(self, message: str) -> None:
        """
        Display output via HTTP response.
        
        Note: Not used in web interface as output is sent via HTTP responses.
        
        Args:
            message: Message to display
        """
        pass
    
    def run(self) -> None:
        """
        Start the Flask web server.
        
        This starts the web server and makes the calculator available
        at http://localhost:5000 (or the configured host/port).
        """
        print(f"\n{'='*60}")
        print(f"Calculator Agent Web Interface")
        print(f"{'='*60}")
        print(f"\nServer starting at http://{self.host}:{self.port}")
        print(f"\nOpen your browser and navigate to:")
        print(f"  → http://localhost:{self.port}")
        print(f"\nPress Ctrl+C to stop the server\n")
        print(f"{'='*60}\n")
        
        self.app.run(host=self.host, port=self.port, debug=False)
