import cv2

def apply_canny_edge(image):
    """Detects edges in an image using the Canny algorithm."""
    # AI vision often starts with edge detection to identify shapes
    return cv2.Canny(image, 100, 200)