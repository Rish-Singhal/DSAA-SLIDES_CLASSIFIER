import sys
import os
import cv2

dirname = sys.argv[1:]
numArg = len(dirname)

# print(dirname)

if numArg != 2:
    print("syntax: python3 main.py path_dir1 path_dir2")
    exit(0)

slides = []
for files in os.listdir(dirname[0]):
    slide = cv2.imread(os.path.join(dirname[0], files))
    if slide is not None:
        slides.append(slide)

yslides = []
for files in os.listdir(dirname[1]):
    slide = cv2.imread(os.path.join(dirname[1], files))
    if slide is not None:
        yslides.append(slide)
