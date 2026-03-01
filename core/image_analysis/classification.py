from core.image_analysis.image_types import PredictionResult


def predict_vitiligo(model, preprocessed_image, threshold=0.5) -> PredictionResult:
    """
    Run ResNet inference and return structured prediction result
    """
    score = model.predict(preprocessed_image).item()

    is_positive = score >= threshold
    label = "Vitiligo Detected" if is_positive else "No Vitiligo Detected"

    return PredictionResult(
        label=label,
        score=score,
        is_positive=is_positive
    )