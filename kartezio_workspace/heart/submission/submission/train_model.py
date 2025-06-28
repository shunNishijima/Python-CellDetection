from kartezio.apps.segmentation import create_segmentation_model
from kartezio.dataset import read_dataset
from kartezio.endpoint import EndpointThreshold
from kartezio.training import train_model

# folder paths
DATASET_FOLDER = "dataset"
MODELS_FOLDER = "models"

# case parameters
CASE_FOLDER = "45_images"
NUMBER_OF_MODELS = 3
# NOTE: to change the amount of images in a case, update the dataset.csv file

# hyper parameters
NUMBER_OF_GENERATIONS = 20000
NUMBER_OF_CHILDREN = 5
NUMBER_OF_NODES = 30
ENDPOINT = EndpointThreshold(128)

# model has one input channel because dataset has grayscale images
NUMBER_OF_INPUTS = 1

# prints and saves progress while training every X number of generation
CALLBACK_FREQUENCY = 100


def main():
    dataset = read_dataset(DATASET_FOLDER, counting=True, preview=True)
    output_dir = f"{MODELS_FOLDER}/{CASE_FOLDER}"
    for i in range(NUMBER_OF_MODELS):
        model = create_segmentation_model(
            NUMBER_OF_GENERATIONS,
            NUMBER_OF_CHILDREN,
            nodes=NUMBER_OF_NODES,
            inputs=NUMBER_OF_INPUTS,
            endpoint=ENDPOINT
        )
        train_model(model, dataset, output_dir, callback_frequency=CALLBACK_FREQUENCY)


if __name__ == "__main__":
    main()
