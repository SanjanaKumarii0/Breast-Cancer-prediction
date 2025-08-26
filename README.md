🩺 Breast Cancer Prediction
📌 Project Overview

This project focuses on predicting whether a breast tumor is malignant (cancerous) or benign (non-cancerous) using a dataset of diagnostic features. The pipeline covers data cleaning, exploratory data analysis (EDA), preprocessing, and machine learning model building, aiming to assist in early detection of breast cancer.

📂 Dataset

The dataset contains diagnostic measurements of breast tumors.

Key features include:

Radius Mean, Texture Mean, Perimeter Mean, Area Mean, Smoothness, Compactness, Concavity, Symmetry, Fractal Dimension, etc.

Target Variable:

M → Malignant (Cancer)

B → Benign (Non-Cancer)

⚙️ Workflow

Data Cleaning → Handling missing values, formatting.

EDA → Understanding relationships, visualizations (correlation heatmaps, distributions).

Preprocessing → Label encoding (M = 1, B = 0), scaling, splitting.

Model Building → Logistic Regression / Random Forest / SVM (whichever used).

Evaluation → Accuracy, Confusion Matrix, Precision, Recall, F1-score.

Deployment → Simple UI built with Streamlit for predictions.

📊 Example EDA Outputs

Correlation heatmap of features.

Distribution of malignant vs benign cases.

Feature importance from trained model.
