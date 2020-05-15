import cv2

class VideoStorage:
    @staticmethod
    def empezar_video():
        """
        Lee un video desde el disco
        """
        video_captura = cv2.VideoCapture(0)
        return video_captura

    @staticmethod
    def guardar_video():
        guardar = cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))
        print('Guardando Video!!!!!')
        print('Nombre del video: videoSalida1.avi')
        print('Comenzando Captura')
        return guardar

    @staticmethod
    def mostrar_video(direccion):
        mostrar = cv2.VideoCapture(direccion)
        while (mostrar.isOpened()):
            ret, imagen = mostrar.read()
            if ret == True:
                cv2.imshow('video', imagen)

                if cv2.waitKey(45) & 0xFF == ord('s'):
                    break
            else: break
        mostrar.release()
