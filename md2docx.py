import os
from spire.doc import *
from spire.doc.common import *

def convert_md_to_docx(input_file, output_file):
    # Create a Document object
    document = Document()
    
    # Load the Markdown file
    document.LoadFromFile(input_file)
    
    # Save as docx file
    document.SaveToFile(output_file, FileFormat.Docx2016)
    
    # Dispose resources
    document.Dispose()

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create output directory if it doesn't exist
output_dir = os.path.join(current_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

# Process all .md files in the current directory
for filename in os.listdir(current_dir):
    if filename.endswith('.md'):
        input_path = os.path.join(current_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.docx'
        output_path = os.path.join(output_dir, output_filename)
        
        print(f"Converting {filename} to {output_filename}...")
        convert_md_to_docx(input_path, output_path)

print("Conversion completed!")