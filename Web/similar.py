import cv2
import numpy as np
import os
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from sklearn.metrics.pairwise import cosine_similarity

# Load Pre-trained Model (ResNet50 without top layers)
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Function to extract features
def extract_features(image_path, model):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    features = model.predict(image)
    return features.flatten()

# Step 1: Build a feature database
def build_feature_database(dataset_folder, model):
    feature_db = {}
    for category in os.listdir(dataset_folder):
        category_path = os.path.join(dataset_folder, category)
        if os.path.isdir(category_path):  # Check if it's a folder
            print(f"Processing subfolder: {category}")  # Print subfolder name
            for filename in os.listdir(category_path):
                if filename.endswith(('.jpg', '.png', '.jpeg', '.webp')):
                    file_path = os.path.join(category_path, filename)
                    features = extract_features(file_path, model)
                    feature_db[file_path] = features
    return feature_db

# Step 2: Find the most similar image
def find_similar_image(uploaded_image_path, feature_db, model):
    uploaded_features = extract_features(uploaded_image_path, model)
    max_similarity = -1
    most_similar_image = None

    for file_path, features in feature_db.items():
        similarity = cosine_similarity([uploaded_features], [features])[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_image = file_path

    return most_similar_image, max_similarity

# Main Execution
if __name__ == "__main__":
    dataset_folder = "dataset"  # Replace with your dataset folder path
    uploaded_image_path = r"D:\Amal kalarickal\Check Image Similarity ML\Check Image Similarity ML\pp.webp"  # Replace with your uploaded image path

    print("Building feature database...")
    feature_db = build_feature_database(dataset_folder, model)

    print("Finding similar image...")
    similar_image, similarity_score = find_similar_image(uploaded_image_path, feature_db, model)
    
    if similar_image:
        # Extract the folder name from the file path
        folder_name = os.path.basename(os.path.dirname(similar_image))
        print(f"Most similar image: {similar_image} (Similarity Score: {similarity_score:.4f})")
        print(f"Located in folder: {folder_name}")
    else:
        print("No similar image found.")
