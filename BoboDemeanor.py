import BoboFace as bf

import cv2
import threading
import queue


class BoboDemeanor(threading.Thread):
    def __init__(self, face_queue):
        threading.Thread.__init__(self, daemon=True)
        self.face_queue = face_queue
        cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def run(self):
        new_face = self.face_queue.get()

        if new_face == "happy":
            cv2.imshow("Frame", bf.showHappy())
        elif new_face == "left":
            cv2.imshow("Frame", bf.showLeft())
        elif new_face == "right":
            cv2.imshow("Frame", bf.showRight())
        elif new_face == "rbf":
            cv2.imshow("Frame", bf.showRBF())