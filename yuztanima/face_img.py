import cv2, sys, time

#Haar cascade classifier yukle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img_path = sys.argv[1] #dosya yolunu al
img = cv2.imread(img_path,1) #dosyayi oku
time.sleep(5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #siyah-beyaz yap

#yuzleri bul
faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize = (130,130))

#yuzleri isaretle
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #gozleri bul
    eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(50,50))
    #gozleri isaretle
    for (x1,y1,w1,h1) in eyes:
        cv2.rectangle(roi_color, (x1,y1), (x1+w1,y1+h1), (255,0,0),2)

cv2.imshow('img',img) #ekranda
cv2.imwrite("output_detected.jpg", img) #kaydet
cv2.waitKey(0) #tusa basinca cik
cv2.destroyAllWindows()