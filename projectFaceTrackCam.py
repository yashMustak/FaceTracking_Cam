import numpy as np
import cv2
import serial
#import matplotlib.pyplot as mpl

face_cascade = cv2.CascadeClassifier('haarCascadeFaceF.xml')

cap = cv2.VideoCapture(1)

ser1 = serial.Serial('COM4',9600)
#hc = 0
#wc = 0
while True:
    ret, img = cap.read()
    rows = 638#np.size(img, 0)
    cols = 479#np.size(img, 1)
    hc = cols/2
    wc = rows/2
    a=20
    b=20
    cv2.line(img, (int(rows/2),0), (int(rows/2),cols), (255,255,255), 2)
    cv2.line(img, (0,int(cols/2)), (rows,int(cols/2)), (255,255,255), 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
        wc = (x+x+w)/2
        hc = (y+y+w)/2

    if(hc>cols/2+b):
        print('D')
        ser1.write('D'.encode())
    elif(hc<cols/2-b):
        print('U')
        ser1.write('U'.encode())

    if(wc>rows/2+a):
        print('R')
        ser1.write('R'.encode())
    elif(wc<rows/2-a):
        print('L')
        ser1.write('L'.encode())

    cv2.imshow('img', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
