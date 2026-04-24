import cv2

def resize_image(image, width=640, height=640):
    """Standardizes image size for AI processing."""
    dimensions = (width, height)
    return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)