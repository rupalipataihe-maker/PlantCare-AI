import os
import numpy as np
from PIL import Image
import tensorflow as tf

DEST_FOLDER = "dataset/leaf_validation/non_leaf"
MAX_IMAGES = 500

os.makedirs(DEST_FOLDER, exist_ok=True)

print("Downloading CIFAR-10 dataset...")

(x_train, y_train), _ = tf.keras.datasets.cifar10.load_data()

count = 0

for image_array in x_train:

    image = Image.fromarray(image_array)
    image = image.resize((224, 224))

    save_path = os.path.join(
        DEST_FOLDER,
        f"non_leaf_{count + 1}.jpg"
    )

    image.save(save_path)

    count += 1

    if count >= MAX_IMAGES:
        break

print(f"Successfully created {count} non-leaf images.")