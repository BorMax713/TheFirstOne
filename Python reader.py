import pytesseract
from PIL import Image
import pyautogui

# Configure pytesseract path (if necessary)
# For Windows, add the path to Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen_and_read_text():
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot (optional)
    screenshot.save("screenshot.png")

    # Convert the screenshot to text using pytesseract
    text = pytesseract.image_to_string(screenshot)

    # Write the text to a file
    with open("output_text.txt", "w") as f:
        f.write(text)

    print("Text written to output_text.txt")

# Call the function
capture_screen_and_read_text()
