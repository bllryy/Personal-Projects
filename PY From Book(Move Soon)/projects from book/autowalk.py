import pyautogui
import keyboard

def hold_mouse_and_walk():
    # Press down the left mouse button (Mouse 1)
    pyautogui.mouseDown(button='left')
    
    # Press down the 'W' key to walk forward
    pyautogui.keyDown('w')

    print("Holding Mouse 1 and walking forward. Press 'q' to stop.")

    # Wait until the 'q' key is pressed to stop the action
    keyboard.wait('q')
    
    # Release the left mouse button and the 'W' key
    pyautogui.mouseUp(button='left')
    pyautogui.keyUp('w')
