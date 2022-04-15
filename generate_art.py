from PIL import Image, ImageDraw, ImageChops
from random import randint, random
import colorsys

def random_color():
    h = random()
    s,v = 1,1
    return tuple(int(channel * 255) for channel in colorsys.hsv_to_rgb(h, s, v))


def interpolate(start_color, end_color, factor: float):
    # Find the color that is exactly factor (0.0 - 1.0) between the two colors.
    new_color_rgb = []
    for i in range(3):
        new_color_value = factor * end_color[i] + (1 - factor) * start_color[i]
        new_color_rgb.append(int(new_color_value))

    return tuple(new_color_rgb)


def generate_art(n):
    print('art generated')
    image_size = (128 *2, 128*2)
    image_background_color = (0, 0, 0)
    start_color = random_color()
    end_color = random_color()

    img = Image.new('RGB', size=image_size, color=image_background_color)

    #draw some lines
    padding = (10, 10)
    thickness = 0
    points = [(randint(padding[0],255 - padding[1]), randint(padding[0],255 - padding[1])) for _ in range(n)]
    #recenter
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    delta_x = min_x - (image_size[0] - max_x)
    delta_y = min_y - (image_size[1] - max_y)
    points = [(point[0] - delta_x // 2, point[1] - delta_y // 2) for point in points]
    lines = [(points[i], points[i+1]) for i in range(len(points)-1)]
    for i,line in enumerate(lines):
        # Find the right color.
        factor = i / n
        line_color = interpolate(start_color, end_color, factor=factor)
        #overlay
        overlay_img = Image.new('RGB', size=image_size, color=image_background_color)
        thickness +=1
        overlay_draw = ImageDraw.Draw(overlay_img)
        overlay_draw.line(line, fill=line_color, width=thickness) #fill=line[0]+(randint(0,255),)
        img = ImageChops.add(img, overlay_img)
    img = img.resize((128, 128), resample=Image.ANTIALIAS)
    img.save('test.png')

if __name__ == '__main__':
    generate_art(10)
