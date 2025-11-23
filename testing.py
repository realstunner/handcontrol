import time
import pydirectinput # type: ignore

# Assign keys
left_pressed = "left"   # Brake
right_pressed = "right" # Gas

def PressKey(key):
    pydirectinput.keyDown(key)
    print(f"{key} pressed")  # For testing

def ReleaseKey(key):
    pydirectinput.keyUp(key)
    print(f"{key} released")  # For testing

# ====== TESTING ======
if __name__ == "__main__":
    print("Starting key press test in 3 seconds...")
    time.sleep(3)

    # Press left arrow for 2 seconds
    PressKey(left_pressed)
    time.sleep(2)
    ReleaseKey(left_pressed)

    # Pause
    time.sleep(1)

    # Press right arrow for 2 seconds
    PressKey(right_pressed)
    time.sleep(2)
    ReleaseKey(right_pressed)

    print("Test completed!")
