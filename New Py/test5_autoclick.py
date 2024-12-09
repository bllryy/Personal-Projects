import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

def main_script():
    print("Script started. Press Ctrl+C to stop.")
    try:
        keyboard.press('s')
        time.sleep(0.005)  # 5 ms delay
        
        while True:
            time.sleep(0.001)  # 1 ms delay
            
            # Perform 'D' action
            keyboard.press('d')
            for _ in range(12):
                mouse.click(Button.right)
                time.sleep(0.001)  # 1 ms delay
            keyboard.release('d')
            time.sleep(0.001)

            # Perform 'A' action
            keyboard.press('a')
            for _ in range(12):
                mouse.click(Button.right)
                time.sleep(0.001)  # 1 ms delay
            keyboard.release('a')
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    finally:
        keyboard.release('s')
        keyboard.release('d')
        keyboard.release('a')

if __name__ == "__main__":
    main_script()

