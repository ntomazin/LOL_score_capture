import pytesseract
import cv2
from utils import *
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


img = cv2.imread("test_pictures\\test2.jpg")

#croping
crop_img = img[0:100, 1000:1200]

gray = get_grayscale(crop_img)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)
erode = erode(crop_img)
dilate = dilate(crop_img)
no_noise = remove_noise(crop_img)

#cv2.imshow('gray', gray)
#cv2.imshow('thresh', thresh)
#cv2.imshow('opening', opening)
#cv2.imshow('canny', canny)

cv2.waitKey(0)


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#print(pytesseract.image_to_string(gray))
#print(pytesseract.image_to_string(thresh))
#print(pytesseract.image_to_string(opening))
#print(pytesseract.image_to_string(canny))

box_chars(crop_img)
box_chars(gray)
box_chars(canny)
#box_chars(opening)
box_chars(thresh)
#box_chars(dilate)
#box_chars(no_noise)
#box_chars(erode)


#d = pytesseract.image_to_data(gray, output_type=Output.DICT)
#print(d.keys())
#custom_config = r'--oem 3 --psm 6 outputbase digits'
#print(pytesseract.image_to_string(img, config=custom_config))
#print(pytesseract.image_to_string(gray, config=custom_config))


#box_words(gray, d)