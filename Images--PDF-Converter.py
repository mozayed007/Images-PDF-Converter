import argparse
from PyPDF2 import PdfFileMerger
import os
import re
from PIL import Image
import img2pdf
from send2trash import send2trash

# Initialize the arguement parser
parser = argparse.ArgumentParser(description='Merge and convert manga images to pdf')

# Add the folder path arguement
parser.add_argument('folder', type=str, help='Path to the manga folder')

# Add the output pdf file name arguement
parser.add_argument('-o', '--output', type=str, help='Name of the output pdf file')

# Parse the arguements
args = parser.parse_args()

# Initialize the pdf merger
merger = PdfFileMerger()

# Get the parent folder path
parent_folder = args.folder

# Change the current working directory to the parent folder
os.chdir(parent_folder)


# Iterate through the subfolders in the parent folder
for subfolder in os.listdir(parent_folder):
    if os.path.isdir(subfolder):
        for filename in os.listdir(subfolder):
            if filename.endswith(('.jpg', '.JPG', '.png', '.PNG', '.jpeg', '.JPEG', '.gif', '.GIF')):
                filename_regex = re.compile(r'(\.jpg)|(\.jpeg)|(\.png)|(\.gif)', re.IGNORECASE)
                new_name = filename_regex.sub('', filename)
                image = Image.open(f"{subfolder}/{filename}")
                pdf_bytes = img2pdf.convert(image.filename)
                pdf_path = f"{subfolder}/{new_name}.pdf"
                with open(pdf_path, 'wb') as pdf_file:
                    pdf_file.write(pdf_bytes)
                print(f"Converted {filename} to {pdf_path}")
                
                
# Iterate through the files in the parent folder
for file in os.listdir(parent_folder ): 
    if file.endswith('.pdf'):
        print(f"Merging file {file}")
        merger.append(file)   
        
# Get the name of the parent folder
manga = os.path.basename(os.path.normpath(parent_folder))

# Write the merged PDF to the parent folder
if args.output:
    output_path = f"{parent_folder}/{args.output}.pdf"
else:
    output_path = f"{parent_folder}/{manga}.pdf"

merger.write(output_path)

# Close the PDF merger
merger.close()

# Iterate through the files in the parent folder
for file in os.listdir(parent_folder ): 
    if file.endswith('.pdf')and file != output_path: 
        send2trash(file)
        print(f"Deleting file {file}")
print('Done.')        