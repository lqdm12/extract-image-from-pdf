import os
from pdf2image import convert_from_path
from cairosvg import svg2png
from PIL import Image
import io

def extract_images_from_pdf(pdf_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        # Convert PIL Image to PNG bytes
        png_image_io = io.BytesIO()
        image.save(png_image_io, format="PNG")
        png_image_data = png_image_io.getvalue()

        # Convert PNG to SVG
        svg_output_path = os.path.join(output_dir, f"page_{i + 1}.svg")
        with open(svg_output_path, "wb") as svg_file:
            cairosvg.svg2png(bytestring=png_image_data, write_to=svg_file)
            print(f"Saved: {svg_output_path}")

# Example usage
pdf_file = "QUIMICA-1.´df"  # Replace with your PDF file path
output_directory = "extracted_images"
extract_images_from_pdf(pdf_file, output_directory)
