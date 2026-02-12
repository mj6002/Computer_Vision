import PyPDF2
from PyPDF2 import PdfReader
from docx import Document

def extract_highlights_from_pdf(pdf_path):
    highlights = []

    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            annotations = page.extract_annotations()
            if annotations:
                for annotation in annotations:
                    content = annotation.get('content')
                    if content:
                        highlights.append(content)

    return highlights


def save_highlights_to_word(highlights, word_path):
    doc = Document()
    for highlight in highlights:
        doc.add_paragraph(highlight)
    doc.save(word_path)


if __name__ == "__main__":
    pdf_path = "d:/Revaluation-15514 (1).pdf"
    word_path = "d:/Revaluation-15514 (1).docx"
    highlights = extract_highlights_from_pdf(pdf_path)
    save_highlights_to_word(highlights, word_path)
