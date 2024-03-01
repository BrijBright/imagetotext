# Image to Text Extraction Tool

This Python script provides a simple graphical user interface (GUI) application for extracting text from images displayed on the screen. It utilizes the Tesseract OCR (Optical Character Recognition) engine to recognize text within screenshots.

## Features

- Capture screenshots of specific regions or the entire screen.
- Extract text from the captured screenshots using Tesseract OCR.
- Display the extracted text in a text box within the GUI.
- Provides a keyboard shortcut ("Alt + Z") to trigger text extraction.
- Option to initiate full mode extraction for capturing text from the entire screen.

## Requirements

- Python 3.x
- `pynput` library: Install using `pip install pynput`
- `PIL` library: Install using `pip install Pillow`
- `pytesseract` library: Install using `pip install pytesseract`
- Tesseract OCR Engine: Download and install from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Usage

1. Install the required dependencies mentioned above.
2. Ensure that Tesseract OCR is installed and the path to the executable is correctly specified in the script (`pytesseract.pytesseract.tesseract_cmd`).
3. Run the script using Python (`python image_to_text.py`).
4. The GUI window will appear, displaying a text box.
5. Press "Alt + Z" keyboard combination to trigger text extraction from the screen.
6. Extracted text will be displayed in the text box.
7. Use the "ADD MORE" button to initiate text extraction from a specific region of the screen.
8. Use the "fullmode" button to initiate text extraction from the entire screen.

## Customization

- Modify the keyboard shortcut by changing the key combination in the `on_press` function (`on_press(key)`).
- Adjust the GUI layout or styling by modifying the Tkinter widgets and their properties.
- Extend the functionality by adding features such as saving extracted text to a file, implementing image preprocessing, or integrating with other services.


