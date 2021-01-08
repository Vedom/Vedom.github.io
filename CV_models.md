[Home](index.md) | 
[Computer Vision](Computer_Vision.md)

# Classification Models

## ResNet

## Inception

## AlexNet
- [Paper](https://arxiv.org/abs/1404.5997)

## VGG
- [Paper](https://arxiv.org/abs/1409.1556)

## SqueezeNet

## DenseNet

## GoogLeNet

## ShuffleNet

## MobileNet 

## ResNeXt

## Wide ResNet

## MNASNet

# Detection Models
## FasterRCNN
- Built off of COCO dataset.


# Segmentation Models

## FCNResnet 
- built on ResNet, CoCo dataset

# 2d Pose Estimation 
## Modeling
Most tend to be Multistage RNNs to provide memory between video frames. 

**2d Estimation approaches**
* Bottom-up - identifies joints first, then combines into a pose
* Top-down - identfies groups of subjects, then ids single person detector. Performance tends to degrade as number of subjects increases
* Output - keypoints, ie, points on human body 
    * mapping depends on body part focus
    * example keypoints: nose, left_eye, right_eye, left_ear, right_ear, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle
* Sport Movement Analysis + Humanoid ML Models
    * Body is split into areas of interest
        * biomechanics: frontal, sagittal, transverse planes ![Image of frontal, sagittal, transverse planes](https://upload.wikimedia.org/wikipedia/commons/2/24/Human_anatomy_planes%2C_labeled.svg)
        * skiing: "jacket", "pants"

**Evaluation Metrics**
* Percentage of Correct Parts - PCP
    - A limb is considered detected and a correct part if the distance between the two predicted joint locations and the true limb joint locations is at most half of the limb length (PCP at 0.5 )
    - Measures detection rate of limbs
    - Cons - penalizes shorter limbs
    - __Calculation__
    - For a specific part, PCP = (No. of correct parts for entire dataset) / (No. of total parts for entire dataset)
    - Take a dataset with 10 images and 1 pose per image. Each pose has 8 parts - ( upper arm, lower arm, upper leg, lower leg ) x2
    - No of upper arms = 10 * 2 = 20
    - No of lower arms = 20
    - No of lower legs = No of upper legs = 20
    - If upper arm is detected correct for 17  out of the 20 upper arms i.e 17 ( 10 right arms and 7 left) → PCP = 17/20 = 85% 
    - Higher the better 

* Percentage of Correct Key-points - PCK
    - Detected joint is considered correct if the distance between the predicted and the true joint is within a certain threshold (threshold varies)
    - PCKh@0.5 is when the threshold = 50% of the head bone link
    - PCK@0.2 == Distance between predicted and true joint < 0.2 * torso diameter 
    - Sometimes 150 mm is taken as the threshold
    - Head, shoulder, Elbow, Wrist, Hip, Knee, Ankle → Keypoints 
    - PCK is used for 2D and 3D (PCK3D)
    - Higher the better

* Percentage of Detected Joints - PDJ
    - Detected joint is considered correct if the distance between the predicted and the true joint is within a certain fraction of the torso diameter
    - Alleviates the shorter limb problem since shorter limbs have smaller torsos
    - PDJ at 0.2 → Distance between predicted and true join < 0.2 * torso diameter
    - Typically used for 2D Pose Estimation
    - Higher the better

* Mean Per Joint Position Error - MPJPE
    - Per joint position error = Euclidean distance between ground truth and prediction for a joint
    - Mean per joint position error = Mean of per joint position error for all k joints (Typically, k = 16)
    - Calculated after aligning the root joints (typically the pelvis) of the estimated and groundtruth 3D pose. 
    - __PA MPJPE__
    - Procrustes analysis MPJPE. 
    - MPJPE calculated after the estimated 3D pose is aligned to the groundtruth by the [Procrustes method](https://www.coursera.org/lecture/robotics-perception/pose-from-3d-point-correspondences-the-procrustes-problem-X22IH)
    - Procrustes method is simply a similarity transformation
    - Lower the better
    - Used for 3D Pose Estimation

* AUC


## Architectures
Nice easy blog read through of seven models [here](https://nanonets.com/blog/human-pose-estimation-2d-guide/?utm_source=github&utm_medium=social&utm_campaign=pose&utm_content=cbsudux).

1. DeepPose

2. Efficient Object Localization Using Convolutional Networks

3. Convolutional Pose Machines

4. Human Pose Estimation with Iterative Error Feedback

5. Stacked Hourglass Networks for Human Pose Estimation - iterative top-down + bottom-up + supervision to capture spatial relationships of body parts

6. Simple Baselines for Human Pose Estimation and Tracking

7. Deep High-Resolution Representation Learning for Human Pose Estimation

- Mask R-CNN - two stages: 1) generates proposed areas, 2) creates masks or bounding boxes in those areas
- Cascade Pyramid Networks - helps address body keypoint occlusion
- Part Affinity Field Method - used in OpenPose, bottom-up approach, real-time performance

## Datasets
- [COCO](https://cocodataset.org/#home) (Common Objects in COntext): 330k images and 250k persons with keypoints
- [MPII](http://human-pose.mpi-inf.mpg.de/) (Max Planck Institut Informatik) Human Pose Dataset: 25k images, 40k persons, 410 activities, 16 keypoints
- [LSP](https://sam.johnson.io/research/lsp.html) (Leeds Sports Pose Dataset): 2k pose-annotated images, 14 keypoints
- [FLIC](https://bensapp.github.io/flic-dataset.html) (Frames Labeled in Cinema): 5k images from movies, also has superset with ~21k images

# 3D Pose Estimation
**3d Estimation approaches**

## Datasets
- [Human3.6m](http://vision.imar.ro/human3.6m/description.php): 3.6 m 3D human poses and images, 50Hz video, accurate 3D join positions and angles, 24 keypoints, background subtraction, person bounding boxes