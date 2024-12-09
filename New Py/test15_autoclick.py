import time
import threading
from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# Controllers
keyboard_controller = KeyboardController()
mouse = MouseController()

# Global variables to track script states
mouse_running = False
keyboard_running = False

# Timing constants
mouse_click_interval = 1 / 12  # 12 CPS = 83 ms
key_action_interval = 0.001   # 1 ms between key actions

def mouse_clicker():
    """
    Handles the mouse clicking action at a set interval.
    """
    global mouse_running
    while mouse_running:
        mouse.click(Button.right)
        time.sleep(mouse_click_interval)  # Delay between mouse clicks
    print("Mouse clicking stopped.")

def keyboard_actions():
    """
    Handles the keyboard actions: holding 's' and alternating 'a' and 'd'.
    """
    global keyboard_running
    keyboard_controller.press('s')  # Press and hold 's'

    while keyboard_running:
        # Perform 'd' action
        keyboard_controller.press('d')
        time.sleep(key_action_interval)  # Fast action
        keyboard_controller.release('d')

        # Perform 'a' action
        keyboard_controller.press('a')
        time.sleep(key_action_interval)  # Fast action
        keyboard_controller.release('a')

    # Release all keys when stopped
    keyboard_controller.release('s')
    keyboard_controller.release('d')
    keyboard_controller.release('a')
    print("Keyboard actions stopped.")

def toggle_mouse(state):
    """
    Toggles the mouse clicker ON or OFF.
    """
    global mouse_running
    mouse_running = state
    if mouse_running:
        print("Mouse clicker started.")
        threading.Thread(target=mouse_clicker, daemon=True).start()
    else:
        print("Mouse clicker stopped.")

def toggle_keyboard(state):
    """
    Toggles the keyboard actions ON or OFF.
    """
    global keyboard_running
    keyboard_running = state
    if keyboard_running:
        print("Keyboard actions started.")
        threading.Thread(target=keyboard_actions, daemon=True).start()
    else:
        print("Keyboard actions stopped.")

def on_press(key):
    """
    Handles key presses for toggling mouse and keyboard actions.
    """
    try:
        if key.char == 'j':  # Toggle mouse clicking
            toggle_mouse(not mouse_running)
        elif key.char == 'k':  # Toggle keyboard actions
            toggle_keyboard(not keyboard_running)
    except AttributeError:
        # Ignore special keys
        pass

if __name__ == "__main__":
    print("Press 'j' to toggle the mouse clicker ON/OFF. Press 'k' to toggle the keyboard actions ON/OFF. Use Ctrl+C to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

