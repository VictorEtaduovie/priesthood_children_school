# =========================================================
# IMAGE TO WEBP CONVERTER
# Converts JPG, JPEG, and PNG to WEBP
# =========================================================

from PIL import Image
import os

# =========================================================
# FOLDERS
# =========================================================

input_folder = "images/jpg"
output_folder = "images/webp"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# =========================================================
# LOOP THROUGH FILES
# =========================================================

for filename in os.listdir(input_folder):

    # Check supported image formats
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        # Full input path
        input_path = os.path.join(input_folder, filename)

        # Remove old extension
        name_without_extension = os.path.splitext(filename)[0]

        # Output WEBP path
        output_path = os.path.join(
            output_folder,
            f"{name_without_extension}.webp"
        )

        try:
            # Open image
            image = Image.open(input_path)

            # Convert RGBA if needed
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            # Save as WEBP
            image.save(
                output_path,
                "WEBP",
                quality=85,
                optimize=True
            )

            print(f"Converted: {filename}")

        except Exception as e:
            print(f"Error converting {filename}: {e}")

print("\nAll images converted successfully!")