import os
import shutil

def create_file(path, content=""):
    """Safely create a file with content, including parent directories."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)  # Create directories if needed
        with open(path, 'w') as f:
            f.write(content)
        return f"Created: {path}"
    except Exception as e:
        return f"Error: {str(e)}"

def read_file(path):
    """Read file content."""
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"

def list_files():
    """List files in current directory."""
    return "\n".join(os.listdir("."))    

def execute_command(command):
    """Safe command executor"""
    if not command:
        return "Error: No command to execute"
    
    allowed_commands = ['create_file', 'read_file']
    if any(cmd in command for cmd in allowed_commands):
        try:
            exec(command)
            return "Success"
        except Exception as e:
            return f"Error: {str(e)}"
    return "Blocked: Unauthorized command"    

def analyze_project():
    """Analyze project structure and content"""
    project_structure = {}
    for root, dirs, files in os.walk("."):
        relative_path = os.path.relpath(root, ".")
        project_structure[relative_path] = {
            "files": files,
            "file_types": set(os.path.splitext(f)[1] for f in files)
        }
    return project_structure

