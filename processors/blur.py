import cv2
def apply_blur(image,strength=5):
    #kernel size must be odd
    return cv2.GaussianBlur(image, (strength, strength), 0)