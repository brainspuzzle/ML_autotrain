import os
import json

class AnnotationExporter:
    def __init__(self, annotations_dir, output_file):
        self.annotations_dir = annotations_dir
        self.output_file = output_file

    def export_to_json(self):
        data = {}
        for annotation_file in os.listdir(self.annotations_dir):
            file_name = os.path.splitext(annotation_file)[0]
            file_path = os.path.join(self.annotations_dir, annotation_file)
            with open(file_path, "r") as f:
                lines = f.readlines()
                light_sources = []
                for line in lines:
                    parts = line.strip().split()
                    if parts:
                        light_source = {
                            "class_id": int(parts[0]),
                            "x_center": float(parts[1]),
                            "y_center": float(parts[2]),
                            "width": float(parts[3]),
                            "height": float(parts[4]),
                            "intensity": float(parts[5]),
                            "color_r": int(parts[6]),
                            "color_g": int(parts[7]),
                            "color_b": int(parts[8]),
                            "radius": float(parts[9]),
                        }
                        light_sources.append(light_source)
                data[file_name] = light_sources

        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Anotacijos eksportuotos į JSON formatą: {self.output_file}")

# Naudojimas
if __name__ == "__main__":
    exporter = AnnotationExporter("data/annotations", "data/light_sources.json")
    exporter.export_to_json()

