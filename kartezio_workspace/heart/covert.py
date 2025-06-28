import nibabel as nib
from PIL import Image
import numpy as np
import os

# List of image and label paths
image_files = [
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_007.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_019.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_023.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_005.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_009.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_017.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_021.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_029.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_003.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_011.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_030.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_022.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_014.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_018.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_020.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_004.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_016.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_024.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_010.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/imagesTr/la_026.nii.gz"
]

label_files = [
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_007.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_019.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_023.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_005.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_009.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_017.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_021.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_029.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_003.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_011.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_030.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_022.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_014.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_018.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_020.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_004.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_016.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_024.nii.gz",
    "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_010.nii.gz", "C:/Module9/Project/module9-dsai/dataset/Task02_Heart/labelsTr/la_026.nii.gz"
]

# Directory to save the converted files
output_dir = "C:\\Module9\\Project\\module9-dsai\\kartezio_workspace\\heart\\dataset_tif"
os.makedirs(output_dir, exist_ok=True)

# Function to save the middle slice of image and label
def save_middle_slice(image_path, label_path):
    # Load image
    img_nii = nib.load(image_path)
    img_data = img_nii.get_fdata()
    
    # Load label
    label_nii = nib.load(label_path)
    label_data = label_nii.get_fdata()

    # Calculate the middle index
    middle_index = img_data.shape[2] // 2

    # Extract the middle slice for image
    img_slice = img_data[:, :, middle_index]
    
    # Normalize the image slice to 0-255 for saving as .tif
    img_slice_normalized = (img_slice - np.min(img_slice)) / (np.max(img_slice) - np.min(img_slice)) * 255
    img_slice_uint8 = img_slice_normalized.astype(np.uint8)
    
    # Extract the middle slice for label
    label_slice = label_data[:, :, middle_index]
    label_mask = (label_slice > 0).astype(np.uint8) * 255  # Convert to binary mask (0 or 255)

    # Save the image slice
    img = Image.fromarray(img_slice_uint8)
    img_output_path = os.path.join(output_dir, f"{os.path.basename(image_path).split('.')[0]}_.tif")
    img.save(img_output_path)
    print(f"Saved {img_output_path}")

    # Save the label slice
    label_img = Image.fromarray(label_mask)
    label_output_path = os.path.join(output_dir, f"{os.path.basename(label_path).split('.')[0]}_mask.tif")
    label_img.save(label_output_path)
    print(f"Saved {label_output_path}")

# Process all images and labels
for img_file, lbl_file in zip(image_files, label_files):
    save_middle_slice(img_file, lbl_file)
