import cv2
import os
import numpy as np


class AnnotationGenerator:
    def __init__(self, source_dir, annotations_dir, brightness_threshold=200, min_blob_area=5):
        self.source_dir = source_dir
        self.annotations_dir = annotations_dir
        self.brightness_threshold = brightness_threshold
        self.min_blob_area = min_blob_area
        os.makedirs(self.annotations_dir, exist_ok=True)

    def generate_annotations(self):
        for image_file in os.listdir(self.source_dir):
            image_path = os.path.join(self.source_dir, image_file)
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(gray, self.brightness_threshold, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            annotation_path = os.path.join(
                self.annotations_dir, f"{os.path.splitext(image_file)[0]}.txt"
            )
            with open(annotation_path, "w") as f:
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
                            f"0 {cx} {cy} {norm_w} {norm_h} {max_intensity / 255:.4f} "
                            f"{int(mean_color[0])} {int(mean_color[1])} {int(mean_color[2])} {normalized_radius:.4f}\n"
                        )

            print(f"Anotacijos sukurtos: {annotation_path}")


# Naudojimas
if __name__ == "__main__":
    generator = AnnotationGenerator("data/prepared_images", "data/annotations")
    generator.generate_annotations()
