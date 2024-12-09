import time
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard_controller = KeyboardController()
mouse = MouseController()

def main_script():
    print("Script started. Press your keybind again to stop.")
    try:
        keyboard_controller.press('s')
        time.sleep(0.005)  # 5 ms delay

        while True:
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
    except StopExecution:
        print("\nScript stopped.")
    finally:
        keyboard_controller.release('s')
        keyboard_controller.release('d')
        keyboard_controller.release('a')

class StopExecution(Exception):
    """Custom exception to stop the script."""
    pass

# To toggle the script on and off
script_running = False

def on_press(key):
    global script_running
    try:
        # Define the key to trigger the script
        if key.char == 'j':  # Change 'j' to any other key if you prefer
            if not script_running:
                script_running = True
                main_script()
            else:
                raise StopExecution()
    except AttributeError:
        # Handle special keys if needed
        pass

if __name__ == "__main__":
    print("Press 'j' to start/stop the script. Use Ctrl+C to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

