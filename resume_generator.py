import json
import sys

from docx_fill import *
from claude_connection import *
from jsonClean import *


def load_user_profile(file_path):
    """Load user profile from JSON file and validate its format."""
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {file_path}: {e}")
    
    return data


if __name__ == "__main__":
    company = input("Enter the company name: ")
    role = input("Enter the role you are applying for: ")
    print("Enter job description (press Enter followed by Ctrl+D on Unix/Linux or Ctrl+Z Windows when finished):")
    job_description = sys.stdin.read()
    print("-" * 50)

    try:
        user_profile_json = load_user_profile("data/profile.json")
        
        job_description_json = {"job_description": job_description}
        
        enhanced_info = send_message_claude(user_profile_json, job_description_json)
        
        json_enhanced_info = extract_valid_json_from_string(enhanced_info)

        output_path = f'./output_docs/pedro-serdio-CV-{company}-{role}.docx'
        template_path = './data/resumeTemplate.docx'
        resume = fill_resume(template_path, output_path, json_enhanced_info)
        
        print("Resume Generated Sucessuflly, check output_docs directory")
    except Exception as e:
        print(f"An error occurred: {e}")