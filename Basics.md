[Home](index.md)
# Basics

[Model Performance Metrics](#model-performance-metrics) | 
[Confusion Matrix Based Metrics](#confusion-matrix-based-metrics)


## Model Performance Metrics

### Confusion Matrix Based Metrics (Decision Support)

**Confusion Matrix**

|            | Predicted  | Positive    | Negative
|------------|------------|------------ | -------------
|            | Positive   | TP          | FN
| Actual     | Negative   | FP          | TN

#### Accuracy
**accuracy** = (TP + TN) / (TP + TN + FP + FN)

In English: What proportion of all cases were predicted correctly.

AKA: ACC

#### Precision
**precision** = TP / (TP + FP)

In English: Of those cases predicted positive, what proportion were actually positive.
AKA: positive predictive value

#### Recall
**recall** = TP / (TP + FN)

In English: Of those truly positive, what proportion were predicted positive.

AKA: true positive rate, sensitivity, hit rate

#### True Negative Rate
**true negative rate** = TN / (TN + FN)

In English: Of those cases that are actually negative, what proportion of them are predicted negative.

AKA: specificity, selectivity, TNR

#### False Positive Rate
**false positive rate** = FP / (FP + TN) = 1 - TNR

In English: Of all cases that are actually negative, what proportion were wrongly predicted positive.

AKA: fall-out, FPR

#### F1 Score
**F1 score** = 2 * (precision * recall) / (precision + recall)

In English: Balances getting all of your predictions right with getting all of the actual positive cases correctly classified.

AKA: F-measure, F1

#### Matthews Correlation Coefficient
**MCC** =
          ((TP * TN) - (FP * FN)) / sqrt((TP + FP)(TP + FN)(TN + FP)(TN + FN))

Range: -1 to 1

In English: A correlation coefficient between the actual cases and their predictions.

### Recommender System Metrics
**Mean Average Precision (mAP)** 

Fantastic explanation [here](http://sdsawtelle.github.io/blog/output/mean-average-precision-MAP-for-recommender-systems.html)

In English: each user gets an average precision of the top n recommendations, then you take the mean of those to get mAP

The precision calculatations are cumulative. So if 0 out of top 1, 1 out of top 3, 2 out of the top 3 are correct, and 2 out of 4, and then 3 out of 5. Then you take 

AKA: MAP, mAP

## Ranking Based Methods

**normalized Discounted Cumulative Gains (nDCG)**
Cumulative Gains - captures idea that more relvant results should be given higher scores. Sum relevancy of each item to get cumulative gain.
<p align="center">
  <img height="65" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/daea2db926c7324e8ed243e6c249a7b75ca2a839">
</p>
Dicounted Cumulative Gains - adds idea that where the result is, its rank, matters too. So relevant items that appear lower in the list get discounted.
<p align="center">
  <img height="65" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3efe45491d555db398ed663107460f81d6ecaf1e">
</p>
This formulation is used more in practice:
<p align="center">
  <img height="65" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d7ce96a2916c5eb451c4da5a1bce54fc9a2f7894">
</p>

Normalized Discounted Cumulative Gains - account for different recommender systems having results with differing potential recommendation counts. The "Ideal" Discounted Cumulative Gain, which is calculated assuming a perfect ranking. RELp is the orderd list of relevant documents.
<p align="center">
  <img height="65" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/b3510c9c5cf42ee8820d65335675cada51b40736">
</p>

**Mean Reciprocal Rank (MRR)**
Recommender ranks each item, then each relevant item is given the value of its reciprocal rank or 1/rank. So the first item (if relevant) is 1/1, the third 1/2 and so forth, but only when they are relevant. Then sum the values for MRR.
<p align="center">
  <img height="65" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d16e3616105fd3cbad78fa61e2f60c6abb458e26">
</p>

**Spearman Rank Correlation**
Correlation between actual ranks and predicted ranks.
<p align="center">
  <img height="65" src="https://wikimedia.org/api/rest_v1/media/math/render/svg/93e96a1c1568d0bb08de95c9976f040409e915a1">
</p>
where di is the difference between the two ranks of each observation and n is the numer of observations.
### Other Classification Metrics

#### ROC Curve and AUC
**ROC Curve and AUC**
Receiver Operating Characteristic curve and associated Area Under the Curve.

In English: ROC is the curve that shows the tradeoff between the benefit of proper classification (TPR) and the costs of misclassification (FPR) across a range of class assignment thresholds.
AUC is the area underneath this curve.
AUC is equal to the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one.

AKA: concordance statistic, c-statistic, A' (A-prime)

### Computer Vision Metrics
**Intersection over Union (IoU)**
Evaluation metric in object detection for evaluating bounding box prediction. 

In English: IoU is the ratio of the area of overlap between actual and predicted bounding box (numerator) and their union (denominator). Bounding boxes are the (x,y) coordinates of the object in the image. IoU > 0.5 is considered "acceptable" and is the typical threshold for a positive label of an instance in an image.

### Other Metrics

**Coverage**
Percent of total item base that the recommender recommends. Assures nothing is left out.

**Popularity**


**Novelty**


**Diversity**


**Temporal Evaluation**
Weight ratings base on how old the rating is.

## Statistics

### P-value
**p-value**: the probability that, when the null hypothesis is true, the statistical summary (such as the sample mean difference between two groups) would be equal to, or more extreme than, the actual observed results.

In English: the probability that the alternative hypothesis is accepted is due to random chance.

### Type I Error
**Type I Error**: Rejecting the null hypothesis when in actuality it should be accepted.

In English: Getting a false positive result.


### Type II Error
**Type II Error**: Accepting the null hypothesis when in actuality it should be rejected.

In English: Getting a false negative result.

### Power
**power (of a test)**: the probability of avoiding type II error. Stated otherwise, the probability of rejecting H0 given that H1 is true.

In English: The probability of avoiding a False Negative result. Or alternatively, the probability of rejecting the null hypothesis when it should be rejected (because H1 is actually true).
