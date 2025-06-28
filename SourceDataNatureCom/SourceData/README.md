# Source Data
Source data associated with Figures 2-6 in the manuscript is described below.    
### Directory Description
#### Raw Images
Raw images are provided as described below. 
#### Datasets
Training and test datasets are provided including both original and annotated images under ```/dataset``` folder. 
#### Kartezio source code
The source code of Kartezio is released and updated on [Github](https://github.com/KevinCortacero/Kartezio) repository.
#### Scripts & Notebooks
The source code of Kartezio article related scripts is released and updated on [Github](https://github.com/KevinCortacero/KartezioPaper) repository.
#### Models (Genotypes)
Genotypes (as json files) are provided for all different conditions under ```/models``` directory.
The number of runs per condition is indicated. 

### Figure 2a,b: Comparison between Kartezio and Cellpose using Cell Image Library  
#### Acquisition
The Cell Image Library dataset (available here https://www.cellpose.org/dataset) is composed of 100 images of in vitro cultured neurons stained for phalloidin and DAPI and imaged using an epifluorescence microscope. 
#### Datasets
The training dataset contains 89 images and the test dataset contains 11. Both are available online at https://www.cellpose.org/dataset
Kartezio was benchmarked on different training dataset sizes, ranging from 1 image to 89 images and associated text file is provided for each training dataset size that indicates the indices of the training images used. 
#### Genotypes
Genotypes are provided for 24 different conditions (35 runs per condition). 

### Figure 2c,d: Comparison between Kartezio and Cellpose using melanoma cohort (melanoma nucleus identification)
#### Acquisition 
Tissue slices were stained for melanoma marker Sox10 (orange), CTL marker CD8 (purple), lysosomal marker CD107a (black) and hematoxylin (blue).
IHC slides were digitized with a Panoramic 250 Flash II digital microscope for a scan resolution of 0.24 µm/pixel in the final whole slide image.   
WSIs corresponded to a 9-level pyramidal image from which we extracted Level 0 for this Figure.   
Authors: NVA/LL/NM/BV/FXF
#### Raw Images
Raw histology patches provided are from Level 0. 
#### Dataset
The training dataset contains 12 images and the test dataset 10 images. 
Images were preprocessed as indicated (RGB, HSV, HED) and Endpoint (MCW, LABELS) is also notified as directory name.
Original and annotated images are included for training and test datasets.  
#### Genotypes 
Genotypes are provided for 6 different conditions (10 runs per condition). 

### Figure 3 (Use Case 1: Melanoma Tumor Nodules)
Tissue slices were stained for melanoma marker Sox10 (orange), CTL marker CD8 (purple), lysosomal marker CD107a (black) and hematoxylin (blue).IHC slides were digitized with a Panoramic 250 Flash II digital microscope for a scan resolution of 0.24 µm/pixel in the final whole slide image.   
WSIs corresponded to a 9-level pyramidal image from which we extracted a low resolution thumbnail of dimension 461x1024 pixels (“training level”) using OpenSlide library. These training level images served as the input dataset for Kartezio and were subject to expert pathologist annotation to establish the ground truth. 
Authors: NVA/LL/NM/BV/FXF
#### Raw Images
Raw thumbnail images are provided from the "training level".  
#### Dataset
The training dataset contains 12 images and the test dataset 12 images. Images were preprocessed by transforming RGB channels into HSV color space. 
Original and annotated images are included for training and test datasets. 
#### Genotypes 
Genotypes are provided for 100 runs.

### Figure 4 (Use Case 2: CTL-released Particles)
#### Acquisition 
Total Internal Reflection Fluorescence Microscopy (TIRFM) images of particles released from human polyclonal CD8+ CTLs (derived from two donors) and stained with Alexa 647-conjugated wheat germ agglutinin (WGA; cyan; a fluorescent probe that stains sialic acid and N-acetyl-glucosamine moieties of glycoproteins), and DiO (magenta; a lipophilic dye that stains hydrophobic lipid membranes). 
Authors: OS, MD
#### Raw Images
Raw TIRF images are provided (DiO, WGA, and merge) 
#### Datasets
The training and test datasets each contain one image split into four. 
Each dataset was split into two datasets, one for WGA and one for DiO. 
Original and annotated images are included for training and test datasets. 
#### Genotypes
Genotypes are provided for 35 runs per channel (DiO, WGA).  

### Figure 5 (Use Case 3: Lytic Content)
#### Acquisition
Human polyclonal CD8+ T cells were stained with antibodies directed against CD45 (gray), perforin (magenta), granzyme B (yellow) and CD107a (cyan) and imaged in 3D by confocal microscopy. ) z-stacks of images in the CD45 channel were used as a 3D input to delimitate individual cells.
Authors: GC, FL, RK 
#### Raw Images
Raw images are provided as merged images in ```/experiment```.
#### Datasets
5 images were selected for the training dataset and 4 for the test dataset. Only the CD45 channel served as input for the model. 
Original and annotated images are included for training and test datasets. 
#### Genotypes
Genotypes are provided for 35 runs.  

### Figure 6 (Use Case 4: Immune Synapse Detection) 
#### Acquisition
CTLs were stained with DAPI (cyan, to detect CTL and target cell nuclei), with antibodies directed against a-tubulin (green, to visualize the cytoskeleton in both cells), and perforin (magenta, a lytic molecule expressed only by CTLs) and imaged by confocal microscopy.  
Author: SM
#### Raw Images
Raw images are provided as merged images in ```/experiment```. 
#### Datasets
Training dataset contains 8 images and test dataset contains 4. Both DAPI and tubulin served as inputs for the models. 
Original and annotated images are included for training and test datasets. 
#### Genotypes
Genotypes are provided for 35 runs.