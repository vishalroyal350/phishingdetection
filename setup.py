"""
Setup configuration for Phishing Detection package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="phishingdetection",
    version="1.0.0",
    author="Vishal Royal",
    author_email="your.email@example.com",
    description="Machine Learning based Phishing Website Detection System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishalroyal350/phishingdetection",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.1.0",
        "numpy>=1.19.0",
        "scikit-learn>=0.24.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=20.8b1",
            "flake8>=3.8.0",
        ],
        "extra": [
            "tensorflow>=2.4.0",
            "xgboost>=1.3.0",
            "lightgbm>=3.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "phishing-detect=src.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
