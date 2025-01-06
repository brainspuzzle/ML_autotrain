import os
import shutil
from pathlib import Path


class ImagePreparer:
    def __init__(self, source_dir, destination_dir, supported_formats):
        self.source_dir = Path(source_dir).resolve()
        self.destination_dir = Path(destination_dir).resolve()
        self.supported_formats = supported_formats

    def prepare_images(self):
        # Sukuriame išvesties katalogą, jei jo nėra
        self.destination_dir.mkdir(parents=True, exist_ok=True)

        # Tikriname, ar šaltinio katalogas egzistuoja
        if not self.source_dir.exists():
            print(f"Klaida: šaltinio katalogas '{self.source_dir}' neegzistuoja.")
            return

        # Perkeliame vaizdo failus
        for file in self.source_dir.iterdir():
            if file.suffix.lower() in self.supported_formats:
                destination_file = self.destination_dir / file.name
                shutil.copy2(file, destination_file)
                print(f"Vaizdas perkeltas: {file.name}")

        print("Visi vaizdai paruošti.")


# Naudojimas
if __name__ == "__main__":
    # Grįžtame per katalogą naudodami `../`
    preparer = ImagePreparer("../data/raw_images", "../data/prepared_images", [".jpg", ".jpeg", ".png"])
    preparer.prepare_images()