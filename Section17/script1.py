import cv2

img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)


resized_image = cv2.resize(img,(int(img.shape[1] / 2), int(img.shape[0] / 2)))
# will show image on screen
cv2.imshow("galaxy", resized_image)

cv2.imwrite("Section17/galaxy_resized.jpg", resized_image)
# specify a time for the window to be closed, this would way for two seconds
cv2.waitKey(2000)
# this would close the image
cv2.destroyAllWindows()

