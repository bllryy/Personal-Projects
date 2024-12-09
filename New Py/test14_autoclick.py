import time
import threading
from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# Controllers
keyboard_controller = KeyboardController()
mouse = MouseController()

# Global variable to track script state
script_running = False

# Timing constants
mouse_click_interval = 1 / 12  # 12 CPS = 83 ms
key_action_interval = 0.001   # 1 ms between key actions

def perform_actions():
    """
    Function to perform the actions while the script is running.
    """
    global script_running

    keyboard_controller.press('s')  # Press and hold 's'

    while script_running:
        # Perform 'd' actions
        keyboard_controller.press('d')
        for _ in range(key_action_interval):  # Click 12 times with 83ms delay
            if not script_running:
                break
            mouse.click(Button.right)
            time.sleep(mouse_click_interval)
        keyboard_controller.release('d')
        if not script_running:
            break
        time.sleep(key_action_interval)

        # Perform 'a' actions
        keyboard_controller.press('a')
        for _ in range(key_action_interval):  # Click 12 times with 83ms delay
            if not script_running:
                break
            mouse.click(Button.right)
            time.sleep(mouse_click_interval)
        keyboard_controller.release('a')
        if not script_running:
            break
        time.sleep(key_action_interval)

    # Release all keys when script stops
    keyboard_controller.release('s')
    keyboard_controller.release('d')
    keyboard_controller.release('a')
    print("Script stopped.")

def toggle_script(state):
    """
    Toggles the script ON or OFF based on the state.
    """
    global script_running
    script_running = state
    if script_running:
        print("Script started.")
        threading.Thread(target=perform_actions, daemon=True).start()
    else:
        print("Script stopped.")

def on_press(key):
    """
    Handles key presses for toggling the script.
    """
    try:
        if key.char == 'j':  # Start the script
            if not script_running:
                toggle_script(True)
        elif key.char == 'k':  # Stop the script
            if script_running:
                toggle_script(False)
    except AttributeError:
        # Ignore special keys
        pass

if __name__ == "__main__":
    print("Press 'j' to toggle the script ON. Press 'k' to toggle the script OFF. Use Ctrl+C to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

