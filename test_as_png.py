import main
import cv2

def test():
    width = 2
    color = [255,0,0]#RGB
    x=152

    img = main.read_image("input/graph.png")
    img = main.add_verticle_line(img, x, width, color)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("output/graph.png", img)

if __name__ == "__main__":
    test()