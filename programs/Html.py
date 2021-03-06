# Imports
import os

# Clearing screen
os.system("clear")

# Title
print("######################################################")
print("######################HTML BUILDER####################")
print("######################################################\n\n")

# Start index
html = input("Enter file name: ") + ".html"
file = open("output/" + html ,"w")

file.write("<html>\n\t<head>")

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
		style = open("output/" + css, "w")
		lines = ["* {", "\n\tpadding: 0;","\n\tmarging: 0;","\n\tfont-family: Arial, sans-serif;", "\n}"]
		for line in lines:
			style.write(line)

# Writing CSS
if css != "":
	if input("Build CSS? (Y/N): "):
		backgroundColour = ""
		backgroundColour = input("Choose background colour (blank for none): ")
		if backgroundColour != "":
			style.write("\n")
			style.write("\nbody {")
			style.write("\n\tbackground-color: " + backgroundColour + ";")
			style.write("\n}")

# Stop head, start body
file.write("\n\t</head>\n\t<body>")

# Menu
list = []
option = "Menu options here"

while option != "":
	option = input("Add menu option (enter to stop): ")
	if option != "":
		list.append(option)

if list != []:
	file.write("\n\t\t<ul>")
	print("Please add the extention of the files you link")
	for item in list:
		file.write("\n\t\t\t<li><a href=\"" + input("Link \"" + item + "\" with: ")  +  "\">" + item + "</a></li>")
	file.write("\n\t\t</ul>")


# Stop body, stop html
file.write("\n\t</body>\n</html>")

# Closing files
if css != "":
	style.close()

file.close()

# Clearing screen
os.system("clear")

# Reopening HTML file, printing and closing
print("HTML FILE:\n\n")
read = open("output/" + html)
print(read.read())
read.close()

# Enter in between
input("\n\n\nEnter to continue")

# Clearing screen
os.system("clear")

if css != "":
# Reopening CSS file, printing and closing
	print("CSS FILE:\n\n")
	readcss = open("output/" + css)
	print(readcss.read())
	readcss.close()

# Enter to close
input("\n\n\nEnter to close, you can find your files in the output folder.")

# Clearing screen
os.system("clear")
