import pdfminer.high_level
from io import BytesIO

def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file uploaded by the user.
    The file is processed in-memory without saving it.
    
    :param file: File object from Flask request
    :return: Extracted text as a string
    """
    text = pdfminer.high_level.extract_text(BytesIO(file.read()))
    file.seek(0)  # Reset file pointer after reading to allow re-use
    return text
