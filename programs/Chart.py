# Import
from PIL import Image, ImageDraw, ImageFont

# Data build up and variables
data = input("Data (separate with comma (,)): ")
data = data.split(",")
sort = input("Sort data? (Y/N): ").lower()
if sort == "y":
	data.sort()

width = 10
height = 0
margin = 10
index = 10
counter = 0
name = ""
max = 0

# Building image
for point in data:
	width = width + 30
	if int(point) >= max:
		max = int(point)

height = max * 20 + 5

img = Image.new("RGB", (width, height), color = "white")

for point in data:
	name = "column" + str(counter)
	name = ImageDraw.Draw(img)
	name.rectangle(((index,int(point)*20),(index + 20,5)), fill="black", outline = "black")
	index = index + 30
	counter = int(counter) + 1

# Flip image
img = img.transpose(Image.FLIP_TOP_BOTTOM)

# Save image
img.save("./output/" + input("File name: ") + ".png")

