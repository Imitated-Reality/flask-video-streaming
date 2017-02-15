from time import time
import cv2

class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self, port):
        self.camera = cv2.VideoCapture(port)
        #self.camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1000.0)
        #self.camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 5000.0)

    def get_frame(self):
        ret, frame = self.camera.read()
        ret2, img = cv2.imencode('.jpeg', frame)
        return img.tostring()
        #return frame.tostring()
