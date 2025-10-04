# NEET-Cortex Project

This repository contains a collection of tools and data for NEET (National Eligibility cum Entrance Test) preparation.

## Project Structure

- `pdf_checker/`: A Python application built with PySide6 to view, correct, and manage OCR data extracted from NEET question papers. See the [pdf_checker/README.md](pdf_checker/README.md) for more details on this tool.
- `PYQ/`: Contains Previous Year Question papers in PDF format and their corresponding extracted data in JSON format.
- `requirements.txt`: Lists all the Python dependencies required to run the tools in this project.

## Setup

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2.  Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the PDF checker tool, see the instructions in its [README file](pdf_checker/README.md).
