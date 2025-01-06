import os

class ModelEvaluator:
    def __init__(self, config_file, weights, img_size=640):
        self.config_file = config_file
        self.weights = weights
        self.img_size = img_size

    def evaluate(self):
        evaluate_command = (
            f"python yolov7/val.py "
            f"--data {self.config_file} "
            f"--weights {self.weights} "
            f"--img {self.img_size}"
        )
        os.system(evaluate_command)
        print("Modelio įvertinimas baigtas.")

# Naudojimas
if __name__ == "__main__":
    evaluator = ModelEvaluator("config.yaml", "models/light_detection/best.pt")
    evaluator.evaluate()
