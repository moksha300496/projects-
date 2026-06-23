# Lumpy Skin Disease (LSD) Prediction Model

## Project Overview

This project develops a machine learning-based prediction system for identifying regions at risk of Lumpy Skin Disease (LSD) outbreaks. The model leverages climatic, environmental, and geographical factors to classify disease occurrence and support early intervention strategies for livestock health management.

## Problem Statement

Lumpy Skin Disease is a viral infection affecting cattle, causing significant economic losses to the livestock industry. Early prediction of disease-prone regions can help authorities and farmers implement preventive measures, reducing disease spread and livestock mortality.

## Dataset Features

The dataset consists of climatic, environmental, and geographical variables associated with disease outbreaks.

### Climatic Variables

* Cloud Cover (`cld`)
* Diurnal Temperature Range (`dtr`)
* Frost Frequency (`frs`)
* Potential Evapotranspiration (`pet`)
* Precipitation (`pre`)
* Vapor Pressure (`vap`)
* Wet Days (`wet`)

### Temperature Metrics

* Minimum Temperature (`tmn`)
* Mean Temperature (`tmp`)
* Maximum Temperature (`tmx`)

### Environmental Features

* Elevation
* Dominant Land Cover
* Population Density

## Methodology

### 1. Data Preprocessing

* Removed irrelevant identifiers:

  * Region
  * Country
  * Reporting Date
* Removed duplicate records
* Handled missing values using backfilling techniques
* Detected and removed outliers using Z-Score filtering (threshold > 3)

### 2. Feature Engineering

* Applied Min-Max Normalization to scale all features into the range [0,1]
* Improved model convergence and stability

### 3. Model Training

The dataset was divided into:

* Training Set: 90%
* Testing Set: 10%
* Stratified sampling was used to preserve class distribution

The following machine learning algorithms were implemented and compared:

* Support Vector Machine (SVC)
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes
* Decision Tree Classifier
* Multi-Layer Perceptron (MLP)

## Model Evaluation

Performance was assessed using:

* Accuracy Score
* F1 Score
* ROC-AUC Score
* Confusion Matrix

## Results

The Support Vector Classifier (SVC) achieved the best overall performance:

| Metric              | Score  |
| ------------------- | ------ |
| Training Accuracy   | ~96.7% |
| Validation Accuracy | ~96.4% |

The results indicate that climatic and environmental factors can effectively predict Lumpy Skin Disease outbreaks using machine learning techniques.

## Technologies Used

* Python
* Pandas
* NumPy
* SciPy
* Scikit-Learn
* Matplotlib
* Jupyter Notebook

## Repository Structure

```text
Lumpy-Skin-Disease-Prediction/
│
├── MLRP.ipynb
├── Lumpy skin disease data.csv
└── README.md
```

## Applications

* Livestock Disease Monitoring
* Veterinary Decision Support Systems
* Agricultural Risk Assessment
* Early Disease Warning Systems

## Future Improvements

* Integration with real-time weather APIs
* Deep Learning-based disease prediction models
* Geographic disease hotspot visualization
* Interactive monitoring dashboard

## Author

**P. Moksha**
B.Tech Computer Science Engineering (Artificial Intelligence)
