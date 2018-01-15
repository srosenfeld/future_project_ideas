import pyautogui as pg
import time
from PIL import Image

#First, make sure to save all images in the same folder.
#Next, use "Shift + right click" to find the filepath for those images.

image_1 = Image.open("C:\\Users\\srose\\Desktop\\zophie.png")
image_2 = Image.open("C:\\Users\\srose\\Desktop\\Capture8.PNG")

image_1.show()
answer = pg.prompt("""
What will you do next?
turn left
turn right
""")

if answer == "turn left":
    image_2.show()
    answer = pg.prompt("""
    What will you do next?
    turn left
    turn right
    """)
