import time
from pynput.keyboard import Key, Controller as KeyboardController, Listener as KeyboardListener
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

def main_script():
    continue_loop = True
    time.sleep(0.005)  # 5 ms delay
    keyboard.press('s')
    
    try:
        while True:
            time.sleep(0.001)  # 1 ms delay
            
            # Check if 'j' is no longer pressed
            if not is_key_pressed('j'):
                keyboard.release('s')
                break

            # Perform actions
            keyboard.press('d')
            for _ in range(12):
                mouse.click(Button.right)
                time.sleep(0.001)  # 1 ms delay
            keyboard.release('d')
            time.sleep(0.001)

            keyboard.press('a')
            for _ in range(12):
                mouse.click(Button.right)
                time.sleep(0.001)  # 1 ms delay
            keyboard.release('a')
    finally:
        keyboard.release('s')
        keyboard.release('d')
        keyboard.release('a')

def is_key_pressed(key_char):
    """
    Check if a specific key is pressed.
    """
    from pynput.keyboard import KeyCode
    try:
        with KeyboardListener(on_press=None, on_release=None) as listener:
            return listener.is_pressed(KeyCode.from_char(key_char))
    except:
        return False

def reload_script():
    print("Reloading script...")
    # This would involve restarting the script. Add code to handle this as necessary.

def exit_script():
    print("Exiting script...")
    exit()

# Map keys to actions
key_actions = {
    "^j": main_script,
    "^r": reload_script,
    "^p": exit_script
}

def key_event_handler(key):
    try:
        if key in key_actions:
            key_actions[key]()
    except Exception as e:
        print(f"Error handling key event: {e}")

# Main listener for key events
def listen_for_keys():
    with KeyboardListener(on_press=lambda key: key_event_handler(key)) as listener:
        listener.join()

if __name__ == "__main__":
    print("Script running. Use '^j' to start, '^r' to reload, and '^p' to exit.")
    listen_for_keys()

