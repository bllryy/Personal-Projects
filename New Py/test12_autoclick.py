import time
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard_controller = KeyboardController()
mouse = MouseController()

# Global variable to track script state
script_running = False
click_interval = 1 / 12  # Delay for ~12 clicks per second (83 ms)
key_delay = 0.001  # Delay for 'a' and 'd' actions (1 ms)

def perform_actions():
    """
    Perform the series of actions defined in the script.
    Checks the global `script_running` flag to stop when toggled off.
    """
    global script_running
    keyboard_controller.press('s')
    time.sleep(0.005)  # 5 ms delay

    while script_running:  # Check if the script is still running
        time.sleep(0.001)  # Minimal delay to keep the loop responsive

        # Perform 'D' action
        keyboard_controller.press('d')
        for _ in range(12):
            if not script_running:
                break
            mouse.click(Button.right)
            time.sleep(click_interval)  # 12 clicks per second (83 ms delay)
        keyboard_controller.release('d')
        if not script_running:
            break
        time.sleep(key_delay)  # 1 ms delay for 'd'

        # Perform 'A' action
        keyboard_controller.press('a')
        for _ in range(12):
            if not script_running:
                break
            mouse.click(Button.right)
            time.sleep(click_interval)  # 12 clicks per second (83 ms delay)
        keyboard_controller.release('a')
        time.sleep(key_delay)  # 1 ms delay for 'a'

    # Release all keys when the script stops
    keyboard_controller.release('s')
    keyboard_controller.release('d')
    keyboard_controller.release('a')
    print("Script stopped.")

def on_press(key):
    """
    Toggle the script on and off with specific keybinds.
    """
    global script_running
    try:
        if key.char == 'j':  # Keybind to toggle the script ON
            if not script_running:
                script_running = True
                print("Script toggled ON.")
                perform_actions()
        elif key.char == 'k':  # Keybind to toggle the script OFF
            if script_running:
                script_running = False
                print("Script toggled OFF.")
    except AttributeError:
        # Handle special keys (if needed)
        pass

if __name__ == "__main__":
    print("Press 'j' to toggle the script ON. Press 'k' to toggle the script OFF. Use Ctrl+C to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

