import cv2

def apply_wood_lamp_effect(image):
    """
    Simulate Wood's lamp effect using CLAHE and colormap
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast_enhanced = clahe.apply(gray_image)

    wood_lamp_effect = cv2.applyColorMap(
        contrast_enhanced, cv2.COLORMAP_OCEAN
    )

    blended = cv2.addWeighted(image, 0.5, wood_lamp_effect, 0.5, 0)

    return {
        "wood_lamp": blended,
        "contrast": contrast_enhanced
    }


def create_heatmap(gray_image):
    """
    Highlight potential vitiligo regions using thresholding
    """
    _, thresholded = cv2.threshold(
        gray_image, 180, 255, cv2.THRESH_BINARY
    )

    heatmap = cv2.applyColorMap(thresholded, cv2.COLORMAP_JET)
    return heatmap