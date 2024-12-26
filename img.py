import os
from tkinter import Tk, filedialog
from PIL import Image
import piexif

def remove_metadata():
    # Open a file dialog to select an image file
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Bring the dialog to the front
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.tiff"), ("All Files", "*.*")]
    )
    root.destroy()  # Close the root window

    if not file_path:
        print("No file selected. Exiting.")
        return

    try:
        # Open the image using Pillow
        img = Image.open(file_path)

        # Check if the image has EXIF metadata
        if "exif" in img.info:
            # Load the current EXIF metadata
            exif_dict = piexif.load(img.info['exif'])

            # Create an empty EXIF dictionary
            empty_exif = piexif.dump({})

            # Save the image with empty EXIF metadata
            img.save(file_path, exif=empty_exif)
            print(f"Metadata removed from {file_path}")
        else:
            print(f"No EXIF metadata found in {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
remove_metadata()
