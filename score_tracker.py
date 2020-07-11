import numpy as np
from PIL import ImageGrab
import cv2
import time
import pytesseract


def test():
    last_time = time.time()
    while (True):
        # 800x600 windowed mode
        printscreen = np.array(ImageGrab.grab(bbox=(1700, 0, 1920, 100)))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break



def screen_record():
    last_time = time.time()
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = "~/Desktop/pytesseract.py"
    while (True):
        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox=(1700, 0, 1920, 100))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        cv2.imshow('window', cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        print(tesstr)

    # Calling the function

screen_record()
