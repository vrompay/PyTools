# Imports
import os

# Menu components
menu = ["Celcius to fahrenheit", "Fahrenheit to celcius"]
inc = 0

# Clear everything
os.system("clear")

# Print menu
for x in menu:
	print("\t" + str(inc) + " : " + x)
	inc = inc + 1

print("\n")

# Switch for choosing options
def corf(argument):
    switcher = {
        0: "ctof",
        1: "ftoc",
    }
    return switcher.get(argument, "nothing")

# Functions
def ctof():
	celcius = int(input("Celcius: "))
	fahrenheit = celcius  * 1.8 + 32
	print(str(celcius) + " degrees celcius is " + str(fahrenheit) + " degrees fahrenheit.")

def ftoc():
	fahrenheit = int(input("Fahrenheit: "))
	celcius = (fahrenheit - 32) / 1.8
	print(str(fahrenheit) + " degrees fahrenheit is " + str(celcius) + " degrees celcius.")

# Choose convertion
option = corf(int(input("Choose your convertion: ")))

# Check option and run function
if (option == "ctof"):
	ctof()
elif (option == "ftoc"):
	ftoc()
else:
	print("A mistake was made.")


