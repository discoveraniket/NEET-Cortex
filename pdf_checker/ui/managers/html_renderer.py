import os

class HTMLRenderer:
    """Handles HTML generation by injecting content into a template."""
    
    def __init__(self):
        self.template_html = ""
        try:
            # Determine the path to the template relative to this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Navigate up one level to the 'ui' directory to find the template
            template_path = os.path.join(current_dir, '..', 'question_renderer.html')
            with open(template_path, 'r', encoding='utf-8') as f:
                self.template_html = f.read()
        except FileNotFoundError:
            # Fallback or error logging
            print(f"ERROR: HTML template not found at {template_path}")
            self.template_html = "<html><body><h1>Error: Template not found.</h1><p>__CONTENT_PLACEHOLDER__</p></body></html>"

    def generate_html(self, raw_text: str) -> str:
        """Injects raw text into the HTML template."""
        if not isinstance(raw_text, str):
            raw_text = str(raw_text)
        
        # Replace the placeholder with the actual content
        return self.template_html.replace('__CONTENT_PLACEHOLDER__', raw_text)