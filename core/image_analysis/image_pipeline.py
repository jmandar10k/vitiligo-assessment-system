from core.image_analysis.preprocessing import preprocess_image, convert_to_grayscale
from core.image_analysis.enhancement import apply_wood_lamp_effect, create_heatmap
from core.image_analysis.classification import predict_vitiligo
from core.image_analysis.image_types import ImagePipelineResult, EnhancementResult


def run_image_pipeline(
    image,
    model,
    apply_enhancement=True
) -> ImagePipelineResult:
    """
    Full image analysis pipeline
    """

    # Preprocess
    preprocessed = preprocess_image(image)

    # Classification
    prediction = predict_vitiligo(model, preprocessed)

    # Early exit if negative
    if not prediction.is_positive:
        return ImagePipelineResult(prediction=prediction)

    # Enhancement (optional)
    if apply_enhancement:
        enhancement_data = apply_wood_lamp_effect(image)
        grayscale = convert_to_grayscale(image)
        heatmap = create_heatmap(enhancement_data["contrast"])

        enhancement = EnhancementResult(
            wood_lamp=enhancement_data["wood_lamp"],
            grayscale=grayscale,
            heatmap=heatmap
        )

        return ImagePipelineResult(
            prediction=prediction,
            enhancement=enhancement
        )

    return ImagePipelineResult(prediction=prediction)