import json
import pathlib
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List, Optional

# --- Pydantic Models for API Response Validation ---

class ExamDetails(BaseModel):
    """Details about the exam paper."""
    year: int = Field(..., description="The year the exam was conducted.")
    subject: str = Field(..., description="The subject of the exam paper, e.g., 'Biology'.")

class MatchColumns(BaseModel):
    """Holds the two columns for a 'match the following' question."""
    columnA: List[str] = Field(..., description="Items in the first column for matching.")
    columnB: List[str] = Field(..., description="Items in the second column for matching.")

class Question(BaseModel):
    """Represents a single question in the API's list-based output."""
    questionNumber: int = Field(..., description="The unique number identifying the question.")
    questionText: str = Field(..., description="The full text of the question.")
    page: int = Field(..., description="The page number where the question is located.")
    bbox: List[float] = Field(..., description="The bounding box coordinates [x0, y0, x1, y1] of the question block.")
    imagePath: Optional[str] = Field(None, description="Optional relative path to an image, e.g., 'images/2019_88.jpg'.")
    matchColumns: Optional[MatchColumns] = Field(None, description="For 'match the following' questions, contains the columns to be matched.")
    options: List[str] = Field(..., description="A list of possible answers.")
    correctOption: int = Field(..., description="The number corresponding to the correct option.")

class QuestionBank(BaseModel):
    """The root model for the API's list-based response."""
    examDetails: ExamDetails = Field(..., description="Metadata about the exam.")
    questions: List[Question] = Field(..., description="A list of all questions in the paper.")

# --- GenAI Client and Configuration ---
client = genai.Client()

# System instruction for the language model
si = """
You are an expert academic data extractor. Analyze the provided exam paper PDF and extract all questions into structured JSON format.

**Formatting Guidelines:**
- Use **Markdown** with **LaTeX-style notation** for all scientific, mathematical, and chemical content
- Maintain proper formatting for subscripts, superscripts, equations, and special symbols

**Output Requirements:**
- For each question, include its number, full text, options, and correct answer.
- You must also include the page number and the precise bounding box coordinates (`[x0, y0, x1, y1]`) for the entire question block.
- For "match the following" questions, structure the column data appropriately.
- If images are present, generate paths in format: `images/[year]_[question_number].jpg`.
- Maintain the exact JSON schema provided.
"""

# The response schema is our root Pydantic model
rs = QuestionBank

# Construct the path to the PDF relative to the script's own location
pdf_name = '2018'
script_dir = pathlib.Path(__file__).parent.parent
input_file = script_dir / 'BIO' / 'pdf'/ f'{pdf_name}.pdf'
output_file = script_dir / 'BIO' / 'json' / f'{pdf_name}.json'

print(f"Processing {input_file.name}...")
response = client.models.generate_content(
    model="gemini-2.5-flash", # Do not change the model
    config=types.GenerateContentConfig(
        system_instruction=si,
        response_mime_type="application/json",
        response_schema=rs),
    contents=[
        types.Part.from_bytes(
            data=input_file.read_bytes(),
            mime_type='application/pdf',
        ),
    ]
)

# --- Process, Convert, and Save Response ---

if response.text:
    # Load the AI's list-based output
    data = json.loads(response.text)

    # --- Convert to the standard key-based format ---
    standard_questions = {}
    if 'questions' in data and isinstance(data['questions'], list):
        for question in data['questions']:
            q_num = question.pop('questionNumber', None)
            if q_num is not None:
                new_key = f"qn_{q_num}"
                standard_questions[new_key] = question

    # Replace the list with the new dictionary
    data['questions'] = standard_questions

    # --- Write the final, standardized JSON ---
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully saved standardized questions to {output_file}")
else:
    print("Received an empty response from the API.")
