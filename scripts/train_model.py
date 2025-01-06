import os

class ModelTrainer:
    def __init__(self, config_file, model_cfg, weights, epochs, project_dir, model_name):
        self.config_file = config_file
        self.model_cfg = model_cfg
        self.weights = weights
        self.epochs = epochs
        self.project_dir = project_dir
        self.model_name = model_name

    def train(self):
        train_command = (
            f"/Users/ciniminis/PycharmProjects/ML_auto_training_tool/.venv/bin/python3 "
            f"../yolov7/train.py "
            f"--data {self.config_file} "
            f"--cfg {self.model_cfg} "
            f"--weights {self.weights} "
            f"--epochs {self.epochs} "
            f"--project {self.project_dir} "
            f"--name {self.model_name}"
        )
        os.system(train_command)
        print("Modelio treniravimas baigtas.")

# Naudojimas
if __name__ == "__main__":
    trainer = ModelTrainer(
        "config.yaml", "yolov7-tiny.yaml", "yolov7-tiny.pt", 50, "models/", "light_detection"
    )
    trainer.train()

