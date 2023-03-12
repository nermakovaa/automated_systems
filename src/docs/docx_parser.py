from mammoth import convert_to_html
from bs4 import BeautifulSoup
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT


def parse_text(doc, doc_name, doc_ext, delete_str):
    def para2text(p):
        rs = p._element.xpath('.//w:t')
        return u"".join([r.text for r in rs])

    paragraphs = doc.paragraphs
    text_path = f"{doc_name}_{doc_ext[1:]}_-text.txt"

    with open(text_path, "w", encoding="utf-8") as f:
        for paragraph in paragraphs:
            text = para2text(paragraph)
            if delete_str:
                if text == delete_str:
                    continue
            f.write(text + "\n")
    
    return text_path


def docx2html(doc_path):
    doc = open(doc_path, 'rb')
    html = convert_to_html(doc)
    return html.value


def parse_hyperlinks(doc_path, doc_name, doc_ext):
    html = docx2html(doc_path)
    soup = BeautifulSoup(html, 'lxml')

    hyperlinks_path = f"{doc_name}_{doc_ext[1:]}_-hyperlinks.txt"

    with open(hyperlinks_path, "w", encoding="utf-8") as f:
        for link in soup.findAll('a'):
            f.write(f"{link.string} -- {link.get('href')}\n")
    
    return hyperlinks_path


def parse_docx(path, document_name=None, document_ext='.docx', delete_str=None):
    document = Document(path)
    if not document_name:
        document_name_ext = path.split("/")[-1]
        document_name = document_name_ext.split(".")[0]
    

    text_path = parse_text(document, document_name, document_ext, delete_str)
    hyperlinks_path = parse_hyperlinks(path, document_name, document_ext)

    return text_path, hyperlinks_path