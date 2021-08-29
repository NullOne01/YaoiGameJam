from genericpath import isdir
import os
from sys import path
from psd_tools import PSDImage

# pathSpritesFolder = "game/images/characters/"
pathSpritesFolder = "/Users/nullone/Projects/RenPy/YaoiGameJam/game/images/characters/"
#print(os.listdir(pathSpritesFolder))

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
                psd.composite(force=True).save(os.path.abspath(strPath))
                sub_layer.visible = False


def main():
    for filename in os.listdir(pathSpritesFolder):
        newFileName = pathSpritesFolder + filename
        if (os.path.isfile(newFileName)):
            continue

        for finalPsdName in os.listdir(newFileName):
            if (finalPsdName.endswith(".psd")):
                process_psd(newFileName + "/" + finalPsdName)

if __name__ == '__main__':
    main()

#psd.print_tree()