Face Mask Detection Web Application

This project is a web application that detects whether a person is wearing a face mask using a deep learning model. The user can upload an image, and the system predicts whether a mask is present or not.

Features
- Upload an image
- Detect face mask or no mask
- Display prediction result

Technologies Used
- Python
- TensorFlow / Keras
- Streamlit

How It Works
- The uploaded image is preprocessed
- The image is passed to a trained CNN model
- The model predicts whether a mask is present or not

How to Run the Project
- This application runs locally on your system
- Install required libraries:
  pip install -r requirements.txt
- Run the application:
  streamlit run app.py

Note
- The trained model file (.h5) is not included due to GitHub size limits
