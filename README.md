# Images  PDF Converter (Manga Version)

A tool script that converts images in sub-directories to one single PDF in the parent directory.

## Usage

The script takes in two arguments:

- `folder`: The path to the manga folder that contains the images.
- `-o, --output`: (optional) The name of the output pdf file. If not provided, the pdf file will be named after the manga folder.

## Functionality

1. The script first initializes an argument parser to handle the input arguments.
2. The script then initializes a pdf merger from the PyPDF2 library.
3. The script then changes the current working directory to the parent folder specified in the input argument.
4. The script then iterates through the subfolders in the parent folder, and for each subfolder, it converts all jpg and JPG images to pdf.
5. After all the images have been converted, the script iterates through the files in the parent folder and appends all pdf files to the pdf merger.
6. The script then writes the merged pdf to the parent folder with the specified output name or the name of the parent folder if no output name is provided.
7. The script then closes the pdf merger and deletes the individual chapter pdfs.

## Requirements

- Python 3
- PyPDF2
- PIL
- img2pdf
- send2trash

## Note

Make sure to install the required packages before running the script. Use command `pip install -r requirements.txt` to install all the packages at once if you have a requirements.txt file.