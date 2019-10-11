#source: https://www.andreasjakl.com/basics-of-ar-anchors-keypoints-feature-detection/



import cv2
# 1. Load the original image
img = cv2.imread('reference/cover.jpg')
 
# 2. Create BRISK algorithm
# OpenCV default threshold = 30, octaves = 3
# Using 4 octaves as cited as typical value by the original paper by Leutenegger et al.
# Using 70 as detection threshold similar to real-world example of this paper
brisk = cv2.BRISK_create(70,4)
 
# 3. Combined call to let the BRISK implementation detect keypoints
# as well as calculate the descriptors, based on the image.
# These are returned in two arrays.
(kps, descs) = brisk.detectAndCompute(img, None)
 
# 4. Print the number of keypoints and descriptors found
print("# keypoints: {}, descriptors: {}".format(len(kps), descs.shape))
# To verify: how many bits are contained in a feature descriptor?
# Should be 64 * 8 = 512 bits according to the algorithm paper.
print(len(descs[1]) * 8)
 
# 5. Use the generic drawKeypoints method from OpenCV to draw the 
# calculated keypoints into the original image.
# The flag for rich keypoints also draws circles to indicate
# direction and scale of the keypoints.
imgBrisk = cv2.drawKeypoints(img, kps, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# 6. Finally, write the resulting image to the disk
cv2.imwrite('brisk_keypoints.jpg', imgBrisk)