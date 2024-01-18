import pyautogui
import os
import time
import cv2
from PIL import ImageGrab
import numpy as np
import time


save_folder = "screenshots"

# Continuously take screenshots and measure speed
def continuously_take_screenshots(template_path, click_x, click_y):
    timings = []
    try:
        while True:
            screenshot_path = take_screenshot(save_folder, timings)
            if find_image(template_path, screenshot_path):
                print("Image recognized! Clicking...")
                click_at_coordinates(click_x, click_y)
                print("Clicked!")
                return True
    except KeyboardInterrupt:
        total_time = sum(timings)
        num_screenshots = len(timings)
        if num_screenshots > 0:
            avg_speed = total_time / num_screenshots
            print(f"\nAverage screenshot speed: {avg_speed:.2f} seconds per screenshot")
        else:
            print("\nNo screenshots taken.")
        print("Stopped.")

def continuously_grab_images(template_path, click_x, click_y):
    last_time = time.time()
    while True:
        screen = np.array(ImageGrab.grab(bbox=(1024,203,1698,1067)))
        if find_image(template_path, screen):
                print("Image recognized! Clicking...")
                click_at_coordinates(click_x, click_y)
                print("Clicked!")
                return True
        print("Loop took {} seconds".format(time.time() - last_time))
        last_time = time.time()
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
            
# Click at specified coordinates
def click_at_coordinates(x, y):
    print(x, y)
    print(f"Clicking at coordinates: ({x}, {y})")
    click_coordinates(x, y)

def find_image(template_path, screen):
    template = cv2.imread(template_path)
    grey_template = cv2.cvtColor(template, 6)
    grey_screen = cv2.cvtColor(screen, 6)

    result = cv2.matchTemplate(grey_screen, grey_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.6  # Adjust this threshold as needed
    print("Max Value for Recongition: " + str(max_val))
    if max_val >= threshold:
        return True  # Image found
    return False

# Move the mouse to specific coordinates and click
def click_coordinates(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)

# Take a screenshot at the current mouse position and save to a folder
def take_screenshot(folder_path, timings):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    start_time = time.time()
    screenshot = pyautogui.screenshot(region=(824,243,1498,1047))
    end_time = time.time()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    screenshot_path = os.path.join(folder_path, f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_path)
    time_taken = end_time - start_time
    timings.append(time_taken)
    print(f"Screenshot saved: {screenshot_path}")
    return screenshot_path