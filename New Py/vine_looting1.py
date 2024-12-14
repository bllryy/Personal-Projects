import pyautogui
import time

# Chest GUI configuration
SCREEN_RESOLUTION = (1920, 1080)
GUI_SCALE = 2
SLOT_SIZE = 36  # Each slot is 36x36 pixels at GUI scale 2
CHEST_TOP_LEFT = (710, 330)  # Replace with the top-left corner of the chest GUI

# Function to calculate the pixel position of a slot
def get_slot_position(row, col):
    x = CHEST_TOP_LEFT[0] + col * SLOT_SIZE
    y = CHEST_TOP_LEFT[1] + row * SLOT_SIZE
    return (x, y)

# Looting specific items based on slot indices
def loot_chest():
    # Slots to loot (row, column) - adjust based on chest layout
    obsidian_slots = [(0, 0), (0, 1), (0, 2)]  # Top row, first 3 slots
    pickaxe_slot = (0, 3)  # Top row, 4th slot
    flint_slot = (1, 2)  # Second row, 3rd slot
    iron_slot = (0, 4)  # Top row, 5th slot (just one iron ingot)

    # Loot obsidian
    for slot in obsidian_slots:
        pyautogui.moveTo(*get_slot_position(*slot))
        pyautogui.click()
        time.sleep(0.1)

    # Loot pickaxe
    pyautogui.moveTo(*get_slot_position(*pickaxe_slot))
    pyautogui.click()
    time.sleep(0.1)

    # Loot flint
    pyautogui.moveTo(*get_slot_position(*flint_slot))
    pyautogui.click()
    time.sleep(0.1)

    # Loot one iron ingot
    pyautogui.moveTo(*get_slot_position(*iron_slot))
    pyautogui.click()
    time.sleep(0.1)

# Run the macro
loot_chest()

