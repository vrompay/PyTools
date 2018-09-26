# Imports
import pyautogui, time

# Declaretions
output = "output"

# Functions
def takeScreenshot():
	output = input("Output to Output or Webshare folder? (O/W): ").lower()
	time.sleep(int(input("Wait before taking screenshot (seconds): ")))

	if output == "o":
		pyautogui.screenshot("./output/screenshot.png")
	elif output == "w":
		pyautogui.screenshot("./webshare/share.png")
	else:
		print("A mistake was made.")

# Main
takeScreenshot()
