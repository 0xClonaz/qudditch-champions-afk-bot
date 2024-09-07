import cv2
import pytesseract
import pyautogui
import time
import numpy as np
import pygetwindow as gw
import keyboard

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

# Set the path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load template images
continue_template = cv2.imread('continue_button.png', cv2.IMREAD_GRAYSCALE)
change_position_template = cv2.imread('change_position.png', cv2.IMREAD_GRAYSCALE)
keeper_template = cv2.imread('keeper.png', cv2.IMREAD_GRAYSCALE)
next_item_template = cv2.imread('next_item.png', cv2.IMREAD_GRAYSCALE)

# Variables to count games and experience
games_played = 0
experience_points = 0

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def check_text_on_screen(text_to_find):
    screenshot = capture_screen()
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    result = pytesseract.image_to_string(thresh, config='--psm 6')
    return text_to_find.lower() in result.lower()

def click_button(template):
    screenshot = capture_screen()
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = 0.9
    if max_val >= threshold:
        match_x, match_y = max_loc
        w, h = template.shape[::-1]
        center_x = match_x + w // 2
        center_y = match_y + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.1)
        pyautogui.click(center_x, center_y)
        return True
    return False

def bring_window_to_front(window_title):
    try:
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            window = windows[0]
            window.activate()  # Bring window to the front
            time.sleep(1)  # Ensure the window is focused
        else:
            print(f"Window with title '{window_title}' not found.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    if keyboard.is_pressed('esc'):
        break
    
    bring_window_to_front("Harry Potter: Quidditch Champions")
    
    if check_text_on_screen("Play Again"):
        pyautogui.press("space")
        time.sleep(1)
        
        change_position_found = False
        while not change_position_found:
            if click_button(change_position_template):
                pyautogui.press("r")
                pyautogui.press("3")
                change_position_found = True
                time.sleep(1)
            else:
                time.sleep(3)
        
        games_played += 1
        experience_points += 100
        print(f"Games played: {games_played}, EXP: {experience_points}")

    # Check for "Next Item" button
    if click_button(next_item_template):
        time.sleep(1)
    else:
        # If "Next Item" button is not detected, move to direct coordinate click
        if check_text_on_screen("Next Item"):
            pyautogui.moveTo(1470, 750, duration=0.1) #SET Next item button here
            pyautogui.click()
            time.sleep(1)

    # Check for Continue button
    if click_button(continue_template):
        time.sleep(1)
    else:
        # If Continue button is not detected, move to direct coordinate click
        if check_text_on_screen("Continue"):
            pyautogui.moveTo(1750, 1005, duration=0.1)#SET Continue button here
            pyautogui.click()
            time.sleep(1)

    time.sleep(1)
