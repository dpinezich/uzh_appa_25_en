
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("model.jpg")

cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img)
plt.axis(False)
plt.show()