import numpy as np
from PIL import ImageGrab
import cv2
import time
import pytesseract
from utils import *


def screen_record():
    last_time = time.time()
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    while (True):
        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox=(1680, 30, 1750, 60))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        gray = get_grayscale(np.array(cap))
        thresh = thresholding(gray)

        cv2.imshow('gray', gray)
        cv2.imshow('thresh', thresh)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.q
        tesstr_gray = pytesseract.image_to_string(gray, lang='eng',
                                                  config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(f"Gray: {tesstr_gray}")

        #The same but for thresholded
        #tesstr_thresh = pytesseract.image_to_string(thresh, lang='eng',
        #                                            config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
        #print(f"Thresh: {tesstr_thresh}")


        #time.sleep(0.8)

screen_record()
