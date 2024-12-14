import pyautogui
import time

def loot_chest():
    # Assuming the chest is already open
    # Adjust these values based on the positions of items in the chest grid
    
    # Coordinates for the specific items (to be determined with screen recording tools)
    obsidian_slots = [(100, 200), (150, 200), (200, 200)]  # Replace with actual coordinates
    pickaxe_slot = (50, 150)  # Replace with actual coordinates
    flint_slot = (200, 250)  # Replace with actual coordinates
    iron_slot = (150, 150)   # Replace with actual coordinates

    # Loot obsidian
    for slot in obsidian_slots:
        pyautogui.moveTo(slot[0], slot[1])
        pyautogui.click()
        time.sleep(0.1)  # Add a small delay to ensure smooth operation

    # Loot pickaxe
    pyautogui.moveTo(pickaxe_slot[0], pickaxe_slot[1])
    pyautogui.click()
    time.sleep(0.1)

    # Loot flint
    pyautogui.moveTo(flint_slot[0], flint_slot[1])
    pyautogui.click()
    time.sleep(0.1)

    # Loot one iron ingot
    pyautogui.moveTo(iron_slot[0], iron_slot[1])
    pyautogui.click()
    time.sleep(0.1)

# Run the macro
loot_chest()

