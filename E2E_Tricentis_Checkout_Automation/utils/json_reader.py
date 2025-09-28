# utils/json_reader.py
import json
import os

def JsonReader(file_path):
    """
    Reads a JSON file and returns its content as a dictionary.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)