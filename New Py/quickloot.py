import keyboard
import pyautogui
import time

def setup_safety():
    pyautogui.FAILSAFE = True  # Move mouse to corner to stop script
    pyautogui.PAUSE = 0.02     # Minimal delay between actions

def perform_action():
    # Hold Shift
    keyboard.press('shift')
    
    # First Shift + Left Click
    pyautogui.click(button='left')
    
    # Release Shift for the next action
    keyboard.release('shift')
    
    # Press V key
    keyboard.press('v')
    keyboard.release('v')
    
    # Hold Shift again for second Left Click
    keyboard.press('shift')
    pyautogui.click(button='left')  # Second Left Click
    keyboard.release('shift')
    
    pyautogui.click(button='left')
    keyboard.press('shift')
    keyboard.release('shift')


    keyboard.press('shift')
    pyautogui.click(button='right')
    keyboard.release('shift')

    # Small delay to prevent repeated triggers too quickly
    time.sleep(0.1)

def main():
    setup_safety()
    print("Script started! Press 'T' to trigger action, 'm' to quit")
    
    while True:
        if keyboard.is_pressed('m'):
            print("Script terminated.")
            break  # Exit the script when 'm' is pressed
        
        if keyboard.is_pressed('t'):
            perform_action()  # Trigger action when 'T' is pressed

if __name__ == "__main__":
    main()
