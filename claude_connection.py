import anthropic
from dotenv import load_dotenv
"""
Sends a message to the Claude AI model to enhance a user's resume based on a given job description.
This function uses the Anthropic Claude API to analyze a user's profile and a job description, 
and generates an enhanced resume tailored to the job requirements. The enhanced resume is 
returned in a structured JSON format.
Args:
    user_profile (str): A JSON-formatted string containing the user's profile information.
    job_description (str): A string containing the job description to tailor the resume to.
Returns:
    str: A string containing the enhanced resume, including:
        - Qualifications: A list of bullet points highlighting the user's qualifications.
        - Technical skills: A categorized list of technical skills.
        - Professional skills: A list of professional and personal skills.
        - Jobs: A list of enhanced job descriptions with bullet points.
        - Projects: A list of enhanced project descriptions with bullet points.
Notes:
    - The function uses the `dotenv` library to load environment variables.
    - The Claude AI model is invoked via the `anthropic` library.
    - The generated resume strictly adheres to the user's original profile information, 
      using language and terminology from the job description where appropriate.
"""
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

Important constraints:
- Do not invent or add any information not present in the user's original profile.
- Maintain the structure of the original profile while enhancing the content.
- Use language and terminology from the job description where appropriate.
- do not show the user the analysis and only return the formated json
- do not modify the points from the jobs, or projects given in the user profile, only enhance and add to the skills and qualifications

After your analysis, provide the enhanced resume in the following JSON format:

{{
 "[qualifications]": ["bullet 1", "bullet 2", "bullet 3", "bullet 4"],
 "[tech_skills]": "list of technical skills, comma separated, grouped by categories",
 "[prof_skills]": "list of professional, personal skills, comma separated",
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
     "bullet 1", "bullet 2", "bullet 3", "bullet 4"
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