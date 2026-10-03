🌱 PlantCare AI

AI-Based Plant Disease Detection and Intelligent Plant Care System.

About the Project

PlantCare AI is a deep learning-based application that detects plant diseases from leaf images and provides disease information, symptoms, care suggestions, prevention tips, and prediction confidence.

Technologies Used

- Python
- TensorFlow
- Streamlit
- NumPy
- Pillow

Main Features

- Plant leaf image upload
- Leaf validation
- Plant disease detection
- Prediction confidence
- Top 3 predictions
- Disease symptoms
- Care suggestions
- Prevention tips
- Simple Streamlit interface

How to Run

1. Clone the repository

git clone https://github.com/rupalipataihe-maker/PlantCare-AI.git
cd PlantCare-AI

2. Create a virtual environment

python -m venv .venv

3. Activate the virtual environment

Windows:

.venv\Scripts\activate

4. Install required libraries

pip install -r requirements.txt

5. Download the required model files

Download the trained model files from Google Drive:

[Download PlantCare AI Models](https://drive.google.com/drive/folders/1SItGeuRQMv8Hbo9tonBfOdTVVt2wTbxN?usp=sharing)

After downloading, place both files inside the `model` folder:

- plant_disease_model.keras
- leaf_validator.keras

6. Run the application

python -m streamlit run app/main.py

The application will open in the browser.

Project Structure

PlantCare-AI/
│
├── app/
│   ├── main.py
│   └── test.py
│
├── model/
│   ├── predict.py
│   └── train_model.py
│
├── prepare_leaf_dataset.py
├── prepare_non_leaf_dataset.py
├── test_leaf_validator.py
├── train_leaf_validator.py
├── requirements.txt
├── README.md
└── .gitignore

Note

The trained model files and dataset are not stored in this GitHub repository because of their large size. They need to be provided separately when setting up the project on another computer.