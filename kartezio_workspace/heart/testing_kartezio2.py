import numpy as np
from kartezio.dataset import read_dataset
from kartezio.inference import ModelPool
from kartezio.fitness import FitnessIOU
from tensorboard.plugins.hparams.summary import experiment_pb

dataset_path = "dataset"
model_folder = "models"
experiments = ["5_images", "10_images", "15_images", "20_images", "25_images"]

dataset = read_dataset(dataset_path, counting=True, preview=True)
for exp_folder in experiments:
    pool = ModelPool(f"{model_folder}/{exp_folder}/", FitnessIOU(), regex="*/elite.json")
    print(f"EXPERIMENT {exp_folder}")
    for subset in ["train", "test"]:
        scores = []
        print(f"  individual scores for {subset} set:")
        for model in pool.models:
            prediction, fitness, time = model.eval(dataset, subset)
            print(f"    {fitness}")
            scores.append(fitness)
        print(f"  mean score on {subset} set: {np.mean(scores)}")
    print()
