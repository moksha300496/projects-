# 🧠 Brain Tumor Segmentation Using Attention U-Net (BraTS2020)

A deep learning-based medical image segmentation project that automatically identifies and delineates brain tumor regions from MRI scans using the BraTS2020 dataset. The project implements an Attention U-Net architecture to improve segmentation accuracy by focusing on clinically relevant regions within multi-modal MRI images.

---

## 1. Project Overview

Brain tumor segmentation plays a critical role in diagnosis, treatment planning, and disease monitoring. Manual segmentation by radiologists is time-consuming and subject to variability.

This project develops an automated tumor segmentation pipeline using deep learning techniques to accurately identify tumor regions from MRI scans and generate pixel-level segmentation masks.

---

## 2. Key Features

### Medical Image Processing

* Automated BraTS2020 dataset loading
* Multi-modal MRI scan handling
* 3D volume processing
* Conversion of MRI volumes into 2D slices

### Data Preprocessing

* Z-score normalization
* Image resizing
* Mask thresholding
* Data quality validation

### Deep Learning Architecture

* Custom Attention U-Net implementation
* Attention Gates for feature refinement
* Skip connections for spatial information preservation
* Encoder-Decoder architecture

### Segmentation Optimization

* Dice Loss implementation
* Early Stopping
* Model Checkpointing
* Adam Optimizer

---

## 3. Dataset Information

### Dataset

BraTS2020 (Brain Tumor Segmentation Challenge)

### Imaging Modality

* MRI Scans

### Input Data

* FLAIR MRI Images

### Output

* Pixel-wise Tumor Segmentation Masks

---

## 4. Workflow Summary

### Step 1: Dataset Acquisition

* Download BraTS2020 dataset using Kaggle API
* Extract and organize MRI volumes

### Step 2: Data Preprocessing

* MRI slice extraction
* Intensity normalization
* Image resizing
* Mask generation

### Step 3: Model Development

#### Attention U-Net Components

* Convolution Blocks (`conv_block`)
* Attention Blocks (`attention_block`)
* Encoder Layers
* Decoder Layers
* Skip Connections

### Step 4: Model Training

Training configuration includes:

* Adam Optimizer
* Dice Loss Function
* EarlyStopping
* ModelCheckpoint

### Step 5: Evaluation

Performance is assessed using:

* Dice Coefficient
* Intersection over Union (IoU)
* Validation Loss

---

## 5. Model Architecture

### Attention U-Net

The model extends the traditional U-Net architecture by integrating attention mechanisms at skip connections, allowing the network to selectively focus on tumor regions while suppressing irrelevant background information.

### Advantages

* Improved localization accuracy
* Better handling of complex tumor boundaries
* Enhanced segmentation performance on medical imaging datasets

---

## 6. Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Matplotlib
* Nibabel
* Kaggle API

---

## 7. Repository Structure

```text
BrainTumor-Segmentation/
│
├── neurosymbolic_ai_in_stroke_prediction(final_year_project).ipynb
├── best_model.h5
└── README.md
```

---

## 8. Installation

Install required dependencies:

```bash
pip install tensorflow nibabel opencv-python numpy matplotlib kaggle
```

Place your Kaggle API credentials (`kaggle.json`) in the working directory and run the notebook:

```bash
jupyter notebook
```

---

## 9. Applications

* Medical Image Analysis
* Computer-Aided Diagnosis (CAD)
* Radiology Support Systems
* Treatment Planning
* Healthcare AI Research

---

## 10. Future Enhancements

* 3D Attention U-Net Implementation
* Multi-Class Tumor Segmentation
* Vision Transformer (ViT) Integration
* Real-Time MRI Segmentation Dashboard
* Explainable AI for Medical Imaging

---

## 11. Disclaimer

This project is intended for educational and research purposes only. The generated segmentation results should not be used as a substitute for professional medical diagnosis.

---

## Author

**P. Moksha**
B.Tech Computer Science Engineering (Artificial Intelligence)
