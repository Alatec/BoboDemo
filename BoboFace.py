import numpy as np
import cv2
import time

face = np.zeros((480,800, 4), np.uint8)
happyFace = cv2.imread("faces/HappyFace.png", -1)
lookLeft = cv2.imread("faces/LookLeft.png", -1)
lookRight = cv2.imread("faces/LookRight.png", -1)
rbf = cv2.imread("faces/RBF.png", -1)

# cv2.namedWindow("Bobo", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Bobo", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.namedWindow("Bobo")
# cv2.setWindowProperty("Bobo")
def showHappy():
    reset()
    alpha = happyFace[:, :, 3] / 255.0
    face[85:394, 143:657, 0] = (1. - alpha) * face[85:394, 143:657, 0] + alpha * happyFace[:, :, 0]
    face[85:394, 143:657, 1] = (1. - alpha) * face[85:394, 143:657, 1] + alpha * happyFace[:, :, 1]
    face[85:394, 143:657, 2] = (1. - alpha) * face[85:394, 143:657, 2] + alpha * happyFace[:, :, 2]
    return face

def showLeft():
    reset()
    alpha = lookLeft[:, :, 3]/255.0
    face[:, :, 0] = (1. - alpha) * face[:, :, 0] + alpha * lookLeft[:, :, 0]
    face[:, :, 1] = (1. - alpha) * face[:, :, 1] + alpha * lookLeft[:, :, 1]
    face[:, :, 2] = (1. - alpha) * face[:, :, 2] + alpha * lookLeft[:, :, 2]
    return face


def showRight():
    reset()
    alpha = lookRight[:, :, 3]/255.0
    face[:, :, 0] = (1. - alpha) * face[:, :, 0] + alpha * lookRight[:, :, 0]
    face[:, :, 1] = (1. - alpha) * face[:, :, 1] + alpha * lookRight[:, :, 1]
    face[:, :, 2] = (1. - alpha) * face[:, :, 2] + alpha * lookRight[:, :, 2]
    return face

def showRBF():
    reset()
    alpha = rbf[:, :, 3]/255.0
    face[:, :, 0] = (1. - alpha) * face[:, :, 0] + alpha * rbf[:, :, 0]
    face[:, :, 1] = (1. - alpha) * face[:, :, 1] + alpha * rbf[:, :, 1]
    face[:, :, 2] = (1. - alpha) * face[:, :, 2] + alpha * rbf[:, :, 2]
    return face


def reset():
    global face
    face = np.zeros((480, 800, 4), np.uint8)

