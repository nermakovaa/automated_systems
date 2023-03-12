import pdfplumber
import PyPDF2


def parse_text(path, document_name):
    with pdfplumber.open(path) as pdf:
        text_path = f"{document_name}_pdf_-text.txt"
        with open(text_path, "w", encoding="utf-8") as f:
            for page in pdf.pages:
                text = page.extract_text()
                f.write(text + "\n")

    return text_path


def parse_hyperlinks(path, document_name):
    PDFFile = open(path, "rb")

    PDF = PyPDF2.PdfReader(PDFFile)

    pages = len(PDF.pages)
    key = "/Annots"
    uri = "/URI"
    ank = "/A"

    hyperlinks_path = f"{document_name}_pdf_-hyperlinks.txt"

    with open(hyperlinks_path, "w", encoding="utf-8") as f:
        for page in range(pages):
            pageSliced = PDF.pages[page]
            pageObject = pageSliced.get_object()
            if key in pageObject.keys():
                ann = pageObject[key]
                for a in ann:
                    u = a.get_object()
                    if uri in u[ank].keys():
                        f.write(u[ank][uri] + "\n")

    return hyperlinks_path


def parse_pdf(path):
    document_name_ext = path.split("/")[-1]
    document_name = document_name_ext.split(".")[0]

    text_path = parse_text(path, document_name)
    hyperlinks_path = parse_hyperlinks(path, document_name)

    return text_path, hyperlinks_path
