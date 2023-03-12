import aspose.words as aw
from .docx_parser import parse_docx
from os.path import join
from tempfile import gettempdir

ASPOSE_STRING = "Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd."


def create_temp_docx(doc_path):
    doc = aw.Document(doc_path)
    
    temp_docx_path = f"temp{doc.__hash__()}.docx"
    temp_docx_path = join(gettempdir(), temp_docx_path)
    doc.save(temp_docx_path)

    return temp_docx_path


def parse_doc(path):
    document_name_ext = path.split("/")[-1]
    document_name = document_name_ext.split(".")[0]

    temp_docx_path = create_temp_docx(path)
    
    text_path, hyperlinks_path = parse_docx(temp_docx_path, document_name, '.doc', ASPOSE_STRING)

    return text_path, hyperlinks_path
