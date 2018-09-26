# Imports
import os

# Clearing screen
os.system("clear")

# Start index
html = input("Enter file name (no extentions): ") + ".html"
file = open("./output/" + html,"w")

file.write("<html>\n\t<head>\n")

# Title
title = ""
title = input("Enter title (blank for none): ")

if title != "":
	file.write("\n\t\t<title>" + title + "</title>")

# Author
author = ""
author = input("Enter author (blank for none): ")

if author != "":
	file.write("\n\t\t<meta name=\"author\" content=\"" + author + "\""">")

# CSS
css = ""
css = input("Enter stylesheet name (blank for none - no extentions): ") + ".css"

# CSS file builder
if css != "":
	file.write("\n\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"" + css + "\">")
	create = ""
	create = input("Create stylesheet? (Y/N): ").lower()
	if create == "y":
		style = open("./output/" + css, "w")
		style.write("* {")
		style.write("\n\tpadding: 0;")
		style.write("\n\tmarging: 0;")
		style.write("\n\tfont-family: Arial, sans-serif;")
		style.write("\n}")

# Writing CSS
if input("Build CSS? (Y/N): "):
	backgroundColour = ""
	backgroundColour = input("Choose background colour (blank for none): ")
	if backgroundColour != "":
		style.write("\n")
		style.write("\nbody {")
		style.write("\n\tbackground-color: " + backgroundColour + ";")
		style.write("\n}")

# Stop head, start body
file.write("\n\t\t</head>\n\t\t<body>")

# Stop body, stop html
file.write("\n\t\t</body>\n</html>")



# Closing files
style.close()
file.close()

# Clearing screen
os.system("clear")

# Reopening HTML file, printing and closing
print("HTML FILE:\n\n")
read = open("./output/" + html)
print(read.read())
read.close()

# Enter in between
input("\n\n\nEnter to continue")

# Clearing screen
os.system("clear")

# Reopening CSS file, printing and closing
print("CSS FILE:\n\n")
readcss = open("./output/" + css)
print(readcss.read())
readcss.close()

# Enter to close
input("\n\n\nEnter to close, you can find your files in the output folder.")

# Clearing screen
os.system("clear")
