import pyautogui
import keyboard
import time

# Configuration
pyautogui.FAILSAFE = True  # Move mouse to corner to stop script
pyautogui.PAUSE = 0.02     # Built-in delay between actions

def perform_sequence():
    # Press 'E'
    keyboard.press_and_release('e')
    time.sleep(0.05)  # 50ms sleep
    
    # Move to first position
    pyautogui.moveTo(1016, 437, duration=0)
    time.sleep(0.02)
    
    # Press 'C'
    keyboard.press_and_release('c')
    time.sleep(0.02)
    
    # Move to second position
    pyautogui.moveTo(1087, 412, duration=0)
    time.sleep(0.02)
    
    # Press 'V'
    keyboard.press_and_release('v')
    time.sleep(0.02)
    
    # Move to third position
    pyautogui.moveTo(1192, 412, duration=0)
    time.sleep(0.02)
    
    # Shift-click
    keyboard.press('shift')
    pyautogui.click()
    keyboard.release('shift')
    time.sleep(0.02)
    
    # Press Escape
    keyboard.press_and_release('esc')

def main():
    print("Script started. Press 'G' to trigger the sequence, 'Q' to quit.")
    
    while True:
        if keyboard.is_pressed('q'):  # Exit condition
            print("Script terminated.")
            break
            
        if keyboard.is_pressed('g'):  # Trigger key
            perform_sequence()
            time.sleep(0.1)  # Prevent multiple triggers

if __name__ == "__main__":
    main()