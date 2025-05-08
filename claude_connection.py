import anthropic
from dotenv import load_dotenv

def send_message_claude(user_profile, job_description):
    load_dotenv()
    
    client = anthropic.Anthropic()
    
    prompt = f"""You are an AI assistant specialized in enhancing resumes to match specific job descriptions. Your task is to analyze a job description and a user's profile, then create an enhanced resume tailored to the job requirements.

    First, carefully read and analyze the following job description:

    <job_description>
    {job_description}
    </job_description>

    Now, examine the user's profile information provided in JSON format:

    <user_profile>
    {user_profile}
    </user_profile>

    Your goal is to enhance the user's resume to better match the job description. 

    1. Generate 4-6 bullet points highlighting the user's qualifications that best match the job description:
    - List key requirements from the job description.
    - Match these requirements with the user's experiences and skills, listing them side by side.
    - Formulate bullet points that highlight these matches.

    2. Enhance the user's technical and professional skills:
    - Create a table with two columns: one for job requirements, one for user's skills.
    - Match skills from both columns, noting any gaps or overlaps.
    - Rephrase user's skills using job description terminology.
    - Group technical skills by categories (e.g., programming languages, frameworks, tools).

    3. Improve the descriptions of the user's job experiences:
    - Identify key achievements in the user's experiences.
    - List these achievements alongside matching job requirements.
    - Rewrite bullet points to emphasize aspects most relevant to the job description.
    - Use similar language and highlight transferable skills.

    4. Enhance the descriptions of the user's projects:
    - Identify relevant aspects of the projects.
    - List these aspects alongside matching job requirements.
    - Rewrite bullet points to emphasize elements most relevant to the job description.
    - Use similar language and highlight transferable skills.

    Important constraints:
    - Do not invent or add any information not present in the user's original profile.
    - Maintain the structure of the original profile while enhancing the content.
    - Use language and terminology from the job description where appropriate.
    - do not show the user the analysis and only return the formated json

    After your analysis, provide the enhanced resume in the following JSON format:

    {{
    "[qualifications]": ["bullet 1", "bullet 2", "bullet 3", "bullet 4"],
    "[tech skills]": "list of technical skills, comma separated, grouped by categories",
    "[prof skills]": "list of professional, personal skills, comma separated",
    "[jobs]": [
    {{
    "header": "job title from input",
    "description": [
    "bullet 1", "bullet 2", "bullet 3", "bullet 4"
    ]
    }}
    ],
    "[projects]": [
    {{
    "header": "project title from input",
    "description": [
    "enhanced bullet 1", "enhanced bullet 2", "enhanced bullet 3", "enhanced bullet 4"
    ]
    }}
    ]
    }}

    Your final output should be the JSON object only, with no additional text or explanations outside the JSON structure."""
    
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=20000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return(message.content[0].text)