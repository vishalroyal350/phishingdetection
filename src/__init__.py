"""
Phishing Detection Package
===========================

A comprehensive machine learning framework for detecting phishing websites.

Modules:
    - feature_extraction: URL and website feature extraction
    - data_preprocessing: Data cleaning and preparation
    - model_training: Model training utilities
    - evaluation: Performance evaluation metrics
"""

__version__ = "1.0.0"
__author__ = "Vishal Royal"
__email__ = "your.email@example.com"

from . import feature_extraction
from . import data_preprocessing
from . import model_training
from . import evaluation

__all__ = [
    "feature_extraction",
    "data_preprocessing",
    "model_training",
    "evaluation",
]
