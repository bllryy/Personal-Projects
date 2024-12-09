import time
from pynput.keyboard import Controller, Listener, Key
import threading

# Create a keyboard controller
keyboard_controller = Controller()

# Flag to indicate if the loop should run
is_running = False

# Function to simulate key presses for god bridging
def press_buttons():
    while is_running:
        keyboard_controller.press('w')
        time.sleep(0.05)
        keyboard_controller.release('s')
        time.sleep(0.05)
        keyboard_controller.press(Key.space)
        time.sleep(0.05)
        keyboard_controller.release(Key.space)
        time.sleep(0.05)
        keyboard_controller.release('w')
        time.sleep(0.05)

# Function to start the timer when 'V' is pressed
def start_pressing():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=press_buttons, daemon=True).start()

# Function to stop the timer when 'B' is pressed
def stop_pressing():
    global is_running
    is_running = False

# Define the hotkeys
def on_press(key):
    try:
        if key.char == 'v':
            start_pressing()
        elif key.char == 'b':
            stop_pressing()
    except AttributeError:
        pass

# Setup the listener for the hotkeys
with Listener(on_press=on_press) as listener:
    listener.join()

