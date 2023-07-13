import pyautogui
from PIL import Image
import pyperclip

def get_hex_color():
    # Get the current position of the mouse
    x, y = pyautogui.position()

    # Capture a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Get the RGB values of the pixel at the given position
    pixel_rgb = screenshot.getpixel((x, y))

    # Convert the RGB values to hexadecimal format
    hex_color = '#{:02x}{:02x}{:02x}'.format(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2])

    return hex_color

# Example usage
color = get_hex_color()
pyperclip.copy(color)
print("Pixel color:", color, "(copied to clipboard)")
