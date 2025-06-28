import os

# Specify the directory containing the images
image_directory = 'C:\Module9\Project\module9-dsai\kartezio_workspace\heart\data\data\images'

# Loop through all files in the directory
for index, filename in enumerate(os.listdir(image_directory)):
    # Construct the full file path
    old_file_path = os.path.join(image_directory, filename)
    
    # Check if the file is an image (optional, based on your image extensions)
    if filename.endswith(('.png')):
        # Create a new file name with a prefix and index
        new_filename = f'image_{index+1}.png'  # Adjust the extension as needed
        
        # Construct the new file path
        new_file_path = os.path.join(image_directory, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed {old_file_path} to {new_file_path}')
