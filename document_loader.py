import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import (
    TextLoader, 
    PyPDFLoader,
)

from dotenv import load_dotenv

load_dotenv()

def load_text_file():
    # Create a temporary text file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name

    try:
        # Load the text file using TextLoader
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        for doc in documents:
            print("Document Content: ", doc)
            print(doc.page_content)
    
    finally:
        os.remove(temp_file_path)

def pdf_loader(pdf_file):
    try:
        loader = PyPDFLoader(pdf_file)
        documents = loader.load()

        for doc in documents:
            print("Document Content: ", doc)
            print(doc.page_content)
    
    except Exception as e:
        print(f"An error occurred while loading the PDF: {e}")

if __name__ == "__main__":
    # load_text_file()
    pdf_loader("./docs/langchain_demo.pdf")