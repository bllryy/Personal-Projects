from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button
import time

class MinecraftMacro:
    def __init__(self):
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        self.running = False  # Control the macro state

    def breezily_bridge(self, duration=10, delay=0.1, strafe_delay=0.5):
        """
        Perform a Minecraft breezily bridge macro with A and D strafing.
        
        :param duration: How long (in seconds) the macro will run.
        :param delay: Delay between block placements (in seconds).
        :param strafe_delay: How often (in seconds) to switch between A and D.
        """
        print("Starting breezily bridge macro...")
        self.running = True
        start_time = time.time()
        strafe_left = True  # Start by strafing left (A key)

        try:
            while self.running and (time.time() - start_time < duration):
                # Hold the "S" key to move backward
                self.keyboard.press('s')

                # Strafe alternately with "A" and "D"
                if strafe_left:
                    self.keyboard.press('a')
                    time.sleep(strafe_delay)  # Hold "A" for a bit
                    self.keyboard.release('a')
                else:
                    self.keyboard.press('d')
                    time.sleep(strafe_delay)  # Hold "D" for a bit
                    self.keyboard.release('d')

                strafe_left = not strafe_left  # Toggle strafe direction

                # Simulate right mouse button press (placing block)
                self.mouse.press(Button.right)
                time.sleep(delay)
                self.mouse.release(Button.right)

                # Small delay to ensure smooth placement
                time.sleep(delay)

        except KeyboardInterrupt:
            print("Macro stopped manually.")

        finally:
            # Ensure keys are released after the macro ends
            self.keyboard.release('s')
            self.keyboard.release('a')
            self.keyboard.release('d')
            print("Breezily bridge macro stopped.")

    def stop(self):
        """Stop the macro manually."""
        self.running = False

# Example usage
if __name__ == "__main__":
    macro = MinecraftMacro()

    # Run the macro for 10 seconds with 0.1-second block placement delay
    # and 0.5-second strafe delay
    macro.breezily_bridge(duration=10, delay=0.1, strafe_delay=0.5)

