from imutils import paths
import os
import argparse
import shutil

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--SrcPathName", required=True,
        help="path to parse image")
ap.add_argument("-d", "--DstPathName", required=True,
        help="path to dst image")
ap.add_argument("-n", "--ImageMount", type=int, default=1000,
        help="# mount of copy images")
args = vars(ap.parse_args())

print("[INFO] loading images...")

number = 0
for i in paths.list_images(args["SrcPathName"]):
    if number < args["ImageMount"]:
        shutil.copy2(i, args["DstPathName"])
    number += 1

print("[INFO] number %d" % (number))
#imagePaths = list(paths.list_images(args["pathname"]))
