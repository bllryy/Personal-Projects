import pyautogui
import time

# Delay before starting the macro (so you can switch to Minecraft)
time.sleep(5)

# Start the macro: simulate pressing the mouse button to place blocks
def godbridge_macro():
    # Move the mouse to a starting position (adjust the coordinates as necessary)
    pyautogui.moveTo(1000, 500)  # Change coordinates to match your screen setup
    time.sleep(0.1)

    # Simulate pressing the 'right click' to place blocks
    for _ in range(100):  # Adjust the range for how long you want the macro to run
        pyautogui.click(button='right')  # Simulates right-clicking
        pyautogui.press('w')  # Move forward by pressing 'W'
        time.sleep(0.05)  # Adjust the delay for faster/slower bridge

godbridge_macro()

