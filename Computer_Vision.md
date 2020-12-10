# Computer Vision

## Computer Vision Tasks
* Classification - most models built off of [ImageNet](http://www.image-net.org/) using CNNs
* Detection - often Object Box-Bounding Localization, usually by R-CNN (Region-based CNN)
* Semantic Scene Labeling or Semantic Segmentation labels each pixel in the image and segments image
	* instance segmentation - ids objects despite occlusion (being blocked or obstructed), e.g., Mask R-CNN
* Object Tracking - object movement over time (i.e., sequences of images in temporal order)
* 2D Pose Estimation - estimating human body's (parts and joints) pose
* 3D Pose Estimation - reconstructs human pose and environment in 3D
* Action recognition - recognizing specific actions from simple to complex (e.g., walking, downward-dog). Often ground truth labels come from sensor data.

## Resources
### Data
* [ImageNet](http://www.image-net.org/) 15m+ hi-res images labeled to ~22k categories
* [Common Objects in Context (CoCo)](https://cocodataset.org/#home) 330k+ images with 200k labeled across 80 object categories, 91 stuff categories. Also has 250k people with keypoints and 5 captions per image.
* [PASCAL Visual Object Classes (PASCAL VOC)](http://host.robots.ox.ac.uk/pascal/VOC/index.html) 11,530 labeled images across 20 classes for a total of 27k ROI objects and 7k segmentations. Provides standardised image data sets for object class recognition. 
* [CIFAR-10 / CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html)
The CIFAR-10 and CIFAR-100 are labeled subsets of the 80 million tiny images dataset (no longer available). They were collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.
	* The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.
	* The CIFAR-100 dataset is just like the CIFAR-10, except it has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class. The 100 classes in the CIFAR-100 are grouped into 20 superclasses. Each image comes with a "fine" label (the class to which it belongs) and a "coarse" label (the superclass to which it belongs).
* [Sports-1M](https://cs.stanford.edu/people/karpathy/deepvideo/) Contains 1,133,158 video URLs which have been annotated automatically with 487 Sports labels using the YouTube Topics API (also available [here](https://github.com/gtoderici/sports-1m-dataset/))

### Pretrained Models & Architectures
* [ModelZoo](https://modelzoo.co/)

### Books
* [Computer Vision: A Modern Approach](http://luthuli.cs.uiuc.edu/~daf/CV2E-site/cv2eindex.html)
* [Computer Vision:  Models, Learning, and Inference](http://www.computervisionmodels.com/)
* [Multiple View Geometry in Computer Vision
Second Edition](https://www.robots.ox.ac.uk/~vgg/hzbook/)
* [Computer Vision: Algorithms and Applications, 2nd ed.](http://szeliski.org/Book/)
* [CVOnline](http://homepages.inf.ed.ac.uk/rbf/CVonline/books.htm#online) Tons of online books

### Blogs and Other Articles
* [Neurohive](https://neurohive.io/en/)
