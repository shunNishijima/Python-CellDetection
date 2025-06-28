import numpy as np
import pandas as pd
from kartezio.dataset import read_dataset
from kartezio.inference import ModelPool
from kartezio.fitness import FitnessIOU

DATASET_FOLDER = "dataset"
MODELS_FOLDER = "models"
EXPERIMENT_FOLDERS = ["5_images", "10_images", "15_images", "20_images", "25_images", "45_images"]
SHOW_INDIVIDUAL = True

def main():
    dataset = read_dataset(DATASET_FOLDER, counting=True, preview=True)
    results = pd.DataFrame({"submission": [], "model": [], "fitness": [], "mean_iou": [], "mean_dsc": []})
    for exp_folder in EXPERIMENT_FOLDERS:
        print()
        print(f"EXPERIMENT {exp_folder}")
        pool = ModelPool(f"{MODELS_FOLDER}/{exp_folder}/", FitnessIOU(), regex="*/elite.json")
        fitness_scores = []
        iou_scores = []
        dsc_scores = []
        for i, model in enumerate(pool.models):
            predictions, fitness, time = model.eval(dataset, "test")
            iou_score = mean_metric(dataset.test_y, predictions, iou)
            dsc_score = mean_metric(dataset.test_y, predictions, dsc)
            if SHOW_INDIVIDUAL:
                print(f"  model {i+1}:")
                print(f"    fitness:  {fitness}")
                print(f"    mean iou: {iou_score}")
                print(f"    mean dsc: {dsc_score}")
            fitness_scores.append(fitness)
            iou_scores.append(iou_score)
            dsc_scores.append(dsc_score)
            results = results._append({"submission": exp_folder, "model": i+1, "fitness": fitness, "mean_iou": iou_score, "mean_dsc": dsc_score}, ignore_index=True)
        print(f"  submission mean:")
        print(f"    fitness:  {np.mean(fitness_scores)}")
        print(f"    mean iou: {np.mean(iou_scores)}")
        print(f"    mean dsc: {np.mean(dsc_scores)}")
    results.to_csv("results.csv")


def mean_metric(true_y, pred_y, func):
    _true_y = [true_yi[0] for true_yi in true_y]
    _pred_y = [pred_yi["mask"] for pred_yi in pred_y]
    scores = []
    for true_yi, pred_yi in zip(_true_y, _pred_y):
        scores.append(func(true_yi, pred_yi))
    return np.mean(scores)


def iou(true_yi, pred_yi):
    intersection = np.logical_and(true_yi, pred_yi)
    union = np.logical_or(true_yi, pred_yi)
    return np.sum(intersection) / np.sum(union)


def dsc(true_yi, pred_yi):
    intersection = np.logical_and(true_yi, pred_yi)
    union = np.logical_or(true_yi, pred_yi)
    n = np.sum(intersection)
    return 2 * n / (n + np.sum(union))


if __name__ == "__main__":
    main()
