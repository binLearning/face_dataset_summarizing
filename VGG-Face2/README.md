## VGG-Face2

[VGGFace2 Dataset](http://www.robots.ox.ac.uk/~vgg/data/vgg_face2/)

### Overview
We introduce a new large-scale face dataset named VGGFace2. The dataset contains 3.31 million images of 9131 subjects (identities), 
with an average of 362.6 images for each subject. Images are downloaded from Google Image Search and have large variations in pose, 
age, illumination, ethnicity and profession (e.g. actors, athletes, politicians). <br>

The dataset was collected with three goals in mind: <br>
(i) to have both a large number of identities and also a large number of images for each identity; <br>
(ii) to cover a large range of pose, age and ethnicity; and <br>
(iii) to minimize the label noise through automated and manual filtering, <br>

The whole dataset is split to a training set (including 8631 identites) and a test set (including 500 identites). 
The identities in the training set are disjoint with the ones in benchmark datasets IJB-A and IJB-B. <br>

### Dataset Statistics
* Total number of images : 3.31 Million.
* Number of identities : 9131 (train: 8631, test: 500)
* Number of male identities : 5452
* Number of images per identity : 87/362.6/843 (min/avg/max)
* Number of pose templates : list of pose template for 368 subjects (2 front templates, 
2 three-quarter templates and 2 profile templates, each template containing 5 images)
* Number of age templates : list of age template for 100 subjects (2 young templates and 2 mature templates,
each template containing 5 images)

### Related Paper
[VGGFace2: A dataset for recognising faces across pose and age](https://arxiv.org/abs/1710.08092)
