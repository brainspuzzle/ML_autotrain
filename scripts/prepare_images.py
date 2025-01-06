import os
import shutil
from pathlib import Path

class ImagePreparer:
    def __init__(self, source_dir, destination_dir, supported_formats):
        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.supported_formats = supported_formats

    def prepare_images(self):
        os.makedirs(self.destination_dir, exist_ok=True)
        for file in os.listdir(self.source_dir):
            if Path(file).suffix.lower() in self.supported_formats:
                shutil.copy2(
                    os.path.join(self.source_dir, file),
                    os.path.join(self.destination_dir, file),
                )
                print(f"Vaizdas perkeltas: {file}")
        print("Visi vaizdai paruošti.")

# Naudojimas
if __name__ == "__main__":
    preparer = ImagePreparer("data/raw_images", "data/prepared_images", [".jpg", ".jpeg", ".png"])
    preparer.prepare_images()
