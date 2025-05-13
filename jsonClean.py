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
    
    
# def main():
#         # Example JSON string with code block markers
#         json_string = """```json
# {
#   "qualifications": [
#     "Experienced in multiple modern programming languages including Java, Python, C/C++, JavaScript, and TypeScript, with proven application in distributed system environments",
#     "Demonstrated ability to design and build innovative technologies through microservice-based cloud architecture implementation in a banking environment",
#     "Strong experience collaborating with cross-disciplinary teams on time-sensitive projects, working effectively in agile environments to deliver high-quality software",
#     "Practical experience with API integration and asynchronous programming, foundational for building distributed systems at scale",
#     "Proven track record of solving complex business challenges through innovative technology, including automation that reduced processing time from 8-12 weeks to one week"
#   ],
#   "tech_skills": "Programming Languages: Java, Python, C/C++, JavaScript, TypeScript; Distributed Systems: API Integration, Asynchronous Programming, Microservice Architecture; Development Tools: Git, Visual Studio, Linux, Windows, macOS; Frontend: HTML, CSS, React, UI/UX Design, Figma; Backend: Node.js, Quarkus; Cloud & AI: VertexAI, Gemini AI Integration",
#   "prof_skills": "Creative Problem Solver, Algorithmic Thinking, Agile Environment Experience, Cross-Disciplinary Collaboration, Comfortable in Fast-Paced Environments, Effective Communication, Independent Worker, Self-Motivated Learner, Product Ownership, Technical Articulation",
#   "jobs": [
#     {
#       "header": "Software Engineer Intern | Banorte | CDMX, Mexico | July - October 2024",
#       "description": [
#         "Created an efficiency-focused Proof of Concept application that automated document template generation and form completion, transforming a labor-intensive 8-12 week process into a streamlined one-week workflow.",
#         "Designed and implemented a microservice-based cloud architecture using Java/Quarkus, featuring containerized deployment for a Gemini-powered conversational AI application. ",
#         "Engineered JavaScript-based frontend components that interfaced with backend services and Google Vertex AI for intelligent natural language processing capabilities.",
#         "Collaborated with cross-functional teams for this 12-week project, including Cyber Security, Project Managers, AI/ML Coders, and Cloud Developers."
#       ]
#     },
#     {
#       "header": "Software QA Intern | Grupo Caliente | CDMX, Mexico | July - August 2023",
#       "description": [
#         "Gained extensive experience with agile workflows, sprint planning, and cross-functional collaboration in a fast-paced software development environment, learning to prioritize bug fixes and feature development based on business impact.",
#         "Collaborated effectively across multiple development teams including Back End, Front End, App Dev, and Web Dev for major betting websites www.caliente.mx and winner.mx.",
#         "Ensured overall quality of new features and enhancements across desktop and mobile platforms through comprehensive testing procedures.",
#         "Developed understanding of complete software development lifecycle, from requirements gathering through deployment and maintenance phases."
#       ]
#     },
#     {
#       "header": "Sales Associate | UCSD Bookstore | San Diego, CA | May 2022 - March 2025",
#       "description": [
#         "Provide personalized assistance and guidance to customers, creating a positive shopping experience through effective communication and building rapport.",
#         "Play a pivotal role in achieving sales targets, promoting Apple products, handling transactions, and keeping an organized and efficient workspace.",
#         "Responsible for the critical tasks of opening and closing procedures, alongside providing support in comprehensive training to new hires, ensuring smooth integration into our operational protocols at the school bookstore."
#       ]
#     }
#   ],
#   "projects": [
#     {
#       "header": "Developer Journal WebApp, Front-end Developer",
#       "description": [
#         "Designed and developed a local-first developer journal using HTML, CSS, and JavaScript, focusing on lightweight and responsive functionality.",
#         "Created UI/UX design systems, including animations, color schemes, and layouts, informed by wireframing, user stories, and product research.",
#         "Utilized Figma for mock-ups and animations to refine designs before implementation.",
#         "Collaborated with development teams to integrate components, providing guidance on HTML structure within design constraints."
#       ]
#     },
#     {
#       "header": "Digital Book Library Tool, Fullstack Developer",
#       "description": [
#         "Developed a full-stack Python application integrating the Google Books API for metadata retrieval with data storage that manages diverse media types including books, comics, and manga.",
#         "Implemented multiple data input methods including manual entry, individual ISBN lookups, and bulk imports to streamline collection management and reduce cataloging time.",
#         "Designed a modular, extensible codebase with clean architecture principles that separates API handling, database management, and core functionality for maintainability and future expansion.",
#         "Currently planning implementation of a GUI inspired by the Library of Babel website for an interactive, web-accessible display and consultation of book collections."
#       ]
#     }
#   ]
# }
# ```"""

#         # Check if the original string is valid JSON
#         is_valid = json_check(json_string)
#         print(f"Is the original string valid JSON? {is_valid}")

#         # Clean the JSON string and validate it
#         try:
#             cleaned_json = clean_json_string(json_string)
#             print("Cleaned JSON object:", cleaned_json)
#         except ValueError as e:
#             print(e)

# if __name__ == "__main__":
#     main()