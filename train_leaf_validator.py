import tensorflow as tf
from tensorflow.keras import layers, models
import os

# -----------------------------
# Dataset Paths
# -----------------------------
DATASET_PATH = "dataset/leaf_validation"

# -----------------------------
# Image Settings
# -----------------------------
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# -----------------------------
# Load Dataset
# -----------------------------
train_dataset = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

# -----------------------------
# Dataset Optimization
# -----------------------------
AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(
    buffer_size=AUTOTUNE
)

validation_dataset = validation_dataset.prefetch(
    buffer_size=AUTOTUNE
)

# -----------------------------
# Build Model
# -----------------------------
model = models.Sequential([

    layers.Rescaling(
        1.0 / 255,
        input_shape=(224, 224, 3)
    ),

    layers.Conv2D(
        32,
        (3, 3),
        activation="relu"
    ),

    layers.MaxPooling2D(),

    layers.Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),

    layers.MaxPooling2D(),

    layers.Conv2D(
        128,
        (3, 3),
        activation="relu"
    ),

    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(
        128,
        activation="relu"
    ),

    layers.Dropout(0.3),

    layers.Dense(
        1,
        activation="sigmoid"
    )
])

# -----------------------------
# Compile Model
# -----------------------------
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# -----------------------------
# Model Summary
# -----------------------------
model.summary()

# -----------------------------
# Train Model
# -----------------------------
print("\nStarting Leaf vs Non-Leaf model training...\n")

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)

# -----------------------------
# Save Model
# -----------------------------
os.makedirs(
    "model",
    exist_ok=True
)

MODEL_PATH = "model/leaf_validator.keras"

model.save(MODEL_PATH)

print("\n--------------------------------")
print("Leaf Validator Training Complete!")
print("--------------------------------")
print(f"Model saved successfully at: {MODEL_PATH}")