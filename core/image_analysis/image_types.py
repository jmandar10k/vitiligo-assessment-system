from dataclasses import dataclass
from typing import Optional
import numpy as np


@dataclass
class PredictionResult:
    label: str
    score: float
    is_positive: bool


@dataclass
class EnhancementResult:
    wood_lamp: np.ndarray
    grayscale: np.ndarray
    heatmap: np.ndarray


@dataclass
class ImagePipelineResult:
    prediction: PredictionResult
    enhancement: Optional[EnhancementResult] = None