import os
from tkinter import Tk, filedialog
from PIL import Image
import piexif

def extract_metadata():
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
            # Load the EXIF metadata
            exif_dict = piexif.load(img.info['exif'])

            # Print the metadata
            for ifd_name in exif_dict:
                print(f"\n{ifd_name} Metadata:")
                for tag, value in exif_dict[ifd_name].items():
                    tag_name = piexif.TAGS[ifd_name].get(tag, {}).get('name', tag)
                    print(f"  {tag_name}: {value}")
        else:
            print(f"No EXIF metadata found in {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
extract_metadata()
