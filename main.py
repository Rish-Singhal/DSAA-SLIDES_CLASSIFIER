import sys
import os
import cv2

dirname = sys.argv[1:]
numArg = len(dirname)

if numArg != 2:
    print("syntax: python3 main.py path_dir1 path_dir2")
    exit(0)


sift = cv2.xfeatures2d.SIFT_create()

slides = []
for files in os.listdir(dirname[0]):
    slide = cv2.imread(os.path.join(dirname[0], files))
    if slide is not None:
        gslide = cv2.cvtColor(slide, cv2.COLOR_BGR2GRAY)
        keyPoint = sift.detect(gslide, None)
        img = cv2.drawKeypoints(
            gslide, keyPoint, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        slides.append(img)

yslides = []
for files in os.listdir(dirname[1]):
    yslide = cv2.imread(os.path.join(dirname[1], files))
    if slide is not None:
        gslide = cv2.cvtColor(yslide, cv2.COLOR_BGR2GRAY)
        keyPoint = sift.detect(gslide, None)
        img = cv2.drawKeypoints(
            gslide, keyPoint, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        yslides.append(img)
