#build html helper
html = input("Enter file name: ")
file = open("output/" + html,"w")

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
css = input("Enter stylesheet name (blank for none): ")

if css != "":
	file.write("\n\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"" + css + "\">")
	create = ""
	create = input("Create stylesheet? (Y/N): ")
	if create != "":
		style = open("output/" + css, "w")
		style.write("* {")
		style.write("\n\tpadding: 0;")
		style.write("\n\tmarging: 0;")
		style.write("\n}")
		style.close()

file.write("\n\t\t</head>\n\t\t<body>")

file.write("\n\t\t</body>\n</html>")

print(file)

file.close()
