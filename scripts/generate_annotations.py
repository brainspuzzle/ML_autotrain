import cv2
import numpy as np
from pathlib import Path


class AnnotationGenerator:
    def __init__(self, source_dir, annotations_dir, brightness_threshold=200, min_blob_area=5):
        self.source_dir = Path(source_dir).resolve()
        self.annotations_dir = Path(annotations_dir).resolve()
        self.brightness_threshold = brightness_threshold
        self.min_blob_area = min_blob_area
        self.annotations_dir.mkdir(parents=True, exist_ok=True)

    def generate_annotations(self):
        total_files = 0
        total_annotations = 0

        # Tikriname, ar šaltinio katalogas egzistuoja
        if not self.source_dir.exists():
            print(f"Klaida: šaltinio katalogas '{self.source_dir}' neegzistuoja.")
            return

        for image_file in self.source_dir.iterdir():
            # Tikriname, ar failas yra vaizdas
            if not image_file.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                continue

            try:
                image = cv2.imread(str(image_file))
                if image is None:
                    print(f"Klaida nuskaitant failą: {image_file.name}")
                    continue

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(
                    gray, self.brightness_threshold, 255, cv2.THRESH_BINARY
                )
                contours, _ = cv2.findContours(
                    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
                )

                annotation_path = self.annotations_dir / f"{image_file.stem}.txt"
                with annotation_path.open("w") as f:
                    h, w = image.shape[:2]
                    for cnt in contours:
                        if cv2.contourArea(cnt) > self.min_blob_area:
                            x, y, w_box, h_box = cv2.boundingRect(cnt)
                            cx = (x + w_box / 2) / w
                            cy = (y + h_box / 2) / h
                            norm_w = w_box / w
                            norm_h = h_box / h

                            mask = np.zeros(gray.shape, dtype=np.uint8)
                            cv2.drawContours(mask, [cnt], -1, (255), -1)
                            max_intensity = np.max(gray[mask > 0])
                            mean_color = cv2.mean(image, mask=mask)[:3]
                            center, radius = cv2.minEnclosingCircle(cnt)
                            normalized_radius = radius / max(w, h)

                            f.write(
                                f"0 {cx:.4f} {cy:.4f} {norm_w:.4f} {norm_h:.4f} "
                                f"{max_intensity / 255:.4f} {int(mean_color[0])} "
                                f"{int(mean_color[1])} {int(mean_color[2])} {normalized_radius:.4f}\n"
                            )
                            total_annotations += 1

                print(f"Anotacijos sukurtos: {annotation_path.name}")
                total_files += 1
            except Exception as e:
                print(f"Klaida apdorojant failą {image_file.name}: {e}")

        print(f"Iš viso apdorota failų: {total_files}")
        print(f"Iš viso sugeneruota anotacijų: {total_annotations}")


# Naudojimas
if __name__ == "__main__":
    # Grįžtame per direktorijas naudodami `../`
    generator = AnnotationGenerator("../data/prepared_images", "../data/annotations")
    generator.generate_annotations()
