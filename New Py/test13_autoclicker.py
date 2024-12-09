import time
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard_controller = KeyboardController()
mouse = MouseController()

# Global variable to track script state
script_running = False
click_interval = 1 / 12  # Delay for ~12 clicks per second (83 ms)
key_action_delay = 0.001  # Delay for 'a' and 'd' actions (1 ms)

def perform_actions():
    """
    Perform the series of actions defined in the script.
    Runs continuously while script_running is True.
    """
    global script_running
    keyboard_controller.press('s')  # Press and hold 's'
    time.sleep(0.005)  # Initial delay

    while script_running:
        # Press and release 'd', clicking 12 times with 83ms delay between clicks
        keyboard_controller.press('d')
        for _ in range(12):
            if not script_running:
                break
            mouse.click(Button.right)
            time.sleep(click_interval)  # 83ms between mouse clicks
        keyboard_controller.release('d')
        if not script_running:
            break
        time.sleep(key_action_delay)  # Delay between key actions

        # Press and release 'a', clicking 12 times with 83ms delay between clicks
        keyboard_controller.press('a')
        for _ in range(12):
            if not script_running:
                break
            mouse.click(Button.right)
            time.sleep(click_interval)  # 83ms between mouse clicks
        keyboard_controller.release('a')
        time.sleep(key_action_delay)  # Delay between key actions

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
        if key.char == 'j':  # Start the script
            if not script_running:
                script_running = True
                print("Script toggled ON.")
                perform_actions()
        elif key.char == 'k':  # Stop the script
            if script_running:
                script_running = False
                print("Script toggled OFF.")
    except AttributeError:
        # Ignore special keys
        pass

if __name__ == "__main__":
    print("Press 'j' to toggle the script ON. Press 'k' to toggle the script OFF. Use Ctrl+C to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

