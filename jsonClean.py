import json

def extract_valid_json_from_file(file_path):
    """
    Extracts and parses valid JSON content from a file.
    This function reads the content of a file, cleans up the string by removing
    unnecessary newline characters and fixing quotation marks, and then attempts
    to parse it as JSON. If the file is not found or the content is not valid JSON,
    appropriate error messages are returned.
    Args:
        file_path (str): The path to the file containing the JSON content.
    Returns:
        dict or str: The parsed JSON object if successful, or an error message
        string if the file is not found or the JSON format is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            raw_string = file.read()
        
        cleaned_string = raw_string.replace('\n', '').replace('\"', '"').strip()
        
        parsed_json = json.loads(cleaned_string)
        return parsed_json
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except json.JSONDecodeError as e:
        return f"Invalid JSON format: {e}"

def save_json_to_file(json_data, output_path):
    """
    Saves the given JSON data to a specified file.

    This function writes the provided JSON data to a file at the specified
    output path. The JSON data is formatted with an indentation of 2 spaces
    for better readability. If an error occurs during the file writing process,
    an error message is returned.

    Args:
        json_data (dict): The JSON data to be saved.
        output_path (str): The file path where the JSON data will be saved.

    Returns:
        str: A success message if the JSON data is saved successfully, or an
             error message if an exception occurs.
    """
    try:
        with open(output_path, 'w') as file:
            json.dump(json_data, file, indent=2)
        return f"JSON data successfully saved to {output_path}"
    except Exception as e:
        return f"Error saving JSON to file: {e}"


def extract_valid_json_from_string(raw_string):
    """
    Extracts and parses a valid JSON object from a raw string.
    This function cleans up the input string by removing newline characters,
    replacing escaped double quotes with standard double quotes, and stripping
    leading/trailing whitespace. It then attempts to parse the cleaned string
    as JSON.
    Args:
        raw_string (str): The raw string containing JSON data.
    Returns:
        dict or list: The parsed JSON object if the input string is valid JSON.
        str: An error message if the input string is not valid JSON.
    Raises:
        None: The function handles JSONDecodeError internally and returns an error message.
    """
    try:
        cleaned_string = raw_string.replace('\n', '').replace('\"', '"').strip()
        
        parsed_json = json.loads(cleaned_string)
        return parsed_json
    except json.JSONDecodeError as e:
        return f"Invalid JSON format: {e}"


