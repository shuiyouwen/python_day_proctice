from PIL import Image, ImageFont, ImageDraw, ImageColor
import glob, os

if __name__ == "__main__":
    im = Image.open("day1/qq.jpg")
    width, height = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("day1/myFont.ttf", size=40)
    fillColor = ImageColor.colormap.get("red")
    draw.text((width - 30, 0), "5", font=font, fill=fillColor)
    im.save("day1/result.jpg", "jpeg")
