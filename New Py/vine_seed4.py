import pyautogui
import keyboard
import time

# Screen configuration (based on 1920x1080 resolution, GUI scale 4)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GUI_SCALE = 4

# Sleep duration between actions to prevent issues
CLICK_DELAY = 0.1

def setup_safety_features():
    pyautogui.FAILSAFE = True  # Move mouse to corner to stop
    pyautogui.PAUSE = 0.05     # Small delay between pyautogui actions

def loot_items():
    # Press E to open chest if needed
    keyboard.press_and_release('e')
    time.sleep(CLICK_DELAY)
    
    # Predefined slot positions for items
    # These coordinates are relative to chest GUI position
    slots = {
        'obsidian': [(710, 330), (746, 330), (782, 330)],  # Multiple obsidian slots
        'pickaxe': [(818, 330)],
        'flint': [(782, 366)],
        'iron': [(854, 330)]
    }
    
    # Loot each item type
    for item_type, positions in slots.items():
        for pos in positions:
            pyautogui.moveTo(pos[0], pos[1], duration=0.1)
            pyautogui.click()
            time.sleep(CLICK_DELAY)
    
    # Close chest
    keyboard.press_and_release('esc')
    time.sleep(CLICK_DELAY)

def main():
    setup_safety_features()
    print("Auto-looting script started!")
    print("Press 't' to toggle script, 'q' to quit")
    
    running = False
    while True:
        if keyboard.is_pressed('q'):
            print("Script terminated.")
            break
            
        if keyboard.is_pressed('t'):
            running = not running
            print(f"Script {'activated' if running else 'deactivated'}!")
            time.sleep(0.5)  # Prevent multiple toggles
            
        if running:
            loot_items()
            time.sleep(1)  # Delay between chest looting attempts

if __name__ == "__main__":
    main()
