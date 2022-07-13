import cv2

webcam = cv2.VideoCapture(0)
classificarVideo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
classificarOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')


while True:
    camera, frame = webcam.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detectando = classificarVideo.detectMultiScale(cinza)

    for(x, y, l, a) in detectando:
        cv2.rectangle(frame, (x, y), (x+l, y+a), (255, 0, 0), 2)
        olho = frame[y:y + a, x:x + l]
        olhoCinza = cv2.cvtColor(olho,cv2.COLOR_BGR2GRAY)
        localizandoOlho = classificarOlho.detectMultiScale(olhoCinza)

        for (olhox, olhoy, olhol, olhoa) in localizandoOlho:
            cv2.rectangle(olho, (olhox, olhoy), (olhox + olhol, olhoy + olhoa),(0, 255, 0), 2 )


    cv2.imshow("Imagem da Webcam", frame)

    if cv2.waitKeyEx(1) == ord('f'):
        break

webcam.release()
cv2.destroyWindow()