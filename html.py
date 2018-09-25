#build html helper
file = open("output/" + input("Enter file name: "),"w")

file.write("<html><head>")

# Title
title = ""
title = input("Enter title (blank for none): ")

if title != "":
	file.write("<title>" + title + "</title>")

# Author
author = ""
author = input("Enter author (blank for none): ")

if author != "":
	file.write("<meta name=\"author\" content=\"" + author + "\""">")

file.write("</head><body>")

file.write("</body></html>")

print(file)

file.close()
