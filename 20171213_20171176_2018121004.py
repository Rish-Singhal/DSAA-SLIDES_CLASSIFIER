import sys
import os
import numpy as np
import cv2

dirname = sys.argv[1:]
numArg = len(dirname)

if numArg != 2:
    print("syntax: python3 main.py path_dir1 path_dir2")
    exit(0)


def printa(a):
    for x in a:
        print(x, end=' ')
    print()


sift = cv2.xfeatures2d.SIFT_create()
indp = dict(algorithm=0, trees=5)
srchp = dict()
flann = cv2.FlannBasedMatcher(indp, srchp)

slides = []
slidesKey = []
slidesDesc = []
slidesName = []
test_data = os.listdir(dirname[1])
test_data.sort()
for files in test_data:
    slide = cv2.imread(os.path.join(dirname[1], files))
    if slide is not None:
        gslide = cv2.cvtColor(slide, cv2.COLOR_BGR2GRAY)
        keyPoint, desc = sift.detectAndCompute(gslide, None)
        slides.append(slide)
        slidesKey.append(keyPoint)
        slidesDesc.append(desc)
        slidesName.append(files)

yslides = []
yslidesKey = []
yslidesDesc = []
yslidesName = []
verify_data = os.listdir(dirname[0])
verify_data.sort()
for files in verify_data:
    yslide = cv2.imread(os.path.join(dirname[0], files))
    if slide is not None:
        gslide = cv2.cvtColor(yslide, cv2.COLOR_BGR2GRAY)
        keyPoint, desc = sift.detectAndCompute(gslide, None)
        yslides.append(yslide)
        yslidesKey.append(keyPoint)
        yslidesDesc.append(desc)
        yslidesName.append(files)

answer = []

# for i in slidesName:
#         print(i, end=' ')
# print()
# for i in yslidesName:
#         print(i, end=' ')
# print()


for i in range(len(slides)):
    mm = -1
    for j in range(len(yslides)):
        similarity = flann.knnMatch(slidesDesc[i], yslidesDesc[j], k=2)
        points = []
        for p1, p2 in similarity:
            if p1.distance < 0.7*p2.distance:
                points.append(p1)

        if mm < len(points):
            mm = len(points)
            an = yslidesName[j]

    answer.append(an)

f = open("20171213_20171176_2018121004.txt", "w")

for i in range(len(slides)):
    line = "%s %s\n" % (slidesName[i], answer[i])
    f.write(line)

f.close()
