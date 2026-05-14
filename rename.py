# =========================================================
# AUTO RENAME ALL IMAGES
# Renames images to:
# priesthood-children-school-1.webp
# priesthood-children-school-2.webp
# etc.
# =========================================================

import os

# =========================================================
# FOLDER CONTAINING YOUR IMAGES
# =========================================================

folder = "images/webp"

# =========================================================
# GET ALL IMAGE FILES
# =========================================================

files = [
    file for file in os.listdir(folder)
    if file.lower().endswith(".webp")
]

# Sort files alphabetically
files.sort()

# =========================================================
# RENAME FILES
# =========================================================

for index, file in enumerate(files, start=1):

    # Old file path
    old_path = os.path.join(folder, file)

    # New filename
    new_name = f"priesthood-children-school-{index}.webp"

    # New file path
    new_path = os.path.join(folder, new_name)

    # Rename file
    os.rename(old_path, new_path)

    print(f"Renamed: {file} --> {new_name}")

print("\nAll files renamed successfully!")