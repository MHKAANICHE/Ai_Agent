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

def delete_file(path):
    """Deletes a file."""
    try:
        os.remove(path)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False

def modify_file(path, new_content):
    """
    Modifies the content of an existing file.

    Args:
        path (str): The path to the file to modify.
        new_content (str): The new content to write to the file.
    """
    try:
        with open(path, "w") as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"Error modifying file: {e}")
        return False

def list_files():
    """List files in current directory."""
    return "\n".join(os.listdir("."))    

def execute_command(command):
    """Safe command executor"""
    if not command:
        return "Error: No command to execute"
    
    allowed_commands = ['create_file', 'read_file', 'delete_file','modify_file']
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

