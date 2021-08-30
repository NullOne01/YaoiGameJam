from genericpath import isdir
import os
from sys import path
from psd_tools import PSDImage
from PIL import Image
import math

# pathSpritesFolder = "game/images/characters/"
pathSpritesFolder = "/Users/nullone/Projects/RenPy/YaoiGameJam/game/images/characters/"
#print(os.listdir(pathSpritesFolder))

def resize_canvas(old_image, new_image_path="save.jpg",
                  canvas_width=500, canvas_height=500):
    """
    Resize the canvas of old_image_path.

    Store the new image in new_image_path. Center the image on the new canvas.

    Parameters
    ----------
    old_image_path : str
    new_image_path : str
    canvas_width : int
    canvas_height : int
    """
    im = old_image
    old_width, old_height = im.size

    # Center the image
    x1 = int(math.floor((canvas_width - old_width) / 2))
    y1 = int(math.floor((canvas_height - old_height)))

    mode = im.mode
    if len(mode) == 1:  # L, 1
        new_background = (255)
    if len(mode) == 3:  # RGB
        new_background = (255, 255, 255)
    if len(mode) == 4:  # RGBA, CMYK
        new_background = (255, 255, 255, 255)
    new_background = (255, 255, 255, 0)

    newImage = Image.new(mode, (canvas_width, canvas_height), new_background)
    newImage.paste(im, (x1, y1, x1 + old_width, y1 + old_height))
    newImage = newImage.resize((1280, 720))
    newImage.save(new_image_path)

def process_psd(fileName):
    psd = PSDImage.open(fileName)

    for layer in psd:
        if (layer.is_group() and layer.name == "Expression"):
            for sub_layer in layer:
                sub_layer.visible = False
            
            for sub_layer in layer:
                sub_layer.visible = True
                mainFileName = os.path.basename(fileName)[:-4]
                strPath = fileName + "/../" + mainFileName.lower() + " " + sub_layer.name.lower() + '.png'
                #img = psd.composite(viewport=(-320, -180, 960, 540), force=True)
                #img = img.resize((1280, 720))
                #img.save(os.path.abspath(strPath))
                img = psd.composite(force=True)
                resize_canvas(img, os.path.realpath(strPath), 1280*2, 720*2)
                sub_layer.visible = False


def main():
    for filename in os.listdir(pathSpritesFolder):
        newFileName = pathSpritesFolder + filename
        if (os.path.isfile(newFileName)):
            continue

        for finalPsdName in os.listdir(newFileName):
            if (finalPsdName.endswith(".psd")):
                process_psd(newFileName + "/" + finalPsdName)
                return

if __name__ == '__main__':
    main()

#psd.print_tree()