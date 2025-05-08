from docx import Document
import docx
from docx.oxml import parse_xml
import json

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

if __name__ == '__main__':
    with open('./data/profile.json', 'r') as file:
        data = json.load(file)

    # with open('./data/sample.json', 'r') as file:
    #     data = json.load(file)

        output_path = './output_docs/pedro-serdio-CV.docx'
        template_path = './data/resumeTemplate.docx'

        fill_resume(template_path, output_path, data)
