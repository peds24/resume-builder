import json

def extract_valid_json_from_file(file_path):
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            raw_string = file.read()
        
        # Clean up the string
        cleaned_string = raw_string.replace('\n', '').replace('\"', '"').strip()
        
        # Parse JSON
        parsed_json = json.loads(cleaned_string)
        return parsed_json
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except json.JSONDecodeError as e:
        return f"Invalid JSON format: {e}"

def save_json_to_file(json_data, output_path):
    try:
        # Save the JSON data to a new file
        with open(output_path, 'w') as file:
            json.dump(json_data, file, indent=2)
        return f"JSON data successfully saved to {output_path}"
    except Exception as e:
        return f"Error saving JSON to file: {e}"


def extract_valid_json_from_string(raw_string):
    try:
        # Clean up the string
        cleaned_string = raw_string.replace('\n', '').replace('\"', '"').strip()
        
        # Parse JSON
        parsed_json = json.loads(cleaned_string)
        return parsed_json
    except json.JSONDecodeError as e:
        return f"Invalid JSON format: {e}"


