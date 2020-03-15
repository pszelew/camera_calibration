import cv2
import numpy as np
cap = cv2.VideoCapture(2)

while cap.isOpened():
	ret, frame = cap.read()
	print('tutaj2')
	if cv2.waitKey(25):
		print('tutaj')
		cv2.imwrite("test.jpg", frame)
		break
cap.release()


mtx = np.array([[315.01134193, 0., 308.28226669],
 [0., 319.32983531, 268.17294287],
 [0., 0., 1.]], dtype=float)

dist = np.array([[-0.00365119,  0.00606801, -0.00559687, -0.00159284, -0.01594543]], dtype='float')


img = cv2.imread("test.jpg")

h, w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imshow("undistorted", dst)
cv2.imshow("distorted", img)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

