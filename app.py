import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load model
model = load_model('face_mask_model.h5')

# Title
st.title("😷 Face Mask Detection App")

st.write("Upload an image to check if the person is wearing a mask or not.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess image
    image = image.resize((128, 128))
    image = image.convert('RGB')
    image = np.array(image) / 255.0
    image = image.reshape(1, 128, 128, 3)

    # Prediction
    prediction = model.predict(image)
    pred = prediction[0][0]

    # Output
    if pred > 0.5:
        st.success(f"✅ With Mask 😷 ({pred:.2f})")
    else:
        st.error(f"❌ Without Mask ({pred:.2f})")