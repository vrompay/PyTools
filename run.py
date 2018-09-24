import os

programs = ["Automatic typer", "Celcius and Fahrenheit convertor", "Take screenshot"]
inc = 0

os.system("clear")
print("PYTHON TOOLS\nby HANSJORG VAN ROMPAY\n")

for x in programs:
	print("\t" + str(inc) + " : " +  x)
	inc = inc + 1

# Choose option
def menu(argument):
    switcher = {
        0: "Key.py",
        1: "Degree.py",
        2: "Screenshot.py",
    }
    return switcher.get(argument, "You invoked an error.")

os.system("clear && python3 " + menu(int(input("\nChoose a program: "))))

