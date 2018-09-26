import os

programs = ["Automatic typer", "Celcius and Fahrenheit convertor", "Take screenshot", "Make graph", "Auto clicker", "HTML builder"]
inc = 0
fol = "programs/"

os.system("clear")
print("PYTHON TOOLS\nby HANSJORG VAN ROMPAY\n")

for x in programs:
	print("\t" + str(inc) + " : " +  x)
	inc = inc + 1

# Choose option
def menu(argument):
    switcher = {
        0: fol + "Key.py",
        1: fol + "Degree.py",
        2: fol + "Screenshot.py",
	3: fol + "Chart.py",
	4: fol + "Mouse.py",
	5: fol + "Html.py",
    }
    return switcher.get(argument, "You invoked an error.")

os.system("clear && python3 " + menu(int(input("\nChoose a program: "))))

