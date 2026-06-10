# Phishing Website Detection

A comprehensive machine learning project for detecting phishing websites using feature extraction and classification algorithms.

## 📋 Overview

Phishing is a sophisticated cyber-attack technique where attackers create fraudulent websites that mimic legitimate ones to trick users into revealing sensitive information. This project employs machine learning algorithms to automatically detect phishing websites based on extracted URL and website features.

### Key Objectives
- Extract meaningful features from URLs and websites
- Build and train classification models
- Achieve high accuracy in phishing detection
- Provide a reusable framework for threat detection

## 🎯 Problem Statement

Financial institutions and individuals face significant risks from phishing attacks. Traditional security measures are often insufficient against evolving attack tactics. This project develops an intelligent system to identify phishing websites automatically using machine learning.

## 📁 Project Structure

```
phishingdetection/
├── notebooks/
│   ├── 01_FeatureExtraction.ipynb           # Feature extraction pipeline
│   ├── 02_DecisionTree_Classifier.ipynb     # Decision Tree model
│   └── 03_RandomForest_Classifier.ipynb     # Random Forest model
├── src/
│   ├── __init__.py
│   ├── feature_extraction.py                # Feature extraction utilities
│   ├── data_preprocessing.py                # Data cleaning and preparation
│   ├── model_training.py                    # Model training functions
│   └── evaluation.py                        # Model evaluation metrics
├── data/
│   ├── raw/
│   │   ├── legitimate-urls.csv
│   │   └── phishing-urls.csv
│   └── processed/
│       └── merged_data.csv
├── models/
│   ├── decision_tree_model.pkl
│   └── random_forest_model.pkl
├── results/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── model_performance.txt
├── requirements.txt
├── setup.py
└── README.md
```

## 🔧 Features Extracted

### URL-Based Features:
| Feature | Description |
|---------|-------------|
| **Having_@_symbol** | Presence of @ symbol in URL |
| **Having_IP** | URL contains IP address instead of domain |
| **Sub_domains** | Number of subdomains |
| **URL_Length** | Length of the URL |
| **Protocol** | HTTP vs HTTPS |
| **Redirection_//_symbol** | Presence of // redirection |
| **Path** | URL path characteristics |
| **Prefix_suffix_separation** | Hyphen usage in domain |

### Domain-Based Features:
| Feature | Description |
|---------|-------------|
| **age_domain** | Domain registration age |
| **dns_record** | Presence of DNS records |
| **domain_registration_length** | Duration of domain registration |
| **web_traffic** | Website traffic statistics |
| **tiny_url** | Use of URL shortening services |
| **statistical_report** | Phishing report on domain |
| **http_tokens** | HTTP token analysis |

## 🤖 Machine Learning Models

### 1. Decision Tree Classifier
- Fast training and prediction
- Highly interpretable results
- Good for feature importance analysis

### 2. Random Forest Classifier
- **Accuracy: ~82.6%**
- 500 estimators with max_depth=20
- Better generalization and robustness
- Handles non-linear relationships

### Model Comparison

| Metric | Decision Tree | Random Forest |
|--------|---------------|---------------|
| Accuracy | ~82.6% | ~82.6% |
| Precision | High | High |
| Recall | Good | Better |
| Training Time | Fast | Moderate |
| Overfitting Risk | High | Low |

## 📊 Dataset

- **Total Samples**: 2,015 URLs
- **Legitimate URLs**: ~1,007
- **Phishing URLs**: ~1,008
- **Train-Test Split**: 70-30 ratio (1,410 training, 605 testing)
- **Class Distribution**: Balanced dataset

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip or conda

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/vishalroyal350/phishingdetection.git
cd phishingdetection

# Install required packages
pip install -r requirements.txt
```

### Required Libraries
```
pandas>=1.1.0
scikit-learn>=0.24.0
numpy>=1.19.0
matplotlib>=3.3.0
seaborn>=0.11.0
jupyter>=1.0.0
```

## 📈 Usage

### 1. Data Preparation
```python
from src.data_preprocessing import load_and_preprocess_data

# Load data
data = load_and_preprocess_data('data/raw/')
```

### 2. Feature Extraction
```python
from src.feature_extraction import extract_features

# Extract features
features = extract_features(data)
```

### 3. Model Training
```python
from src.model_training import train_random_forest

# Train model
model = train_random_forest(X_train, y_train)
```

### 4. Prediction
```python
# Predict on new data
predictions = model.predict(X_test)

# Get probability scores
probabilities = model.predict_proba(X_test)
```

### 5. Evaluation
```python
from src.evaluation import evaluate_model

# Evaluate performance
evaluate_model(y_test, predictions)
```

## 📊 Model Performance

### Random Forest Classifier Results
- **Training Samples**: 1,410
- **Testing Samples**: 605
- **Accuracy**: 82.64%

### Confusion Matrix
```
                Predicted
              Legitimate  Phishing
Actual  Legitimate    258         33
        Phishing       72        242
```

### Top 5 Important Features
1. **URL_Length** (21.47%)
2. **web_traffic** (17.06%)
3. **statistical_report** (16.38%)
4. **age_domain** (8.94%)
5. **dns_record** (8.64%)

## 🔍 Key Findings

1. **URL characteristics** are the most important predictors
2. **Web traffic patterns** provide strong signals
3. **Statistical reports** correlate well with phishing sites
4. **Domain age** and **DNS records** are secondary indicators
5. The model shows good **generalization** capabilities

## 🛡️ Security Considerations

- Use only on authorized websites/URLs
- Combine with other security measures
- Regularly update with new phishing patterns
- Consider ensemble methods for production use
- Implement proper data privacy measures

## 📚 Related Research

- Domain reputation analysis
- URL feature engineering
- Machine learning for cybersecurity
- Phishing detection using deep learning
- Real-time threat detection systems

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Performance improvements
- Additional features
- Documentation improvements
- New classification models

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Vishal Royal**
- GitHub: [@vishalroyal350](https://github.com/vishalroyal350)

## 🙏 Acknowledgments

- Dataset providers for phishing URL data
- Scikit-learn community
- Contributors and reviewers

## 📞 Support & Contact

For questions or issues:
- Open an issue on GitHub
- Check existing documentation
- Review the notebooks for examples

## ⚠️ Disclaimer

This project is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. Always obtain proper authorization before testing.

---

**Last Updated**: December 2025
**Version**: 1.0.0
