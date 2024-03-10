import numpy as np
import cv2  #görüntü işleme özelliğini kullanmamızı sağlayan modül
import keyboard #program sonlandırma için kullanıcaz




vid=cv2.VideoCapture(0) #video açmayı sağlar

yuz_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #yüz tespiti yapmak için cv2.CascadeClassifier() fonksiyonu ile OpenCV nin data/haarcascadein içindeki haarcascade_frontalface_default.xml yani eğitilmiş modelini indiriyoruz ve yuz_cascade değişkenine atıyoruz

while (True): #devamlı çalışacak 
    ret,frame=vid.read() #bu kod bir kareyi okur 
    
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #renkli görüntüyü gri tonlamalarına çevirecek
    yuzler=yuz_cascade.detectMultiScale(gri,1.3,5) #ekranda birden çok yüz varsa ilk parametre tonlama 2.si scale_factor nesnenin boyutunu ayarlamak için, 3.süde nesneyi tespit etmek için kullanılacak köşegen sayısıdır
    
    for (x,y,w,h) in yuzler: #x: sağ sol  y: yukarı aşağı  w: genişlik  h: yükseklik
         cv2.rectangle(frame,(x,y),(x+w,y+h),(235,222,39),3) #görüntüde dikdörtgen çizmemizi sağlayan fonksiyon
    #frame içine çizilecek, başlangıç ve bitiş noktaları, kullanılacak renk kodu rgb ve son olarak kalınlığı belirtiyoruz
    
    
    cv2.imshow("video",frame) #bir pencere oluşturacak başlık video olacak göstereceği görüntü frame olacak
    
    if keyboard.is_pressed('q') or cv2.waitKey(1) & 0xFF == 27:   #q tuşuna basıldığında veya ESC tuşuna basıldığında 
       break                           #programı sonlandıracak 


vid.release() #VideoCapture nesnesini serbest bırakacak ve buda daha düzgün çalışmasını, sonlanmasını sağlayacak
cv2.destroyAllWindows() #imshow() fonksiyonu ile açtığımız pencereyi kapatır


