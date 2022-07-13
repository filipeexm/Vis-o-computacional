import cv2

#carregar o algoritmo cascade
carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlhos = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('Imagens_Projeto/4.jpg')

# deixando imagem em escala de cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemCinza, scaleFactor=1.05, minNeighbors=1, minSize=(35, 35))


print(faces)

# criando um retangulo na face
for(x, y, l, a) in faces:
    img = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    olhos = img[y:y + a, x:x + l]
    olhoCinza = cv2.cvtColor(olhos, cv2.COLOR_BGR2GRAY)
    detectado = carregaOlhos.detectMultiScale(olhoCinza, scaleFactor=1.3, minNeighbors=9)

# criando para os olhos
    for (olhox,olhoy, olhol, olhoa) in detectado:
        cv2.rectangle(olhos, (olhox, olhoy), (olhox + olhol, olhoy + olhoa), (0, 0, 255), 2)

cv2.imshow("Detectando Faces e Olhos", imagem)
cv2.waitKey()

