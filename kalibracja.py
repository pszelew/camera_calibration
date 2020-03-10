import numpy as np
import cv2
 
# Ustawic tak zeby byla odpowiednia kamera
cap = cv2.VideoCapture(2)
 
# Kryterium przerwania wykyrwania naroznikow z dokladnoscia ponizej 1 pxl
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
# przyogtowane punkty rzeczywistego polozenia naroznikow
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)
 
# Listy przechowujace punkty
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
 
i = 0
succes = 0
 
while (cap.isOpened()):
    retcam, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 
    # Find the chess board corners
    retcor, corners = cv2.findChessboardCorners(gray, (9,6),None)
 
    # If found, add object points, image points (after refining them)
    if retcor == True:
        objpoints.append(objp)
 
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
 
        # Draw and display the corners
        frame = cv2.drawChessboardCorners(frame, (9,6), corners2,retcor)
        succes += 1
    else:
        print("Nie Znaleziono")
    cv2.waitKey(1000)
    frame_disp = cv2.flip(frame, 1)
    cv2.imshow('frame',frame_disp)
    i += 1
    if(i == 100):
        break
 
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
 
print(f"Succes: {succes}")
print("Camera Matrix:")
print(mtx)
print("Distorion Matrix:")
print(dist)
 
cap.release()
cv2.destroyAllWindows()
