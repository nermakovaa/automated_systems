import pytest

from src.docs.docx_parser import parse_docx
from src.docs.doc_parser import parse_doc
from src.docs.pdf_parser import parse_pdf


def load_txt(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


@pytest.mark.parametrize(
    "docx_path, reference_text_path, reference_hyperlinks_path",
    [
        (
            "./tests/docs/example.docx",
            "./tests/reference/example_docx_-text.txt",
            "./tests/reference/example_docx_-hyperlinks.txt"
        )
    ],
)
def test_docx_parser(docx_path, reference_text_path, reference_hyperlinks_path):
    text_path, hyperlinks_path = parse_docx(docx_path)
    output_text = load_txt(text_path)
    output_hyperlinks = load_txt(hyperlinks_path)

    reference_text = load_txt(reference_text_path)
    reference_hyperlinks = load_txt(reference_hyperlinks_path)

    assert output_text == reference_text
    assert output_hyperlinks == reference_hyperlinks


@pytest.mark.parametrize(
    "pdf_path, reference_text_path, reference_hyperlinks_path",
    [
        (
            "./tests/docs/example.pdf",
            "./tests/reference/example_pdf_-text.txt",
            "./tests/reference/example_pdf_-hyperlinks.txt"
        )
    ],
)
def test_pdf_parser(pdf_path, reference_text_path, reference_hyperlinks_path):
    text_path, hyperlinks_path = parse_pdf(pdf_path)
    output_text = load_txt(text_path)
    output_hyperlinks = load_txt(hyperlinks_path)

    reference_text = load_txt(reference_text_path)
    reference_hyperlinks = load_txt(reference_hyperlinks_path)
    
    assert output_text == reference_text
    assert output_hyperlinks == reference_hyperlinks


@pytest.mark.parametrize(
    "doc_path, reference_text_path, reference_hyperlinks_path",
    [
        (
            "./tests/docs/example.doc",
            "./tests/reference/example_doc_-text.txt",
            "./tests/reference/example_doc_-hyperlinks.txt"
        )
    ],
)
def test_doc_parser(doc_path, reference_text_path, reference_hyperlinks_path):
    text_path, hyperlinks_path = parse_doc(doc_path)
    output_text = load_txt(text_path)
    output_hyperlinks = load_txt(hyperlinks_path)

    reference_text = load_txt(reference_text_path)
    reference_hyperlinks = load_txt(reference_hyperlinks_path)

    assert output_text == reference_text
    assert output_hyperlinks == reference_hyperlinks
    