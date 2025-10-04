# PDF Checker

This is a Python application for viewing and correcting OCR data from PDF files. It's built with PySide6 and is designed to help with the process of verifying and correcting data extracted from PDF documents.

## Features

- View PDF pages and extracted OCR data side-by-side.
- Edit and correct OCR data.
- Save corrected data back to a JSON file.
- Navigate through questions and pages.

## Project Structure

```
pdf_checker/
├── app/                # Core application logic
├── data/               # Data management (loading, saving)
├── ui/                 # User interface (PySide6 views and widgets)
├── utils/              # Utility scripts and functions
├── main.py             # Main application entry point
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the `main.py` script:

```bash
python main.py --pdf <path-to-pdf> --bbox-json <path-to-bbox-json> --ocr-json <path-to-ocr-json>
```

