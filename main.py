import cv2
import json
from PIL import Image, ImageDraw

def main():
    linewidth = 3
    gif_duration = 1000#ms
    color = [255,0,0]#RGB
    pixellist = read_json("input/data.json")
    img = read_image("input/graph.png")
    imglist = make_imagelist(img, pixellist, 152, linewidth, color)
    save_as_gif(gif_duration, "output/graph.gif", imglist)

def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    begin, step, end = data["begin"], data["step"], data["end"]

    assert begin < end
    assert type(begin) == type(end) == type(step) == int

    pixellist = range(begin, end+step, step)
    return pixellist

def read_image(filename):
    img = cv2.imread(filename=filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def add_verticle_line(img, x, width, color):
    img[:, x:x+width] = color
    return img

def make_imagelist(originalimg, pixellist, x, linewidth, color):
    imglist = []
    for x in pixellist:
        img = originalimg.copy()
        img = add_verticle_line(img, x, linewidth, color)
        img = Image.fromarray(img)
        imglist.append(img)

    return imglist

def save_as_gif(duration, filename, imglist):
    imglist[0].save(filename, save_all=True, append_images=imglist[1:], optimize=False, duration=duration, loop=0)


if __name__ == "__main__":
    main()