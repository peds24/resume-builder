import json
import sys
import os
import logging
from datetime import datetime

from docx_fill import *
from claude_connection import *
from jsonClean import *


def setup_logging():
    """Set up logging to save logs in the ./run-logs/ directory."""
    os.makedirs('./run-logs', exist_ok=True)
    log_filename = datetime.now().strftime('./run-logs/run-log-%Y-%m-%d_%H-%M-%S.log')
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging initialized.")


def load_user_profile(file_path):
    """Load user profile from JSON file and validate its format."""
    logging.info(f"Loading user profile from {file_path}")
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            logging.info(f"User profile loaded successfully: {data}")
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON format in {file_path}: {e}")
            raise ValueError(f"Invalid JSON format in {file_path}: {e}")
    
    return data


if __name__ == "__main__":
    setup_logging()

    company = input("Enter the company name: ")
    role = input("Enter the role you are applying for: ")
    print("Enter job description (press Enter followed by Ctrl+D on Unix/Linux or Ctrl+Z Windows when finished):")
    job_description = sys.stdin.read()
    print("-" * 50)

    logging.info(f"Company: {company}")
    logging.info(f"Role: {role}")
    logging.info(f"Job Description: {job_description}")

    try:
        user_profile_json = load_user_profile("data/profile.json")
        
        job_description_json = {"job_description": job_description}
        logging.info(f"Job Description JSON: {job_description_json}")
        
        enhanced_info = send_message_claude(user_profile_json, job_description_json)
        logging.info(f"Enhanced Info from Claude: {enhanced_info}")
        
        try:
            json_enhanced_info = clean_json_string(enhanced_info)
        except Exception as e:
            logging.error(f"Failed to extract valid JSON from enhanced info: {e}")
            raise ValueError(f"Failed to extract valid JSON from enhanced info: {e}")
        
        logging.info(f"Extracted Enhanced JSON Info: {json_enhanced_info}")

        output_path = f'./output_docs/pedro-serdio-CV-{company}-{role}.docx'
        template_path = './data/resumeTemplate.docx'
        logging.info(f"Template Path: {template_path}")
        logging.info(f"Output Path: {output_path}")

        resume = fill_resume(template_path, output_path, json_enhanced_info)
        logging.info("Resume generation completed successfully.")
        
        print("Resume Generated Successfully, check output_docs directory")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        print(f"An error occurred: {e}")
        
        