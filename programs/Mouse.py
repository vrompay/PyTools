from pynput.mouse import Button, Controller
import time, os

mouse = Controller()
x = 0
counter = 0

wait = int(input("Wait time between clicks (1 second = 1000): ")) / 1000

time.sleep(int(input("Time to wait before starting (1 second = 1000): ")) / 1000)

while x == 0:
	mouse.press(Button.left)
	mouse.release(Button.left)
	time.sleep(wait)
	os.system("clear")
	counter = counter + 1
	print("Clicked: " + str(counter) + " times")
