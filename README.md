# AI-3Dpath provides all source code needed for training and implementing AI-assisted 3D pathology using OTLS datasets.

To use these resources, the user should clone or download this repo and begin working with the provided jupyter notebooks from the main AI-3Dpath directory.

For example, on Windows:

git clone https://github.com/lindseyerionbarner/AI-3Dpath.git

cd AI-3Dpath

jupyter notebook


To install the necessary packages, the instructions provided in resource (1) listed at the bottom may be followed. Note that openslide must be installed (openslide.org).

In general, the code used in this repo relies on the directory formatting provided and should not be changed (for example the "images" directory and its containing subfolders should not be renamed or moved relative to the main AI-3Dpath working directory). 


Notebook (1) will split the provided images into 512 x 512 patches and save them to a directory called "patches". These patches are ready to be loaded by the trained algorithm ("trained_model_fold_0.pt") for predictions.

Notebook (2) will run the trained models (saved as .pt files in the main directory) on these image patches and estimate patch-based performance.


## Thank you to HTW Berlin - University of Applied Sciences for development and distribution of deep.TEACHING notebooks. Much of this code is adapted from the following resources:

(1) https://gitlab.com/deep.TEACHING/educational-materials/-/blob/master/notebooks/medical-image-classification/data-handling-usage-guide.ipynb

(2) https://gitlab.com/deep.TEACHING/educational-materials/-/blob/master/notebooks/medical-image-classification/exercise-prediction-and-heatmap-generation.ipynb

(3) https://github.com/3dimaging/DeepLearningCamelyon
