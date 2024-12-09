from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button
import time

keyboard = KeyboardController()
mouse = MouseController()

def breezily_bridge():
    """
    Simulates breezily bridging in Minecraft.
    The player must position the crosshair correctly before running the macro.
    """
    try:
        while True:
            # Simulate backward movement ('s' key down)
            keyboard.press('s')
            time.sleep(0.0001)

            # Alternate between strafing left and right while right-clicking
            keyboard.press('d')  # Strafe right
            for _ in range(12):
                mouse.click(Button.right)  # Simulate placing blocks
                time.sleep(0.03)  # Adjust timing as needed # was 0.05
            keyboard.release('d')

            time.sleep(0.1)

            keyboard.press('a')  # Strafe left
            for _ in range(12):
                mouse.click(Button.right)
                time.sleep(0.01)  # Adjust timing as needed # was 0.05
            keyboard.release('a')

            # Pause backward movement for a moment
            keyboard.release('s')
            time.sleep(0.01)

    except KeyboardInterrupt:
        # Release all keys if interrupted
        keyboard.release('s')
        keyboard.release('d')
        keyboard.release('a')
        print("\nMacro stopped.")

# Run the macro
print("Position yourself in Minecraft and press Ctrl+C to stop the macro.")
time.sleep(3)
breezily_bridge()

