import logging
import os
from typing import Dict

# Global storage for loggers and their file paths
_loggers: Dict[str, logging.Logger] = {}
_log_files: Dict[str, str] = {}

def setup_module_logger(module_name: str, output_dir: str, file_number: str) -> logging.Logger:
    """
    Setup a logger for a specific module with its own log file.
    
    Args:
        module_name: Name of the module (e.g., 'main', 'generator', 'comparator')
        output_dir: Directory where log files should be created
        file_number: Number to append to log file names
    
    Returns:
        Logger instance for the module
    """
    logger_key = f"{module_name}_{file_number}"
    
    # Return existing logger if already configured
    if logger_key in _loggers:
        return _loggers[logger_key]
    
    # Create logger
    logger = logging.getLogger(logger_key)
    logger.setLevel(logging.DEBUG)
    
    # Clear any existing handlers
    logger.handlers = []
    
    # Create file handler
    log_file_path = os.path.join(output_dir, f"{module_name}_log_{file_number}.txt")
    file_handler = logging.FileHandler(log_file_path, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(file_handler)
    
    # Prevent propagation to root logger
    logger.propagate = False
    
    # Store logger and file path
    _loggers[logger_key] = logger
    _log_files[logger_key] = log_file_path
    
    return logger

def get_log_files_for_number(file_number: str) -> list:
    """
    Get all log file paths for a specific file number.
    
    Args:
        file_number: The file number to get log files for
    
    Returns:
        List of log file paths
    """
    return [path for key, path in _log_files.items() if key.endswith(f"_{file_number}")]

def suppress_external_logs():
    """Suppress logs from external libraries (OpenAI, HTTP, etc.)"""
    external_loggers = [
        "openai", "httpx", "httpcore", "urllib3", 
        "httpcore.connection", "httpcore.http11", "httpx._client"
    ]
    
    for logger_name in external_loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.WARNING)
        logger.propagate = False