

```markdown
# PDF Image Extractor

PDF Image Extractor is a Python script designed to extract images from PDF files and convert them into SVG format. This tool is ideal for users who need to transform PDF content into image formats for further editing or other applications.

## Features

- Extracts images from each page of a PDF file.
- Converts extracted images into SVG format.
- Saves the converted images in a specified output directory.

## Requirements

To run this script, the following Python packages need to be installed:

- `pdf2image`: Converts PDF pages to images.
- `cairosvg`: Converts PNG images to SVG format.
- `Pillow`: Handles image files.

You can install these packages using pip:

```bash
pip install pdf2image cairosvg Pillow
```

Additionally, **Poppler** is required for the `pdf2image` library to function correctly. Install it on Ubuntu with:

```bash
sudo apt-get install poppler-utils
```

## Usage

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Place your PDF file** in the project directory or specify the path in the script.

3. **Edit the script** as necessary:
   - Update the `pdf_file` variable with the path to your PDF file.
   - Update the `output_directory` variable with your desired output directory name.

4. **Run the script**:
   ```bash
   python your_script_name.py
   ```

### Example

Here’s an example of how to set up and run the script:

```python
pdf_file = "QUIMICA-1.pdf"  # Replace with your PDF file path
output_directory = "extracted_images"
extract_images_from_pdf(pdf_file, output_directory)
```

### Output

The extracted images will be saved in the specified output directory as SVG files named `page_1.svg`, `page_2.svg`, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue with any suggestions or improvements.

## Acknowledgments

- This project uses [pdf2image](https://github.com/Belval/pdf2image) for converting PDFs to images.
- Thanks to [CairoSVG](https://cairosvg.org/) for providing an easy way to convert images to SVG format.
```
