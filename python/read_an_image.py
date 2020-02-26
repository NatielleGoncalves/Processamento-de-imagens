import cv2

img = cv2.imread('first_image_woman_by_christina_morillo.jpg', cv2.IMREAD_COLOR) # load the image

print("Size of image: ", img.shape) # print size of image

# show the image loaded 
cv2.namedWindow('first_image_loaded', cv2.WINDOW_NORMAL) # resize image for length of window
cv2.imshow('first_image_loaded', img) # show the image
cv2.waitKey(0) # Wait for any keypress
cv2.destroyAllWindows() # Destroy all windows