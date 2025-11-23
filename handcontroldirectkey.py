# handcontroldirectkey.py
import pydirectinput
import time

# Assign keys
LEFT_KEY = "left"   # Brake
RIGHT_KEY = "right" # Gas

def PressKey(key: str):
    """Hold down a key"""
    pydirectinput.keyDown(key)
    print(f"{key} pressed")

def ReleaseKey(key: str):
    """Release a key"""
    pydirectinput.keyUp(key)
    print(f"{key} released")

# ====== TESTING ======
if __name__ == "__main__":
    print("Testing pydirectinput keys in 3 seconds...")
    time.sleep(3)

    # Press and hold left arrow
    PressKey(LEFT_KEY)
    time.sleep(2)
    ReleaseKey(LEFT_KEY)

    time.sleep(1)

    # Press and hold right arrow
    PressKey(RIGHT_KEY)
    time.sleep(2)
    ReleaseKey(RIGHT_KEY)

    print("✅ Test completed!")
