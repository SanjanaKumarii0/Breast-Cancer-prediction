import streamlit as st
import streamlit as st
import pickle
import numpy as np  # <-- add this
# --------- Custom CSS for styling ---------st.markdown(
st.markdown(
    """
    <style>
    /* Full screen background image */
    .stApp {
        background-image: url("background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Overlay black with some transparency so text is visible */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0,0,0,0.7);  /* black overlay with 70% opacity */
        z-index: -1;
    }

    /* Text color */
    body, .stApp {
        color: #ffb6c1;  /* light pink text */
    }

    /* Inputs and buttons styling */
    .stNumberInput>div>div>input {
        background-color: #1c1c1c;
        color: #ffb6c1;
    }

    .stButton>button {
        background-color: #ffb6c1;
        color: #000000;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
    }

    /* Success message styling */
    .stSuccess {
        background-color: #1c1c1c;
        color: #ffb6c1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔬 Breast Cancer Prediction App")
st.write("Enter patient details below:")

# Input fields
radius_mean = st.number_input("Radius Mean", min_value=0.0)
texture_mean = st.number_input("Texture Mean", min_value=0.0)
perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0)
area_mean = st.number_input("Area Mean", min_value=0.0)
smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0)
compactness_mean = st.number_input("Compactness Mean", min_value=0.0)
concavity_mean = st.number_input("Concavity Mean", min_value=0.0)
concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0)
symmetry_mean = st.number_input("Symmetry Mean", min_value=0.0)
fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.0)
import pickle

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Collect inputs
if st.button("Predict"):
    input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean,
                            smoothness_mean, compactness_mean, concavity_mean,
                            concave_points_mean, symmetry_mean, fractal_dimension_mean]])
    prediction = model.predict(input_data)[0]
    result = "Malignant (Cancerous)" if prediction == 1 else "Benign (Non-cancerous)"
    st.success(f"Prediction: {result}")
