# About

This is the project doing analysis about Cartesian Genetic Programming, using [Kartezio](https://github.com/KevinCortacero/Kartezio).

# Installation

## Requirements

- Python 2.x
- Latest version of Kartezio package. (Can be install using `pip install kartezio`)

## How to install

- Just simply download this whole project and unzip. When running the project, remember to redirect to the correct working path.

## How to use

We have provided all the needed files to run. Depending on your dataset or purpose of your analysis, you can modify them. The [medical dataset](http://medicaldecathlon.com/) is already provided as well.

- In the project, the main running file is `training_kartezio.py`. Check the file, modify the variable `dataset_path` as the path should lead to the dataset folder. Also, the `destination_directory` will be changed to the directory (preferably empty one) that saves the models which are produced after the training step.
- Regarding the dataset folder, the inner folders are `images` and its corresponding `labels` to contain the images and labels used. The `.csv` file is to define the paths of image/label, showing which one is used for training and testing. The `META.json` file is to define the configuration of our current project (to configure the type of images and labels we used)
- In our project, the `models` folder already contained the models we trained with different number of dataset. You can check the `elite.json` file in each model to know more about the result.

# Note

- Besides the main file (i.e., `training_kartezio.py`), we also had other files to utilise other functions. Note that, these files are only for reference and you need to modify accordingly.
  - `convert_png.py`: to convert .nii files into readable image files.
  - `slice_dataset.ipynb`: to create slices of the dataset
  - `visualise_model.py`: to visualise the pipeline of Kartezio as a graph
  - `show_predictions.py`: to create an overlay of predictions; it is used to shows whether the model is learning well or not
- We also attached `results.csv`, which shows the result of our experiments.

# Acknowledgement

Technical Computer Science, University Of Twente

- Thijmen Welberg, s3016110
- Khanh Nguyen, s2950944
- Matthew Pieper, s2131455
- Shun Nishijima, s2977923
