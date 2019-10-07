# Basics

[Model Performance Metrics](#model-performance-metrics)
[Confusion Matrix Based Metrics](#confusion-matrix-based-metrics)


## Model Performance Metrics

### Confusion Matrix Based Metrics

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
          (TP * TN) - (FP * FN) / sqrt((TP + FP)(TP + FN)(TN + FP)(TN + FN))

Range: -1 to 1

In English: A correlation coefficient between the actual cases and their predictions.

### Other Metrics

#### ROC Curve and AUC
**ROC Curve and AUC**
Receiver Operating Characteristic curve and associated Area Under the Curve.

In English: ROC is the curve that shows the tradeoff between the benefit of proper classification (TPR) and the costs of misclassification (FPR) across a range of class assignment thresholds.
AUC is the area underneath this curve.
AUC is equal to the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one.

AKA: concordance statistic, c-statistic, A' (A-prime)


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
