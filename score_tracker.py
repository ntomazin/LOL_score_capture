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
        cap = ImageGrab.grab(bbox=(1680, 32, 1750, 60))
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        #resizing image
        img = cv2.resize(np.array(cap), None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
        gray = get_grayscale(np.array(img))
        thresh = thresholding(gray)
        thresh_inv = thresholding_inv(gray)
        #a_thresh = adaptive_thresholding_gaussian(gray)
        #a_thresh_m = adaptive_thresholding_mean(gray)

        cv2.imshow('gray', gray)
        #cv2.imshow('thresh', thresh)
        cv2.imshow('thresh_inv', thresh_inv)

        #cv2.imshow('thresh2', a_thresh_m)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.q
        tesstr_thresh = pytesseract.image_to_string(thresh_inv, lang='eng',
                                                  config='--psm 7 --oem 3')
        print(f"Thresh inv: {tesstr_thresh}")


screen_record()
