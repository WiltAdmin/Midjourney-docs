"""
Combine Text Files Script

This script combines all text files in a specified directory and writes their contents to a single text file,
with an option to also create a PDF file.

How to use:
1. Ensure you have the `reportlab` library installed. If not, install it with the following command:
    pip install reportlab

2. Save this script to a file, for example, `combine_text_files.py`.

3. Open a terminal and navigate to the directory where the script is saved.

4. Run the script with the following command:
    python combine_text_files.py /path/to/input/directory --output_text.txt --output_pdf output_pdf.pdf

   Replace `/path/to/input/directory`, `output_text.txt`, and `output_pdf.pdf` with the desired input directory and output filenames.
   If you don't want to create a PDF file, simply omit the `--output_pdf` option.
   e.g. python3 combine_text_files.py . --output_pdf output_pdf.pdf
"""

import os
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def combine_text_files(input_dir, output_txt, output_pdf=None):
    """
    Combine all text files in the input directory and write their contents to a single text file,
    with an option to also create a PDF file.

    :param input_dir: Path to the directory containing the text files to be combined.
    :param output_txt: Path to the output text file.
    :param output_pdf: Path to the output PDF file (optional). Default is None.
    """
    combined_content = ""

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    header = f'file path: {file_path}\n# {os.path.splitext(file)[0]}\n\n'
                    combined_content += header + content + "\n\n"
                    combined_content += content + "\n\n"

    if output_pdf:
        pdf = canvas.Canvas(output_pdf, pagesize=letter)
        pdf.setFont("Helvetica", 12)
        x, y = 50, 750

        for line in combined_content.split('\n'):
            if y < 50:
                pdf.showPage()
                y = 750
            pdf.drawString(x, y, line)
            y -= 14

        pdf.save()
    else:
        with open(output_txt, 'w') as f:
            f.write(combined_content)


def main():
    parser = argparse.ArgumentParser(
        description='Combine text files in a directory into a single text and optionally PDF file.')
    parser.add_argument(
        'input_dir', help='Path to the directory containing the text files to be combined')
    parser.add_argument(
        '--output_txt', help='Path to the output text file default(output_text.txt)', default="output_text.txt")
    parser.add_argument(
        '--output_pdf', help='Path to the output PDF file (optional)', default=None)

    args = parser.parse_args()

    combine_text_files(args.input_dir, args.output_txt, args.output_pdf)


if __name__ == "__main__":
    main()
