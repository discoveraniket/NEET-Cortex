import re
from markdown2 import Markdown
from pylatexenc.latex2text import LatexNodes2Text

def convert_latex_to_html(text: str) -> str:
    """
    Converts LaTeX-like syntax within a string to corresponding HTML tags or Unicode.
    """
    # First, let pylatexenc handle commands it knows, converting them to Unicode
    try:
        # This will convert things like \lambda to a unicode 'λ'
        text = LatexNodes2Text().latex_to_text(text)
    except Exception:
        # If pylatexenc fails, just continue with the original text
        pass

    # Now, convert our custom sub/super script syntax to HTML tags
    text = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', text)
    text = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', text)
    
    return text

def convert_to_html(raw_text: str) -> str:
    """
    Converts a raw string containing Markdown and LaTeX into a clean HTML string
    to be rendered by tkhtmlview.
    """
    if not raw_text:
        return ""

    # Step 1: Convert LaTeX to an intermediate format (mix of HTML tags and Unicode)
    processed_text = convert_latex_to_html(raw_text)

    # Step 2: Convert Markdown to HTML, ensuring existing HTML tags are not escaped.
    markdowner = Markdown(extras=["process-html"])
    html = markdowner.convert(processed_text)
    
    # The tkhtmlview widget expects an HTML fragment, not a full document.
    # Return the generated HTML directly.
    return html