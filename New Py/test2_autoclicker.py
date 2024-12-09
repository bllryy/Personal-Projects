import time
import keyboard
import threading

# Flag to indicate if the loop should run
is_running = False

# Function to simulate key presses for god bridging
def press_buttons():
    while is_running:
        keyboard.press('w')
        time.sleep(0.05)
        keyboard.release('s')
        time.sleep(0.05)
        keyboard.press('space')
        time.sleep(0.05)
        keyboard.release('space')
        time.sleep(0.05)
        keyboard.release('w')
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

# Bind the hotkeys to start and stop the pressing function
keyboard.add_hotkey('v', start_pressing)
keyboard.add_hotkey('b', stop_pressing)

# Keep the program running
keyboard.wait()

