import os
import uuid
from typing import List
from fastapi import UploadFile


def save_uploaded_image(image: UploadFile, folder: str) -> str:
    os.makedirs(folder, exist_ok=True)
    filename, file_extension = os.path.splitext(image.filename)
    unique_filename = f"{filename}_{str(uuid.uuid4())}{file_extension}"
    image_path = os.path.join(folder, unique_filename)
    with open(image_path, "wb") as image_file:
        image_file.write(image.file.read())

    return f"{folder}{unique_filename}"


def delete_file(file_path: str):
    """Delete the specified file from the filesystem."""
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
