# Intro
Tired of trying out all kinds of ML models when starting a new project. Try `superml`.

`superml` is a shortcut to ML. A wrapper of scikit-learn, etc.

# Getting Started

## Classification
The `SuperClassifier` module currently supports:

- "SVM"
- "LogisticRegression"
- "KNN"
- "RandomForest"
- "AdaBoost"
- "NaiveBayes"

It is super easy to start by copy-paste:

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

from superml import SuperClassifier
from superml import DEFAULT_CLASSIFIERS


X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
sclf = SuperClassifier(classifiers=DEFAULT_CLASSIFIERS)
sclf.fit(X_train, y_train)
sclf.evaluate(X=X_test, y=y_test, print_report=True)
```

Output right away:
```
SVM classification report: 
               precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       1.00      1.00      1.00        15
           2       1.00      1.00      1.00        16

    accuracy                           1.00        50
   macro avg       1.00      1.00      1.00        50
weighted avg       1.00      1.00      1.00        50

LogisticRegression classification report: 
               precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       1.00      1.00      1.00        15
           2       1.00      1.00      1.00        16

    accuracy                           1.00        50
   macro avg       1.00      1.00      1.00        50
weighted avg       1.00      1.00      1.00        50

KNN classification report: 
               precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       0.94      1.00      0.97        15
           2       1.00      0.94      0.97        16

    accuracy                           0.98        50
   macro avg       0.98      0.98      0.98        50
weighted avg       0.98      0.98      0.98        50

RandomForest classification report: 
               precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       0.94      1.00      0.97        15
           2       1.00      0.94      0.97        16

    accuracy                           0.98        50
   macro avg       0.98      0.98      0.98        50
weighted avg       0.98      0.98      0.98        50

AdaBoost classification report: 
               precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       0.79      1.00      0.88        15
           2       1.00      0.75      0.86        16

    accuracy                           0.92        50
   macro avg       0.93      0.92      0.91        50
weighted avg       0.94      0.92      0.92        50

NaiveBayes classification report: 
               precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       0.93      0.93      0.93        15
           2       0.94      0.94      0.94        16

    accuracy                           0.96        50
   macro avg       0.96      0.96      0.96        50
weighted avg       0.96      0.96      0.96        50
```

