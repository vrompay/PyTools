# Imports
from pynput.mouse import Button, Controller
import time, os

# Variables
mouse = Controller()
x = 0
counter = 0

# Inputs
wait = int(input("Wait time between clicks (1 second = 1000): ")) / 1000

# Sleep before app
time.sleep(int(input("Time to wait before starting (1 second = 1000): ")) / 1000)

# Functions

while x == 0:
	mouse.press(Button.left)
	mouse.release(Button.left)
	time.sleep(wait)
	os.system("clear")
	counter = counter + 1
	print("Clicked: " + str(counter) + " times")

# Run

