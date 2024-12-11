import time
from pynput import keyboard
from pynput  import Key, Controler as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard_controller = KeyboardController()
mouse = MouseController()

def preform_actions():
    global script_running
    



def on_press(key):
    global script_running
    try:
        if not script_running:
            if key.char == 'b':
            script running = True
        
