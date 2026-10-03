import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load trained model
model = tf.keras.models.load_model("model/plant_disease_model.keras")

print("Model loaded successfully!")

# Image path
image_path = input("Enter the path of plant image: ")

# Check if image exists
if not os.path.exists(image_path):
    print("Image not found!")
    exit()

# Load and prepare image
img = Image.open(image_path).convert("RGB")
img = img.resize((224, 224))

# Convert image to array
img_array = np.array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Make prediction
prediction = model.predict(img_array)

predicted_class = np.argmax(prediction[0])

dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Dataset", "color"))

class_names = sorted([
    folder for folder in os.listdir(dataset_path)
    if os.path.isdir(os.path.join(dataset_path, folder))
])

print("Predicted Disease:", class_names[predicted_class])

print("Predicted class index:", predicted_class)
print("Prediction completed successfully!")