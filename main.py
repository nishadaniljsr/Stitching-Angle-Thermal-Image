import cv2
from cv2 import Stitcher

# List of images
images = ['11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg']

# Read images
imgs = [cv2.imread(img) for img in images]

# Initialize stitcher
stitcher = Stitcher.create()

# Perform stitching
(status, stitched) = stitcher.stitch(imgs)

# Check if successful
if status == cv2.Stitcher_OK:
    cv2.imwrite('stitched.jpg', stitched)
else:
    print('Stitching failed: ', status)
