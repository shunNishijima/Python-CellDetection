import cv2
import numpy as np
from numena.image.drawing import draw_overlay
from kartezio.apps.segmentation import create_segmentation_model
from kartezio.dataset import read_dataset
from kartezio.endpoint import EndpointThreshold
from kartezio.export import GenomeToPython
from kartezio.training import train_model

dataset_path = "C:/Module9/Project/module9-dsai/kartezio_workspace/heart/ex_data"


def create_model(n_inputs):
    n_iterations = 20000
    n_children = 5
    n_nodes = 30
    model = create_segmentation_model(
        n_iterations,
        n_children,
        inputs=n_inputs,
        nodes=n_nodes,
        endpoint=EndpointThreshold(128),
    )
    return model


def main():
    destination_directory = "C:/Module9/Project/module9-dsai/kartezio_workspace/heart/models/experiment"
    dataset = read_dataset(dataset_path, preview=True)
    train_x, train_y, train_v = dataset.train_xyv
    for i in range(len(train_x)):
        print(train_v[i].shape, train_y[i][0].shape)

    model = create_model(dataset.inputs)
    print(model)

    elite, _ = train_model(
        model,
        dataset,
        destination_directory,
        callback_frequency=10,
    )

    python_writer = GenomeToPython(model.parser)
    python_writer.to_python_class("HeartDetector", elite)

    p_train, _ = model.predict(dataset.train_x)
    for i, pi in enumerate(p_train):
        overlayed = draw_overlay(
            dataset.train_v[i],
            pi["mask"].astype(np.uint8),
            color=[128, 0, 0],
            alpha=0.6,
            thickness=2,
        ) 
        cv2.imwrite(f"train_{i}.png", overlayed)
        cv2.imwrite(f"train_{i}_mask.png", pi["mask"].astype(np.uint8))

    p_test, _ = model.predict(dataset.test_x)
    for i, pi in enumerate(p_test):
        overlayed = draw_overlay(
            dataset.test_v[i],
            pi["mask"].astype(np.uint8),
            color=[128, 0, 0],
            alpha=0.6,
            thickness=2,
        )
        cv2.imwrite(f"test_{i}.png", overlayed)


if __name__ == "__main__":
    main()
