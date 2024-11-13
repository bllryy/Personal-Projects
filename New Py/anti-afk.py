from pynput.mouse import Controller

mouse = Controller()

start_position = mouse.position

# Move the cursor back by 1 pixel
mouse.move(-1, 0)  # Move left by 1 pixel
time.sleep(1.0)    # Optional: wait a little before moving back

# Move the cursor back to the starting position
mouse.position = start_position