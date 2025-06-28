from kartezio.apps.instance_segmentation import create_instance_segmentation_model
from kartezio.dataset import read_dataset
from kartezio.endpoint import EndpointWatershed
from kartezio.stacker import StackerMean
from kartezio.training import train_model
from kartezio.preprocessing import Format3D, SelectChannels

DATASET = "C:/Module9/Project/module9-dsai/kartezio_workspace/heart/dataset_tif"
OUTPUT = "C:/Module9/Project/module9-dsai/kartezio_workspace/heart/models"
CHANNELS = [0, 1, 2]
preprocessing = SelectChannels(channels=CHANNELS)


if __name__ == "__main__":
    generations = 100
    _lambda = 5
    frequency = 5
    model = create_instance_segmentation_model(
        generations,
        _lambda,
        inputs=2,
        outputs=2,
        series_mode=True,
        series_stacker=StackerMean(arity=2),
        endpoint=EndpointWatershed(),
    )

    dataset = read_dataset(DATASET)

    elite, _ = train_model(
        model,
        dataset,
        OUTPUT,
        preprocessing=preprocessing,
        callback_frequency=frequency,
    )
