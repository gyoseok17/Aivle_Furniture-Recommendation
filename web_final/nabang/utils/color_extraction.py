# # 01-1.
# # for User image
# # This Python file is intended to extract colors(3) and percentages from website input image!!!!
# # used: scikit-learn for KMeans
# # without nugi

# # Frequency of each cluster(n=3)
# import numpy as np
# from matplotlib import image as mp_image
# from matplotlib import pyplot as plt
# from sklearn.cluster import KMeans
# # from cuml.cluster import KMeans
# from PIL import Image
# import io
# import numpy as np
# from matplotlib import image as mp_image
# from sklearn.cluster import KMeans
# from PIL import Image
# import io


# def extract_ordered_dominant_colors(image_file, num_colors):
#     # Load and normalize image
#     # image = mp_image.imread(image_file) / 255.0
#     image = Image.open(io.BytesIO(image_file.read()))
#     image = np.array(image) / 255.0
#     # plt.imshow(image)
#     # plt.axis('off')
#     # plt.show()

#     # Reshape the image to be a list of pixels
#     pixels = image.reshape(-1, 3)
    
#     # Use KMeans to find main colors
#     model = KMeans(n_clusters=num_colors)
#     model.fit(pixels)
    
#     # Get the colors and labels
#     colors = model.cluster_centers_
#     labels = model.labels_
    
#     # Count labels to find the frequency of each cluster
#     count_labels = np.bincount(labels)
#     total_pixels = len(pixels)
    
#     # Calculate the percentage of each cluster
#     percentages = 100 * count_labels / total_pixels
#     percentages_rounded = np.round(percentages, 2)  # Round to 2 decimal places
    
#     # Order the clusters by their frequency (most common first)
#     ordered_indices = np.argsort(count_labels)[::-1]  # Descending order
#     ordered_colors = colors[ordered_indices]
#     ordered_percentages = percentages_rounded[ordered_indices]
    
#     # Display the ordered dominant colors
#     # plt.figure(figsize=(num_colors, 2))
#     # for i, color in enumerate(ordered_colors):
#     #     plt.subplot(1, num_colors, i+1)
#     #     plt.imshow([[color]])
#     #     plt.axis('off')
#     # plt.show()
    
#     return ordered_colors, ordered_percentages

# # # Use the function
# # image_file = r'C:\Users\user\amazon\Detection\team5\Color_Extraction\test_images\AAIRLLENSleekandSturdyInchComputerDeskPerfectforWorkandStudyMultiPurposeTableforWritingDiningandWorkstation.jpg'
# # num_colors = 3

# # ordered_dominant_colors, ordered_percentages = extract_ordered_dominant_colors(image_file, num_colors)

# # print("Ordered Dominant Colors:\n", ordered_dominant_colors)
# # print("Percentage of each color (rounded):\n", ordered_percentages)

import numpy as np
from sklearn.cluster import KMeans
# from cuml.cluster import KMeans
from PIL import Image
import io
# import cupy
import gc
# import numba

import time
def extract_ordered_dominant_colors(image_file, num_colors):
    # time.sleep(0.1)
    # Assuming image_file is your image file object
    image = Image.open(io.BytesIO(image_file.read()))

    # Convert the image to a NumPy array
    image_np = np.array(image) / 255.0

    # Check the image format and process accordingly
    if image.mode == 'RGBA':  # If the image is RGBA
        # Keep only RGB values, discard the alpha channel
        pixels = image_np.reshape(-1, 4)[:, :3]
    elif image.mode == 'RGB':  # If the image is RGB
        pixels = image_np.reshape(-1, 3)
    
    # Use KMeans to find main colors
    model = KMeans(n_clusters=num_colors, n_init=10)
    model.fit(pixels)
    
    # Get the colors and labels
    colors = model.cluster_centers_
    labels = model.labels_
        
    # Count labels to find the frequency of each cluster
    count_labels = np.bincount(labels)
    total_pixels = len(pixels)
    
    # Calculate the percentage of each cluster
    percentages = 100 * count_labels / total_pixels
    percentages_rounded = np.round(percentages, 2)  # Round to 2 decimal places
    
    # Order the clusters by their frequency (most common first)
    ordered_indices = np.argsort(count_labels)[::-1]  # Descending order
    ordered_colors = colors[ordered_indices].tolist()
    ordered_percentages = percentages_rounded[ordered_indices].tolist()
    # ordered_colors = colors[ordered_indices]
    # ordered_percentages = percentages_rounded[ordered_indices]
    result =[]
    for i in range(3):
        result.append([ordered_colors[i], ordered_percentages[i]])
        
    # Free CuPy memory pool
    # cupy.get_default_memory_pool().free_all_blocks()
    # del model
    # del pixels
    # del colors
    # del labels
    # gc.collect()
    # numba.cuda.close()
    
    return result
    # return 0, 0

# print(extract_ordered_dominant_color())