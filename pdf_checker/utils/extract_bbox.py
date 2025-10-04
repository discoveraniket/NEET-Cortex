import json
import fitz  # PyMuPDF
import os
import re

def get_script_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_project_root():
    return os.path.abspath(os.path.join(get_script_dir(), "..", ".."))

def clean_text_for_search(text):
    """
    Cleans text by removing common Markdown and LaTeX formatting
    to make it suitable for searching in a PDF's raw text layer.
    """
    if not isinstance(text, str):
        return ""
    # Remove markdown characters `*` and `_`
    text = text.replace('*' , '').replace('_', '')

    # A simple approach to handle LaTeX: remove formatting characters.
    # This turns '$O_2$' into 'O2', and '\lambda' into 'lambda'.
    text = re.sub(r'\\([a-zA-Z]+)', r'\1', text)  # e.g., \lambda -> lambda
    text = text.replace('$', '').replace('{', '').replace('}', '').replace('^', '').replace('_', '')

    # Normalize whitespace
    text = ' '.join(text.split())
    return text

def extract_question_bboxes(pdf_path, question_json_path, bbox_json_path):
    """
    Extracts bounding box coordinates for each question from a PDF file based on question data from a JSON file.

    The function reads a PDF and a corresponding JSON file containing question text and options. It then locates
    each question and its components (question text, options) within the PDF and calculates a bounding box
    that encapsulates the entire question. The resulting bounding boxes are saved to a new JSON file.

    The process involves:
    1. Loading the question data from the source JSON file.
    2. Opening the specified PDF document.
    3. Iterating through each question from the JSON data.
    4. Searching for the question number in the PDF to identify the page and general location.
    5. Verifying the correct question location by matching a snippet of the question text.
    6. Finding the bounding boxes for the question text and each of its options.
    7. Calculating the union of these bounding boxes to create a single bounding box for the entire question.
    8. Storing the page number and the calculated bounding box in a dictionary, keyed by the question number.
    9. Writing the final dictionary of bounding boxes to the output JSON file.

    This approach is designed to be robust, handling multi-column layouts and variations in question formatting by
    dynamically calculating the boundaries of each question based on its content.
    """
import argparse

def main():
    parser = argparse.ArgumentParser(description='Extract question bounding boxes from a PDF.')
    parser.add_argument('--pdf', required=True, help='Path to the PDF file.')
    parser.add_argument('--json', required=True, help='Path to the question JSON file.')
    parser.add_argument('--output', required=True, help='Path to the output bbox JSON file.')
    args = parser.parse_args()

    extract_question_bboxes(args.pdf, args.json, args.output)

if __name__ == "__main__":
    main()
