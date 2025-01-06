import os

class ModelExporter:
    def __init__(self, weights, img_size=640, device="cpu"):
        self.weights = weights
        self.img_size = img_size
        self.device = device

    def export_to_onnx(self):
        export_command = (
            f"python yolov7/export.py "
            f"--weights {self.weights} "
            f"--grid --simplify --dynamic "
            f"--img-size {self.img_size} "
            f"--device {self.device} "
            f"--format onnx"
        )
        os.system(export_command)
        print("Modelis eksportuotas į ONNX formatą.")

# Naudojimas
if __name__ == "__main__":
    exporter = ModelExporter("models/light_detection/best.pt")
    exporter.export_to_onnx()

