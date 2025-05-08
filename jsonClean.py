import json
import re


def clean_json_string(json_string):
    """
    Cleans a JSON string by removing code block markers and validates the JSON.
    
    Args:
        json_string (str): The JSON string with possible code block markers
        
    Returns:
        str: The cleaned valid JSON string
        
    Raises:
        ValueError: If the cleaned string is not valid JSON
    """
    # Remove the ```json at the beginning
    cleaned = re.sub(r'^```(?:json)?\n', '', json_string)
    
    # Remove the ``` at the end
    cleaned = re.sub(r'```\s*$', '', cleaned)
    
    # Trim any whitespace
    cleaned = cleaned.strip()
    
    # Validate the JSON
    try:
        json_object = json.loads(cleaned)
        return json_object
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON after cleaning: {e}")