import cv2
import numpy as np
from kartezio.dataset import read_dataset
from kartezio.easy import load_model
from numena.image.drawing import draw_overlay


MODEL_FILE = "models/45_images/331539-d865b1d3-1901-42f1-948e-e349665805ab/elite.json"
DATASET_FOLDER = "dataset"
OUTPUT_FOLDER = "predictions"


def main():
    model = load_model(MODEL_FILE)
    dataset = read_dataset(DATASET_FOLDER, counting=True, preview=True)
    p_train, _ = model.predict(dataset.train_x)
    for i, pi in enumerate(p_train):
        overlayed = draw_overlay(
            dataset.train_v[i],
            pi["mask"].astype(np.uint8),
            color=[128, 0, 0],
            alpha=0.6,
            thickness=2,
        )
        cv2.imwrite(f"{OUTPUT_FOLDER}/train_{i}.png", overlayed)
        cv2.imwrite(f"{OUTPUT_FOLDER}/train_{i}_mask.png", pi["mask"].astype(np.uint8))

    p_test, _ = model.predict(dataset.test_x)
    for i, pi in enumerate(p_test):
        overlayed = draw_overlay(
            dataset.test_v[i],
            pi["mask"].astype(np.uint8),
            color=[128, 0, 0],
            alpha=0.6,
            thickness=2,
        )
        cv2.imwrite(f"{OUTPUT_FOLDER}/test_{i}.png", overlayed)

if __name__ == "__main__":
    main()