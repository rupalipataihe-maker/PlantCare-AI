import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Load Leaf Validator Model
# -----------------------------
MODEL_PATH = "model/leaf_validator.keras"

model = tf.keras.models.load_model(MODEL_PATH)

# -----------------------------
# Image to Test
# -----------------------------
IMAGE_PATH = "dataset/leaf_validation/leaf/leaf kareli.jpeg"
# -----------------------------
# Load Image
# -----------------------------
image = Image.open(IMAGE_PATH).convert("RGB")
image = image.resize((224, 224))

img_array = np.array(image)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(
    img_array,
    verbose=0
)

score = float(prediction[0][0])

# -----------------------------
# Result
# -----------------------------
if score >= 0.5:

    print("Prediction: Leaf")
    print(f"Confidence: {score * 100:.2f}%")

else:

    print("Prediction: Non-Leaf")
    print(f"Confidence: {(1 - score) * 100:.2f}%")