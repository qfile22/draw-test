from PIL import Image, ImageDraw, ImageFont

# create an image
out = Image.new("RGB", (150, 100), (100, 100, 255))

# get a font
fnt = ImageFont.truetype("Coco-Sharp-Regular-trial.ttf", 40)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10, 10), "Hello\nThere", font=fnt, fill=(100, 10, 30))

out.show()
