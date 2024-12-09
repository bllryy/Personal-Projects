import time
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard_controller = KeyboardController()
mouse = MouseController()

# Global variable to track script state
script_running = False

def perform_actions():
    """
    Perform the series of actions defined in the script.
    """
    keyboard_controller.press('s')
    time.sleep(0.005)  # 5 ms delay

    while script_running:
        time.sleep(0.001)  # 1 ms delay

        # Perform 'D' action
        keyboard_controller.press('d')
        for _ in range(12):
            mouse.click(Button.right)
            time.sleep(0.001)  # 1 ms delay
        keyboard_controller.release('d')
        time.sleep(0.001)

        # Perform 'A' action
        keyboard_controller.press('a')
        for _ in range(12):
            mouse.click(Button.right)
            time.sleep(0.001)  # 1 ms delay
        keyboard_controller.release('a')

    # Release all keys when the script stops
    keyboard_controller.release('s')
    keyboard_controller.release('d')
    keyboard_controller.release('a')
    print("Script stopped.")

def on_press(key):
    """
    Toggle the script on and off with a specific key.
    """
    global script_running
    try:
        # Toggle the script with the 'j' key (replace 'j' with your desired key)
        if key.char == 'j':
            if script_running:
                script_running = False
                print("Script toggled OFF.")
            else:
                script_running = True
                print("Script toggled ON.")
                perform_actions()
    except AttributeError:
        # Handle special keys (if needed)
        pass

if __name__ == "__main__":
    print("Press 'j' to toggle the script ON/OFF. Use Ctrl+C to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


