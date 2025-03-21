<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Code Copilot - README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 20px;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code {
      background-color: #f4f4f4;
      padding: 2px 5px;
      border-radius: 3px;
      font-family: "Courier New", monospace;
    }
    pre {
      background-color: #282c34;
      color: #abb2bf;
      padding: 15px;
      border-radius: 5px;
      overflow-x: auto;
    }
    a {
      color: #3498db;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
    }
    .section {
      margin-bottom: 30px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>AI Code Copilot</h1>
    <p>An AI-powered coding assistant that helps you create, modify, and organize files and folders in your project. Built with <strong>Gemini API</strong> and designed to run in <strong>GitHub Codespaces</strong>.</p>

    <div class="section">
      <h2>Features</h2>
      <ul>
        <li><strong>File Operations</strong>: Create, read, modify, and delete files/folders.</li>
        <li><strong>Project Awareness</strong>: Understands your project structure and context.</li>
        <li><strong>Natural Language Interface</strong>: Interact with the AI using plain English.</li>
        <li><strong>Safe Execution</strong>: Confirms actions before executing file operations

Here’s a **README.md** file for your project. This document explains the purpose, setup, and usage of your AI-powered coding assistant.

---

# AI Code Copilot

An AI-powered coding assistant that helps you create, modify, and organize files and folders in your project. Built with **Gemini API** and designed to run in **GitHub Codespaces**.

---

## Features

- **File Operations**: Create, read, modify, and delete files/folders.
- **Project Awareness**: Understands your project structure and context.
- **Natural Language Interface**: Interact with the AI using plain English.
- **Safe Execution**: Confirms actions before executing file operations.
- **React/JS Support**: Generates React components and utility files.

---

## Setup

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment Variables**
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
MONGO_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/code_copilot?retryWrites=true&w=majority
DB_NAME=code_copilot
```

Check Your environement 
```bash
echo $GEMINI_API_KEY
echo $MONGO_URI
echo $DB_NAME
```
And 

```bash
python3 -c "
from pymongo import MongoClient
import os
client = MongoClient(os.getenv('MONGO_URI'))
print(client.server_info())
"
```

### 4. **Run the Copilot**
```bash
python main.py
```

---

## Usage

### Start the Copilot
```bash
python main.py
🤖 Code Execution Agent - GitHub Codespace
```

### Example Commands
1. **Create a React Component**:
   ```
   You: Create src/components/Button.jsx with a React button component
   ```

2. **Create a Utility File**:
   ```
   You: Create src/utils/helpers.js with utility functions
   ```

3. **Read a File**:
   ```
   You: Read src/components/Button.jsx
   ```

4. **Exit the Copilot**:
   ```
   You: exit
   ```

---

## Project Structure

```
.
├── .env                    # Environment variables
├── .gitignore              # Ignore .env and other files
├── requirements.txt        # Python dependencies
├── app/
│   ├── __init__.py         # Package initialization
│   ├── file_ops.py         # File system operations
│   ├── gemini_brain.py     # AI integration
│   ├── mongo_db.py         # Database handling (optional)
│   └── execution_engine.py # Core logic
└── main.py                 # Entry point
```

---

## Dependencies

- **Python 3.8+**
- **Google Generative AI SDK**: `google-generativeai`
- **MongoDB (Optional)**: For conversation history
- **dotenv**: For environment variable management

---

## Example Workflow

### 1. Create a React Component
```bash
You: Create src/components/Header.jsx with a React header component

Generated Code:
header_component = """
import React from 'react';

function Header({ title }) {
  return (
    <header className="header">
      <h1>{title}</h1>
    </header>
  );
}

export default Header;
"""

create_file("src/components/Header.jsx", header_component)

Result: Created: src/components/Header.jsx
```

### 2. Create a Utility File
```bash
You: Create src/utils/helpers.js with utility functions

Generated Code:
helpers_code = """
export function formatDate(date) {
  return new Date(date).toLocaleDateString();
}

export function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}
"""

create_file("src/utils/helpers.js", helpers_code)

Result: Created: src/utils/helpers.js
```

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Google Gemini API**: For powering the AI.
- **GitHub Codespaces**: For providing the development environment.

---

Let me know if you'd like to add more sections or customize this further!

# Ai_Agent
.
├── .env
├── .gitignore
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── file_ops.py       # File operations
│   ├── gemini_brain.py   # AI processing
│   ├── mongo_db.py       # Database handling
│   └── execution_engine.py # Core logic
└── main.py


