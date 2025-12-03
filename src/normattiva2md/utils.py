import os
import re

def load_env_file():
    """
    Load environment variables from .env file if it exists.
    This allows storing API keys locally without exporting them each time.
    """
    # Search in current working directory and up directory tree
    search_paths = [
        os.getcwd(),
        os.path.dirname(__file__), # package dir
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))) # project root (approx)
    ]

    for path in search_paths:
        env_path = os.path.join(path, ".env")
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            # Split on first '=' to handle values with '='
                            if "=" in line:
                                key, value = line.split("=", 1)
                                key = key.strip()
                                value = value.strip()
                                # Remove quotes if present
                                if (value.startswith('"') and value.endswith('"')) or (
                                    value.startswith("'") and value.endswith("'")
                                ):
                                    value = value[1:-1]
                                os.environ[key] = value
                # Found and loaded, stop searching
                break
            except Exception as e:
                # Silently ignore errors loading .env file
                pass

def sanitize_output_path(path, allow_absolute=True):
    """
    Sanitizes an output file path to prevent path traversal attacks.

    Args:
        path: File path to sanitize
        allow_absolute: Whether to allow absolute paths

    Returns:
        str: Sanitized absolute path

    Raises:
        ValueError: If path attempts traversal outside working directory
    """
    if not path:
        raise ValueError("Path non può essere vuoto")

    # Convert to absolute path
    abs_path = os.path.abspath(path)

    # Get working directory
    cwd = os.path.abspath(os.getcwd())

    # If not allowing absolute paths or path is outside cwd, reject
    if not allow_absolute and not abs_path.startswith(cwd):
        raise ValueError(f"Path fuori dalla directory di lavoro: {path}")

    # Check for common path traversal patterns
    if ".." in path or path.startswith("/etc") or path.startswith("/sys"):
        raise ValueError(f"Path non sicuro rilevato: {path}")

    return abs_path

def generate_snake_case_filename(title):
    """
    Generate a snake_case filename from a document title.
    
    Args:
        title (str): Document title
        
    Returns:
        str: Snake case filename with .md extension
    """
    # Remove special characters and convert to lowercase
    cleaned = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces and hyphens with underscores
    snake = re.sub(r'[-\s]+', '_', cleaned)
    # Remove leading/trailing underscores
    snake = snake.strip('_')
    # Truncate to reasonable length (max 100 chars before .md)
    if len(snake) > 100:
        snake = snake[:100].rstrip('_')
    
    return f"{snake}.md"
