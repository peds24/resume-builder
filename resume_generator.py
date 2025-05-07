import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

def load_user_profile(file_path):
    """Load user profile from JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_resume(profile, company, role, job_description):
    return



# if __name__ == "__main__":