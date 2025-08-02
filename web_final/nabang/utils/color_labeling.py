import pickle
import os
from pathlib import Path
from PIL import Image

import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent   # web
# Load the model
with open(os.path.join(BASE_DIR,'nabang','utils','kmeans_model.pkl'), 'rb') as file:
    kmeans_model = pickle.load(file)
    
def color_label(image):
    print(-1)
    img_pil = Image.open(image)
    # Convert the image to a NumPy array
    image_array = np.array(img_pil)
    # Ensure the image has three channels (remove alpha channel if present)
    if len(image_array.shape) == 3 and image_array.shape[-1] == 4:
        image_array = image_array[:, :, :3]
        
    # Normalize the image
    image_array = image_array / 255.0
    # Flatten the image array
    pixels = image_array.reshape(-1, image_array.shape[-1])
    
    # Ensure pixels array is not empty
    if len(pixels) == 0:
        return None  # Handle the case where pixels array is empty
    
    # Predict the cluster label for each pixel
    labels = kmeans_model.predict(pixels)
    # Determine the most frequent label
    label_counts = np.bincount(labels)
    dominant_label = np.argmax(label_counts)
    
    return str(dominant_label)