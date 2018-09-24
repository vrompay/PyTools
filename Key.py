# Import and declarations
from pynput.keyboard import Key, Controller
import time, random

keyboard = Controller()

# Writer
def write():
	time.sleep(delayBefore)
	for x in range(amount):
		time.sleep(int(delay))
		if (realistic == "y"): # Check for realistic typing
			for char in message:
				keyboard.press(char)
				keyboard.release(char)
				realnumb = random.randint(5,13)
				time.sleep(realnumb / 100)
		else:
			keyboard.type(message)
		if (enterAfter == "y"): # Check for enter after
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)

# Settings Builder
message = input("Enter the sentence to print: ")
delay = int(input("Enter delay (1000 = 1 second): ")) / 1000
delayBefore = int(input("Enter delay before starting (1000 = 1 second): ")) / 1000
realistic = input("Use realistic typing? (Y/N): ").lower()
enterAfter = input("Enter after? (Y/N): ").lower()
repeat = input("Repeat infinitely? (Y/N): ").lower()

if (repeat == "n"):
	amount = int(input("Repeat for: "))
else:
	amount = 99999 # "Infinite" to use against abuse

# Run
write();
