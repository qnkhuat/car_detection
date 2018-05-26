import json
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-j',help='json')
parser.add_argument('-i',help='path to images folder')
args = parser.parse_args()

a = json.load(open(args.j))

for dir in os.listdir(args.i):
    if '.jpg' in dir:
        img = Image.open(os.path.join(args.i,dir))
        for i in range(len(a)):
            if a[i]['filename'] in  dir:
                draw = ImageDraw.Draw(img)
                for j in range(len(a[i]['regions'])):
                    x = a[i]['regions'][str(j)]['shape_attributes']['all_points_x']
                    y = a[i]['regions'][str(j)]['shape_attributes']['all_points_y']
                    x = list(map(int, x))#convert points from string to int
                    y = list(map(int, y))#convert points from string to int
                    xy = tuple(zip(x,y))
                    draw.line(xy,fill=200,width=10)
                img.show()
                input('Come on')
    else :
        continue
