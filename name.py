from PIL import Image, ImageFont, ImageDraw
from random import randint

name = ""
while len(name) == 0:
    print "Enter a name:"
    name = raw_input().upper()

letter = name[0]
image = Image.new('RGB', (100, 100))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", 100)
draw.rectangle([0, 0, 100, 100], (randint(0, 256), randint(0, 256), randint(0, 256)))
draw.text((15, 0), letter, font=font)

image.save("out.png")
