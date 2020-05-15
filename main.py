import cv2
from hola.VideoStorage import VideoStorage
import numpy as np
"""
Descripcion de captura, guardado y mostrado de la deteccion de rostros
para finalizar la grabacion presion s
"""

if __name__ == '__main__':
    captura = VideoStorage.empezar_video()
    salida = VideoStorage.guardar_video()
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        ret, frame = captura.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        salida.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    captura.release()
    salida.release()
    cv2.destroyAllWindows()
    print("Programa Corrio con exito")
    path = input('Introduzca el nombre del video guardado:')
    VideoStorage.mostrar_video(path)
    print("Programa Terminado")
    cv2.destroyAllWindows()
