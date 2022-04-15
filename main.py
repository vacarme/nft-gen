from PIL import Image, ImageDraw, ImageChops

def generate():
    image_size = (128 *2, 128*2)
    image_background_color = (0, 0, 0)

    img = Image.new('RGB', size=image_size, color=image_background_color)