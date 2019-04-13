import numpy as np
import cv2

# Read the intensity data for the two polarizations
im = cv2.imread('vh.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
vh_im, vh_contours, vh_hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

im = cv2.imread('vv.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
vv_im, vv_contours, vv_hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Find where they interesect
intersection = np.logical_and(vh_im, vv_im)
union = np.logical_or(vh_im, vv_im)
 
# Find the centroids of the places where they intersect
detector = cv2.SimpleBlobDetector()
keypoints = detector.detect(intersection)
 
# Draw circles at the centroids on the picture that shows both
im_with_keypoints = cv2.drawKeypoints(union, keypoints, np.array([]), (0,0,255),  v2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
