import cv2
from PIL import Image, ImageDraw

def main():
    timesteps = range(0, 30+2, 2)
    linewidth = 2
    gif_duration = 1000#ms
    color = (255, 0, 0)#RGB
    """
    0ns--x=152
    5ns--x=282
    25ns--x=802
    """
    img, w, h = read_image("input/graph.png")
    imglist = make_imagelist(img, timesteps, 152, linewidth, color)
    save_as_gif(gif_duration, "output/graph.gif", imglist)

def read_image(filename):
    img = cv2.imread(filename=filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img, img.shape[0], img.shape[1]

def add_verticle_line(img, x, width, color):
    img[:, x:x+width] = color
    return img

def make_imagelist(originalimg, timesteps, x, linewidth, color):
    imglist = []
    for t in timesteps:
        img = originalimg.copy()
        img = add_verticle_line(img, 152+26*t, linewidth, color)
        img = Image.fromarray(img)
        imglist.append(img)

    return imglist

def save_as_gif(duration, filename, imglist):
    imglist[0].save(filename, save_all=True, append_images=imglist[1:], optimize=False, duration=duration, loop=0)


if __name__ == "__main__":
    main()