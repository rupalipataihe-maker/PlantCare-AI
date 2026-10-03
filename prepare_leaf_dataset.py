import os
import shutil

SOURCE_FOLDER = "dataset/color"
DEST_FOLDER = "dataset/leaf_validation/leaf"

MAX_IMAGES = 500

image_extensions = (
    ".jpg",
    ".jpeg",
    ".png"
)

os.makedirs(DEST_FOLDER, exist_ok=True)

count = 0

for folder_name in os.listdir(SOURCE_FOLDER):

    folder_path = os.path.join(
        SOURCE_FOLDER,
        folder_name
    )

    # Sirf original disease folders ko process karo
    if not os.path.isdir(folder_path):
        continue

    # leaf_validation ko skip karo
    if folder_name == "leaf_validation":
        continue

    for file_name in os.listdir(folder_path):

        if file_name.lower().endswith(image_extensions):

            source_path = os.path.join(
                folder_path,
                file_name
            )

            destination_path = os.path.join(
                DEST_FOLDER,
                f"leaf_{count + 1}.jpg"
            )

            shutil.copy2(
                source_path,
                destination_path
            )

            count += 1

            if count >= MAX_IMAGES:
                break

    if count >= MAX_IMAGES:
        break

print(f"Successfully copied {count} leaf images.")