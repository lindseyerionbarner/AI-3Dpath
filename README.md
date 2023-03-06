# AI-3Dpath provides all source code needed for training and implementing AI-assisted 3D pathology using OTLS datasets.

## Several small example images are provided in the "images//" directory. These are full-resolution OTLS en face images saved in an RGB format for the deep learning algorithm. The nuclear channel is stored in R and the cytoplasmic channel is stored in G.

Notebook (1) will split these images into 512 x 512 patches and save them to a directory called "patches". These patches are ready to be loaded by the trained algorithm ("trained_model_fold_0.pt") for predictions.




Thank you to HTW Berlin - University of Applied Sciences for development and distribution of deep.TEACHING notebooks. Much of this code is adapted from the following resources:

https://gitlab.com/deep.TEACHING/educational-materials/-/blob/master/notebooks/medical-image-classification/data-handling-usage-guide.ipynb

https://gitlab.com/deep.TEACHING/educational-materials/-/blob/master/notebooks/medical-image-classification/exercise-prediction-and-heatmap-generation.ipynb


https://github.com/3dimaging/DeepLearningCamelyon
