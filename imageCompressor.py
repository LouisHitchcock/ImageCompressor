import os
import json
from PIL import Image

def compress_and_downscale_images(input_folder, output_folder=None, quality=85, max_width=1000):
    # Ensure the input folder exists
    if not os.path.isdir(input_folder):
        print(f"The input folder '{input_folder}' does not exist.")
        return

    # If output_folder is not specified, overwrite the input images
    if output_folder is None:
        output_folder = input_folder
    else:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

    # Get list of files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # JSON file to keep track of processed images (saved in script directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_images_path = os.path.join(script_dir, "images.json")
    processed_data = {"processed": []}
    if os.path.exists(processed_images_path):
        try:
            with open(processed_images_path, "r") as f:
                content = f.read().strip()
                if content:
                    processed_data = json.loads(content)
        except json.JSONDecodeError:
            print("Warning: images.json is invalid. Reinitializing it.")

    for file in files:
        try:
            # Open the image file
            with Image.open(os.path.join(input_folder, file)) as img:
                # Calculate the new size while maintaining aspect ratio
                width_percent = (max_width / float(img.size[0]))
                new_height = int((float(img.size[1]) * float(width_percent)))
                new_size = (max_width, new_height)

                # Downscale the image if it's wider than max_width
                if img.size[0] > max_width:
                    img = img.resize(new_size, Image.Resampling.LANCZOS)

                # Compress and save the image
                output_path = os.path.join(output_folder, file)
                img.save(output_path, quality=quality, optimize=True)
                print(f"Compressed and downscaled '{file}' successfully.")

                # Add to processed list if not already there
                if file not in processed_data["processed"]:
                    processed_data["processed"].append(file)
        except Exception as e:
            print(f"Error processing '{file}': {e}")

    # Save updated JSON
    with open(processed_images_path, "w") as f:
        json.dump(processed_data, f, indent=4)

if __name__ == "__main__":
    input_folder = input("Enter input folder path (default: ./uncompressed/): ").strip() or "./uncompressed/"
    output_folder = input("Enter output folder path (default: ./compresssed/): ").strip() or "./compresssed/"

    while True:
        try:
            quality = int(input("Enter quality (1-100, default: 85): ").strip() or 85)
            if 1 <= quality <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            max_width = int(input("Enter max width in pixels (default: 1000): ").strip() or 1000)
            if max_width > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

    compress_and_downscale_images(input_folder, output_folder, quality=quality, max_width=max_width)