from docx import Document
from docx.shared import Inches

import docx2txt
mytext = docx2txt.process("/path/2019-USAPhO-Qualifiers.docx")

document = Document()


p = document.add_paragraph(mytext)


document.save('/path/fixed-format.docx')