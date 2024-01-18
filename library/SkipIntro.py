import pyautogui
import time
import numpy as np
from PIL import ImageGrab
import pytesseract
import re

first_skip = True
def default_skip_intro(x, y):
    global first_skip 
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)
    if (first_skip == True):
        time.sleep(1)
        pyautogui.press('space')
        first_skip = False

def find_title_card(start_x, start_y, end_x, duration, title_card):
    title_card_seconds = title_card_to_seconds(title_card)
    print("title card in seconds: " + str(title_card_seconds))
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hergo\AppData\Local\Programs\Tesseract-OCR\Tesseract'
    pyautogui.moveTo(start_x, start_y)
    last_valid_time = 240
    current_x = start_x
    while current_x < end_x:
        pyautogui.moveTo(current_x + 2, start_y,.1)
        timestampImage = np.array(ImageGrab.grab(bbox=(current_x - 70, start_y - 60, current_x + 70, start_y + 20)))
        image_text = pytesseract.image_to_string(timestampImage)
        current_time = image_text_to_seconds(image_text, last_valid_time)
        time_difference = title_card_seconds - current_time
        if time_difference <= 0 and time_difference >= -5:
            print('---------CLOSE-ENOUGH------------')
            print('current time: ' + str(current_time))
            print('start time: ' + str(title_card_seconds))
            print('difference: ' + str(time_difference))
            print('------------------------------')
            pyautogui.click(current_x, start_y)
            return
        else:
            print('------------------------------')
            print('current time: ' + str(current_time))
            print('start time: ' + str(title_card_seconds))
            print('difference: ' + str(time_difference))
            print('------------------------------')
            last_valid_time = current_time
            current_x += time_difference
        # elif time_difference > 25:
        #     current_x += 25 
        # elif time_difference > 15:
        #     current_x += 15
        # elif time_difference > 10:
        #     current_x += 5
        # elif time_difference < -20:
        #     current_x -= 25
        # elif time_difference < -10:
        #     current_x -= 15
        # else:
        #     current_x += 1

    pyautogui.click(start_x, start_y)
    return

def image_text_to_seconds(image_text, last_valid_time):
    string_number = re.sub(r"[^0-9]", "", image_text)
    print('------------------------------')
    print('image text: ' + str(image_text))
    print('string number: ' + str(string_number))
    print('------------------------------')
    if(len(string_number) < 3):
        return last_valid_time
    elif(len(string_number) == 3):
        minutes = int(string_number[0]) * 60
        seconds = int(string_number[1] + string_number[2])
        return minutes + seconds
    elif(len(string_number) == 3):
        minutes = int(string_number[0] + string_number[1]) * 60
        seconds = int(string_number[2] + string_number[3])
        return minutes + seconds
    return last_valid_time

def title_card_to_seconds(title_card):
    print(title_card)
    string_number = re.sub(r"[^0-9]", "", title_card)
    if(len(string_number) == 3):
        minutes = int(string_number[0]) * 60
        print("Time Card Minutes in seconds: " + str(minutes))
        seconds = int(string_number[1] + string_number[2])
        print("Time Card Seconds in seconds: " + str(seconds))
        return minutes + seconds
    elif(len(string_number) == 4):
        minutes = int(string_number[0] + string_number[1]) * 60
        seconds = int(string_number[2] + string_number[3])
        return minutes + seconds
    print('DID NOT GET TITLE CARD')
    return 0