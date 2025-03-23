from PIL import Image
from pathlib import Path
from tqdm import tqdm

# required to open heic-formatted images
from pillow_heif import register_heif_opener
register_heif_opener()

HEIC_DIRECTORY = Path("fotos")
JPG_DIRECTORY = Path("fotos/jpg")

for image_file in tqdm(HEIC_DIRECTORY.glob("*.HEIC")):
    heic_image = Image.open(image_file)
    jpg_image_name = JPG_DIRECTORY / f"{image_file.stem}.jpg"
    heic_image.save(jpg_image_name, "JPEG", quality=100)
 
input("Press Enter to exit...")
