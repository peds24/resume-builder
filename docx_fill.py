from docx import Document
import docx
from docx.oxml import parse_xml

"""
Fills a Word document template with provided data and saves the output.
This function takes a Word document template, replaces placeholders in the 
template with corresponding values from the provided data, and saves the 
modified document to the specified output path. It supports replacing 
placeholders with plain text, bullet points, and structured content such as 
headers with descriptions.
Args:
    template_path (str): The file path to the Word document template.
    output_path (str): The file path where the filled document will be saved.
    data (dict): A dictionary containing the data to fill in the template. 
                 Keys represent placeholders in the template, and values 
                 represent the content to replace them with. The values can 
                 be:
                 - A string for simple text replacement.
                 - A list of strings for bullet points (e.g., qualifications).
                 - A list of dictionaries for structured content, where each 
                   dictionary contains:
                   - 'header' (str): The header text.
                   - 'description' (list): A list of strings for bullet points 
                     under the header.
Raises:
    KeyError: If a placeholder in the template is not found in the data.
    ValueError: If the data format is invalid.
Example:
    with open("data.json", "r") as file:
        data = json.load(file)
    fill_resume("template.docx", "output.docx", data)
"""
def fill_resume(template_path, output_path, data):
    doc = Document(template_path)
    
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                if key == paragraph.text:
                    if isinstance(value, list):
                        if (key == '[qualifications]'):
                            # Logic to add bullet points for qualifiactions
                            p_to_replace = paragraph._element
                            parent = p_to_replace.getparent()
                                
                            for item in value:
                                new_p = doc.add_paragraph(item, style='List Paragraph')
                                new_p._p.get_or_add_pPr().append(
                                    parse_xml('<w:numPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>')
                                )
                                parent.insert(parent.index(p_to_replace), new_p._element)
                            parent.remove(p_to_replace)
                            continue
                        else:
                            # logic for jobs, projects which feature heading and description
                            p_to_replace = paragraph._element
                            parent = p_to_replace.getparent()
            
                            for item in value:
                                header = doc.add_paragraph()
                                header_run = header.add_run(item['header'])
                                header_run.bold = True
                                parent.insert(parent.index(p_to_replace), header._element)
                                
                                for point in item['description']:
                                    bullet_p = new_p = doc.add_paragraph(point, style='List Paragraph')
                                    new_p._p.get_or_add_pPr().append(
                                        parse_xml('<w:numPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>')
                                    )
                                    parent.insert(parent.index(p_to_replace), bullet_p._element)
                            parent.remove(p_to_replace)
                            continue
                    else:
                        style = doc.styles['Normal']
                        font = style.font
                        font.name = 'Times New Roman'
                        font.size = docx.shared.Pt(10)
                        paragraph.text = paragraph.text.replace(key, value)

                for run in paragraph.runs:
                    style = doc.styles['Normal']
                    font = style.font
                    font.name = 'Times New Roman'
                    font.size = docx.shared.Pt(10)
                    run.text = run.text.replace(key, value)

    doc.save(output_path)

# if __name__ == '__main__':
#     with open('./data/profile.json', 'r') as file:
#         data = json.load(file)

#     # with open('./data/sample.json', 'r') as file:
#     #     data = json.load(file)

#         output_path = './output_docs/pedro-serdio-CV.docx'
#         template_path = './data/resumeTemplate.docx'

#         fill_resume(template_path, output_path, data)
