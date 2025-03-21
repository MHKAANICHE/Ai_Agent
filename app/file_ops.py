import os
import shutil

# file : create, read, delete, modify, list
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

def rename_file(old_path, new_path):
    """Renames a file from old_path to new_path.

    Args:
        old_path: The original path of the file.
        new_path: The new path for the file.
    """
    try:
        os.rename(old_path, new_path)
    except FileNotFoundError:
        print(f"Error: File not found at {old_path}")
    except OSError as e:
        print(f"Error: Could not rename file: {e}")


def list_files():
    """Lists all files in the current project directory."""
    files = []
    for root, _, filenames in os.walk("."):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files  

# Folder : create, delete, modify
def create_folder(path):
    """Creates a new folder at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)  # exist_ok=True avoids errors if the folder already exists
        return True, f"Folder created successfully at {path}"
    except Exception as e:
        return False, str(e)

def delete_folder(path):
    """Deletes an existing folder at the specified path."""
    try:
        shutil.rmtree(path)
        return True, f"Folder deleted successfully at {path}"
    except FileNotFoundError:
        return False, f"Folder not found at {path}"
    except Exception as e:
        return False, str(e)

def modify_folder(path, new_name=None):
    """Modifies an existing folder. Currently only supports renaming."""
    if new_name:
        try:
            new_path = os.path.join(os.path.dirname(path), new_name)
            os.rename(path, new_path)
            return True, f"Folder renamed successfully from {path} to {new_path}"
        except FileNotFoundError:
            return False, f"Folder not found at {path}"
        except Exception as e:
            return False, str(e)
    else:
        return False, "No modification specified."

def rename_folder(old_path, new_path):
    """Renames a folder from old_path to new_path."""
    try:
        shutil.move(old_path, new_path)
        return True
    except FileNotFoundError:
        print(f"Error: Folder not found at {old_path}")
        return False
    except OSError as e:
        print(f"Error: Could not rename folder: {e}")
        return False
# execute commands        

def execute_command(command):
    try:
        exec(command)
        return "Success"
    except Exception as e:
        return f"command: {command} - Error: {str(e)}"


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

