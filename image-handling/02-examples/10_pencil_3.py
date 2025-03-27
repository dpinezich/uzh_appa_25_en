
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("model.jpg")

cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert_img=cv2.bitwise_not(grey_img)
#invert_img=255-grey_img

# blur
blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

# invert blur
invblur_img=cv2.bitwise_not(blur_img)
#invblur_img=255-blur_img

#sketch
sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
cv2.imwrite('sketch.png', sketch_img)
