## MS-Celeb-1M

[MS-Celeb-1M: A Dataset and Benchmark for Large-Scale Face Recognition](https://arxiv.org/abs/1607.08221)<br>
[MS-Celeb-1M: Challenge of Recognizing One Million Celebrities in the Real World](https://www.microsoft.com/en-us/research/project/ms-celeb-1m-challenge-recognizing-one-million-celebrities-real-world/)

### Details
MS-Celeb-1M is a large training dataset which covers about **100K** celebrities.<br>
The dataset has 6 types:
#### 1. Full ImageThumbnails data
**Purpose**: Whole images are down sampled to up to 300*300 thumbnails, which are meant to provide the complete contextual information of the faces.

Some statistics:
* #of Entities: 99,952
* #of Lines: 10,490,534
* Image Resolution: up to 300*300
* Average Image#/Entity: 105
* Total file size (uncompressed): 214GB

#### 2. Cropped face images
**Purpose**: Faces are cropped with enough background region, and meant to let participants run their own face detector and alignment for more flexibility.

Some statistics:
* #of Entities: 99,892
* #of Lines: 8,456,240
* Image Resolution: up to 300*300
* Average Image#/Entity: 85
* Total file size (uncompressed): 152GB

#### 3. Aligned face images
**Purpose**: Faces are aligned by MSR’s algorithm, and meant to let participants directly train models  if they don’t have face detector and alignment modules at hand. We will use the same alignment approach on DevSet and MeasurementSet.

Some statistics:
* #of Entities: 99,892
* #of Lines: 8,456,240
* Image Resolution: up to 300*300
* Average Image#/Entity: 85
* Total file size (uncompressed): 89 GB

#### 4. Sample data: same format to the full data, smaller file size, for your preview
Sample ImageThumbnails Data: 14 entities, 44MB<br>
Sample FaceCropped Data: 14 entities, 41MB<br>
Sample FaceAligned Data: 14 entities, 32MB<br>

#### 5. Complete 1M entity list can be downloaded here
**Purpose**: MIDs and names of the 1M celebrities are released for algorithm training and data collection

Some statistics:
* #of line: 3,481,187
* #of unique MIDs: 1,000,000
* Total file size: 110MB

#### 6. Development data set can be downloaded here. 
**Purpose**: This data has 6 files. Each file contains 500 face images and labels, which can be used to develop/verify your recognition algorithms. They may also be used during the dry-run stage. DevSet1 is used to test the robustness of an algorithm on illumination, pose, resolution, etc. DevSet2 is used to test the coverage of an algorithm among the 1M entities. Both of these two sets include cropped and aligned face images.

Some Statistics:
* #of line: 500 lines in each file
* #of unique MIDs: 500
* Total file size: tsv files: 44 MB, zip files: 32MB

### Related Paper
[MS-Celeb-1M: A Dataset and Benchmark for Large-Scale Face Recognition](https://arxiv.org/abs/1607.08221)<br>
[MS-Celeb-1M: Challenge of Recognizing One Million Celebrities in the Real World](https://www.researchgate.net/publication/295074418_MS-Celeb-1M_Challenge_of_Recognizing_One_Million_Celebrities_in_the_Real_World)
