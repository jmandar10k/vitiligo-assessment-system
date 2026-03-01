import cv2
import numpy as np

def preprocess_image(image, target_size=(224, 224)):
    """
    Resize, normalize, and add batch dimension
    """
    image_resized = cv2.resize(image, target_size)
    image_normalized = image_resized / 255.0
    return np.expand_dims(image_normalized, axis=0)


def convert_to_grayscale(image):
    """
    Convert BGR/RGB image to grayscale
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)