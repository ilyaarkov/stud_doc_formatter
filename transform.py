import docx
from docx.shared import Pt

# read in a document 
document = docx.Document("/Users/igor/Projects/stud_doc_formatter/test_doc/test_file.docx")

# flag to indicate if the previous paragraph contained an image
prev_paragraph_had_image = False

# iterate over paragraphs in the document
for paragraph in document.paragraphs:
    # check if the paragraph contains an image
    paragraph_has_image = any('graphicData' in run._r.xml for run in paragraph.runs)

    # if the previous paragraph had an image, change the font size of the current paragraph
    if prev_paragraph_had_image:
        for run in paragraph.runs:
            run.font.size = Pt(8)

    # update the flag for the next iteration
    prev_paragraph_had_image = paragraph_has_image

document.save('demo.docx')