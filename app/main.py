import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="centered"
)


# -----------------------------
# App Header
# -----------------------------
st.title("🌱 PlantCare AI")

st.subheader(
    "AI-Based Plant Disease Detection & Intelligent Plant Care System"
)

st.info(
    "Upload a clear plant leaf image to detect possible diseases "
    "and get symptoms, care and prevention guidance."
)

st.divider()


# -----------------------------
# Application Navigation
# -----------------------------
section = st.radio(
    "Navigate",
    [
        "🏠 Home",
        "🔬 Disease Detection",
        "ℹ️ How It Works",
        "📖 About"
    ],
    horizontal=True
)

st.divider()


# -----------------------------
# Home Section
# -----------------------------
if section == "🏠 Home":

    st.header("🌿 Welcome to PlantCare AI")

    st.write(
        "PlantCare AI is an AI-based plant disease detection "
        "and intelligent plant care system."
    )

    st.write(
        "Upload a clear image of a plant leaf and the trained "
        "AI model will analyze the image and provide a possible "
        "disease prediction along with useful care information."
    )

    st.subheader("✨ What PlantCare AI Provides")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🔬 AI-Based Disease Detection")
        st.info("📊 Prediction Confidence")
        st.info("🩺 Disease Symptoms")

    with col2:
        st.info("🌱 Plant Care Guidance")
        st.info("🛡️ Prevention Tips")
        st.info("📷 Image-Based Analysis")

    st.success(
        "💡 Start by selecting '🔬 Disease Detection' "
        "from the navigation above."
    )


# -----------------------------
# Disease Class Names
# -----------------------------
class_names = [
    "Apple - Apple Scab",
    "Apple - Black Rot",
    "Apple - Cedar Apple Rust",
    "Apple - Healthy",
    "Blueberry - Healthy",
    "Cherry - Powdery Mildew",
    "Cherry - Healthy",
    "Corn - Cercospora Leaf Spot / Gray Leaf Spot",
    "Corn - Common Rust",
    "Corn - Northern Leaf Blight",
    "Corn - Healthy",
    "Grape - Black Rot",
    "Grape - Esca (Black Measles)",
    "Grape - Leaf Blight",
    "Grape - Healthy",
    "Orange - Citrus Greening",
    "Peach - Bacterial Spot",
    "Peach - Healthy",
    "Bell Pepper - Bacterial Spot",
    "Bell Pepper - Healthy",
    "Potato - Early Blight",
    "Potato - Late Blight",
    "Potato - Healthy",
    "Raspberry - Healthy",
    "Soybean - Healthy",
    "Squash - Powdery Mildew",
    "Strawberry - Leaf Scorch",
    "Strawberry - Healthy",
    "Tomato - Bacterial Spot",
    "Tomato - Early Blight",
    "Tomato - Late Blight",
    "Tomato - Leaf Mold",
    "Tomato - Septoria Leaf Spot",
    "Tomato - Spider Mites",
    "Tomato - Target Spot",
    "Tomato - Yellow Leaf Curl Virus",
    "Tomato - Mosaic Virus",
    "Tomato - Healthy"
]


# -----------------------------
# Disease Information
# -----------------------------
disease_info = {

    "Apple - Apple Scab": {
        "symptoms": "Olive-green or dark spots may appear on leaves and fruit.",
        "care": "Remove affected leaves and improve air circulation.",
        "prevention": "Keep fallen leaves and infected plant material cleaned up."
    },

    "Apple - Black Rot": {
        "symptoms": "Dark circular spots and dead areas may develop on leaves.",
        "care": "Remove affected plant parts and keep the area clean.",
        "prevention": "Remove infected plant material and maintain good airflow."
    },

    "Apple - Cedar Apple Rust": {
        "symptoms": "Yellow-orange spots may appear on apple leaves.",
        "care": "Remove badly affected leaves and monitor the plant.",
        "prevention": "Maintain plant hygiene and monitor regularly."
    },

    "Apple - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue proper watering, sunlight and nutrition.",
        "prevention": "Regularly inspect leaves for early signs of disease."
    },

    "Blueberry - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Maintain proper watering, sunlight and soil conditions.",
        "prevention": "Regularly monitor leaves and stems."
    },

    "Cherry - Powdery Mildew": {
        "symptoms": "White powder-like growth may appear on leaves.",
        "care": "Remove severely affected leaves and improve air circulation.",
        "prevention": "Avoid overcrowding and maintain good airflow."
    },

    "Cherry - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue regular plant care.",
        "prevention": "Monitor the plant regularly."
    },

    "Corn - Cercospora Leaf Spot / Gray Leaf Spot": {
        "symptoms": "Gray or brown elongated spots can develop on corn leaves.",
        "care": "Remove severely affected material where practical and improve airflow.",
        "prevention": "Maintain field hygiene and avoid prolonged leaf wetness."
    },

    "Corn - Common Rust": {
        "symptoms": "Small reddish-brown rust-like spots may appear on leaves.",
        "care": "Monitor affected leaves and maintain good airflow.",
        "prevention": "Use healthy planting material and maintain plant hygiene."
    },

    "Corn - Northern Leaf Blight": {
        "symptoms": "Long gray-green or tan lesions may appear on corn leaves.",
        "care": "Remove severely affected material where practical and maintain airflow.",
        "prevention": "Use healthy planting material and maintain crop hygiene."
    },

    "Corn - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue proper watering, sunlight and nutrition.",
        "prevention": "Regularly inspect the leaves."
    },

    "Grape - Black Rot": {
        "symptoms": "Brown or black spots may develop on leaves and fruit.",
        "care": "Remove affected plant material and keep the area clean.",
        "prevention": "Maintain good airflow and remove infected debris."
    },

    "Grape - Esca (Black Measles)": {
        "symptoms": "Leaf discoloration and irregular dead areas may occur.",
        "care": "Remove severely affected material and monitor plant health.",
        "prevention": "Use healthy planting material and maintain vineyard hygiene."
    },

    "Grape - Leaf Blight": {
        "symptoms": "Brown or dark lesions may appear on grape leaves.",
        "care": "Remove badly affected leaves and improve air circulation.",
        "prevention": "Avoid prolonged leaf wetness and maintain cleanliness."
    },

    "Grape - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue regular grape plant care.",
        "prevention": "Monitor leaves and fruit regularly."
    },

    "Orange - Citrus Greening": {
        "symptoms": "Leaves may show uneven yellowing and reduced plant vigor.",
        "care": "Monitor affected plants and remove severely declining material where appropriate.",
        "prevention": "Use healthy planting material and regularly monitor plants."
    },

    "Peach - Bacterial Spot": {
        "symptoms": "Small dark spots may appear on leaves and fruit.",
        "care": "Remove affected plant material and maintain good airflow.",
        "prevention": "Keep the growing area clean and avoid prolonged leaf wetness."
    },

    "Peach - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue normal plant care.",
        "prevention": "Inspect leaves regularly."
    },

    "Bell Pepper - Bacterial Spot": {
        "symptoms": "Small dark spots may develop on leaves and fruit.",
        "care": "Remove severely affected leaves and maintain airflow.",
        "prevention": "Avoid unnecessary leaf wetness and maintain hygiene."
    },

    "Bell Pepper - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue proper watering and sunlight.",
        "prevention": "Monitor the plant regularly."
    },

    "Potato - Early Blight": {
        "symptoms": "Dark spots with ring-like patterns may develop on older leaves.",
        "care": "Remove severely affected leaves and maintain good airflow.",
        "prevention": "Keep plant debris cleaned up and avoid prolonged leaf wetness."
    },

    "Potato - Late Blight": {
        "symptoms": "Dark irregular patches may develop on leaves.",
        "care": "Remove severely affected plant material and monitor nearby plants.",
        "prevention": "Maintain good airflow and avoid prolonged leaf wetness."
    },

    "Potato - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue normal plant care.",
        "prevention": "Inspect leaves regularly."
    },

    "Raspberry - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue proper watering and sunlight.",
        "prevention": "Regularly monitor plant health."
    },

    "Soybean - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue normal crop care.",
        "prevention": "Monitor leaves regularly."
    },

    "Squash - Powdery Mildew": {
        "symptoms": "White powder-like patches may appear on leaves.",
        "care": "Remove severely affected leaves and improve airflow.",
        "prevention": "Avoid overcrowding and excessive leaf moisture."
    },

    "Strawberry - Leaf Scorch": {
        "symptoms": "Dark reddish or brown areas may appear on leaves.",
        "care": "Remove severely affected leaves and maintain plant hygiene.",
        "prevention": "Provide good airflow and monitor plants regularly."
    },

    "Strawberry - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue regular plant care.",
        "prevention": "Inspect leaves regularly."
    },

    "Tomato - Bacterial Spot": {
        "symptoms": "Small dark spots may appear on leaves and fruit.",
        "care": "Remove affected leaves and avoid unnecessary leaf wetness.",
        "prevention": "Maintain plant hygiene and good airflow."
    },

    "Tomato - Early Blight": {
        "symptoms": "Dark spots with concentric ring patterns may develop on leaves.",
        "care": "Remove affected leaves and improve air circulation.",
        "prevention": "Keep plant debris clean and avoid prolonged leaf wetness."
    },

    "Tomato - Late Blight": {
        "symptoms": "Dark irregular patches may appear on leaves.",
        "care": "Remove affected plant material and monitor nearby plants.",
        "prevention": "Maintain airflow and avoid prolonged leaf wetness."
    },

    "Tomato - Leaf Mold": {
        "symptoms": "Yellow areas may appear on upper leaf surfaces with mold underneath.",
        "care": "Remove affected leaves and improve ventilation.",
        "prevention": "Avoid excessive humidity and maintain airflow."
    },

    "Tomato - Septoria Leaf Spot": {
        "symptoms": "Small circular spots may develop on older leaves.",
        "care": "Remove affected leaves and keep plant debris away.",
        "prevention": "Avoid prolonged leaf wetness and maintain cleanliness."
    },

    "Tomato - Spider Mites": {
        "symptoms": "Fine speckling and discoloration may appear on leaves.",
        "care": "Inspect the underside of leaves and isolate affected plants if needed.",
        "prevention": "Monitor plants regularly and maintain healthy growing conditions."
    },

    "Tomato - Target Spot": {
        "symptoms": "Dark circular target-like spots may appear on leaves.",
        "care": "Remove affected leaves and improve air circulation.",
        "prevention": "Avoid prolonged leaf wetness and maintain plant hygiene."
    },

    "Tomato - Yellow Leaf Curl Virus": {
        "symptoms": "Leaves may curl, become yellow and show reduced growth.",
        "care": "Remove severely affected plants where appropriate and monitor nearby plants.",
        "prevention": "Use healthy planting material and control insect vectors."
    },

    "Tomato - Mosaic Virus": {
        "symptoms": "Mottled light and dark green patterns may appear on leaves.",
        "care": "Remove severely affected plants and avoid spreading plant sap.",
        "prevention": "Maintain hygiene and use healthy planting material."
    },

    "Tomato - Healthy": {
        "symptoms": "No major disease symptoms detected.",
        "care": "Continue proper watering, sunlight and nutrition.",
        "prevention": "Regularly monitor leaves and plant growth."
    }
}


# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = "model/plant_disease_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

# -----------------------------
# Load Leaf Validator Model
# -----------------------------
VALIDATOR_MODEL_PATH = "model/leaf_validator.keras"

leaf_validator = tf.keras.models.load_model(
    VALIDATOR_MODEL_PATH
)


# -----------------------------
# Disease Detection Section
# -----------------------------
if section == "🔬 Disease Detection":

    st.header("📷 Plant Leaf Analysis")

    st.write(
        "Choose a clear image of a plant leaf for AI-based analysis."
    )

    uploaded_file = st.file_uploader(
        "Upload Plant Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        st.success("Image uploaded successfully! 🌿")

    # -----------------------------
    # Image Analysis
    # -----------------------------
    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")
        # -----------------------------
        # Leaf / Non-Leaf Validation
        # -----------------------------
        validation_image = image.resize((224, 224))

        validation_array = np.array(
            validation_image
        ).astype(np.float32)

        validation_array = np.expand_dims(
            validation_array,
            axis=0
        )

        validation_array = validation_array / 255.0

        validator_prediction = leaf_validator.predict(
            validation_array,
            verbose=0
        )

        validator_score = float(
            validator_prediction[0][0]
        )

        # 0 = Non-Leaf
        # 1 = Leaf

        if validator_score < 0.5:

            st.error(
                "⚠️ This image does not appear to contain "
                "a plant leaf."
            )

            st.info(
                "🌿 Please upload a clear image of a plant leaf "
                "for disease detection."
            )

            st.stop()

        else:

            st.success(
                "🌿 Plant leaf detected. Starting disease analysis..."
            )

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.divider()

        # -----------------------------
        # Basic Plant Image Validation
        # -----------------------------
        validation_image = image.resize((224, 224))

        validation_array = np.array(
            validation_image
        ).astype(np.float32)

        # Extract RGB channels
        red = validation_array[:, :, 0]
        green = validation_array[:, :, 1]
        blue = validation_array[:, :, 2]

        # Detect green plant-like pixels
        green_pixels = (
            (green > red * 1.05) &
            (green > blue * 1.05) &
            (green > 50)
        )

        green_ratio = np.mean(green_pixels)

        # Basic validation threshold
        if green_ratio < 0.03:

            st.error(
                "⚠️ This image does not appear to contain "
                "a clear plant leaf."
            )

            st.info(
                "🌿 Please upload a clear image of a plant leaf "
                "for disease detection."
            )

            st.stop()

        # -----------------------------
        # Prepare Image for AI Model
        # -----------------------------
        img = image.resize((224, 224))

        img_array = np.array(img)

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        img_array = img_array / 255.0

        # -----------------------------
        # Prediction
        # -----------------------------
        prediction = model.predict(
            img_array,
            verbose=0
        )

        predicted_class = np.argmax(
            prediction[0]
        )

        confidence = float(
            np.max(prediction[0]) * 100
        )

        disease_name = class_names[
            predicted_class
        ]

        # -----------------------------
        # Top 3 Predictions
        # -----------------------------
        top_3_indices = np.argsort(
            prediction[0]
        )[-3:][::-1]

        top_3_predictions = []

        for index in top_3_indices:

            name = class_names[index]

            score = float(
                prediction[0][index] * 100
            )

            top_3_predictions.append(
                (name, score)
            )

        # -----------------------------
        # Detection Result
        # -----------------------------
        st.header("🔍 Detection Result")

        st.success(
            "✅ Image analyzed successfully!"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "🌿 Possible Disease",
                disease_name
            )

        with col2:
            st.metric(
                "📊 Confidence",
                f"{confidence:.2f}%"
            )

        st.progress(
            min(confidence / 100, 1.0)
        )
        # -----------------------------
        # Top 3 Predictions Display
        # -----------------------------
        st.subheader("🏆 Top 3 Model Predictions")

        for name, score in top_3_predictions:

            st.write(
                f"**{name}** — {score:.2f}%"
            )

            st.progress(
                min(score / 100, 1.0)
            )

        if confidence >= 70:

            st.success(
            "🟢 High confidence prediction. "
            "The model has strong confidence in this result."
            )

        elif confidence >= 50:

            st.info(
            "🟡 Moderate confidence prediction. "
            "For better reliability, you can upload a clearer leaf image."
            )

        else:

            st.warning(
            "🔴 Low confidence prediction. "
            "Please upload a clearer leaf image for a more reliable result."
            )
        # -----------------------------
        # Care Information
        # -----------------------------
        healthy_classes = [
            3, 4, 6, 10, 14, 17,
            19, 22, 23, 24, 27, 37
        ]

        if predicted_class in healthy_classes:

            st.success(
                "🌿 The plant appears healthy. "
                "Continue proper watering, sunlight, nutrition "
                "and regular monitoring."
            )

        else:

            st.warning(
                "⚠️ Possible disease detected. "
                "Check the affected leaves and follow suitable "
                "plant-care practices."
            )

            if disease_name in disease_info:

                info = disease_info[disease_name]

                st.subheader("🩺 Symptoms")
                st.info(info["symptoms"])

                st.subheader("🌱 Care")
                st.write(info["care"])

                st.subheader("🛡️ Prevention")
                st.write(info["prevention"])

            st.subheader("🌱 Recommended Care")

            st.write(
                "• Remove severely affected leaves.\n"
                "• Avoid unnecessary watering on the leaves.\n"
                "• Provide proper sunlight and air circulation.\n"
                "• Keep infected plant material away from healthy plants.\n"
                "• Monitor the plant regularly for changes."
            )


# -----------------------------
# How It Works Section
# -----------------------------
elif section == "ℹ️ How It Works":

    st.header("⚙️ How PlantCare AI Works")

    st.write(
        "PlantCare AI uses an artificial intelligence model "
        "to analyze an uploaded plant leaf image and predict "
        "the possible plant disease."
    )

    st.subheader("🔄 Detection Process")

    st.info("1️⃣ Upload a clear image of a plant leaf.")

    st.info("2️⃣ The image is converted into a suitable format.")

    st.info("3️⃣ The image is resized to 224 × 224 pixels.")

    st.info("4️⃣ The trained AI model analyzes the image.")

    st.info("5️⃣ The model predicts the most likely disease class.")

    st.info("6️⃣ PlantCare AI displays the prediction and confidence.")

    st.info(
        "7️⃣ If a disease is detected, symptoms, care and "
        "prevention information is provided."
    )

    st.subheader("🧠 AI Model")

    st.write(
        "The system uses a trained deep learning image "
        "classification model for plant disease detection."
    )

    st.write(
        "The model was trained using labeled plant leaf images "
        "and can recognize multiple plant disease categories."
    )


# -----------------------------
# About Section
# -----------------------------
elif section == "📖 About":

    st.header("📖 About PlantCare AI")

    st.write(
        "PlantCare AI is an AI-based plant disease detection "
        "and intelligent plant care system developed as a "
        "BCA project."
    )

    st.subheader("🎯 Project Objective")

    st.write(
        "The main objective of PlantCare AI is to help users "
        "identify possible plant diseases from leaf images "
        "and provide useful plant-care guidance."
    )

    st.subheader("✨ Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🔬 AI-Based Detection")
        st.info("📊 Confidence Analysis")
        st.info("🩺 Disease Information")

    with col2:
        st.info("🌱 Care Guidance")
        st.info("🛡️ Prevention Tips")
        st.info("📷 Image Analysis")

    st.subheader("💻 Technologies Used")

    st.write(
        "• Python\n"
        "• Streamlit\n"
        "• TensorFlow\n"
        "• NumPy\n"
        "• Pillow (PIL)\n"
        "• Deep Learning / Image Classification"
    )

    st.success(
        "🌱 PlantCare AI combines artificial intelligence "
        "with practical plant-care information to support "
        "early disease identification."
    )


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "PlantCare AI • AI-Based Plant Disease Detection and Intelligent Plant Care System"
)