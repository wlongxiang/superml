from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from superml import SuperClassifier


def run():
    myclfs = {
        "SVM": SVC(),
        "LogisticRegression": LogisticRegression(max_iter=100),
        "KNN": KNeighborsClassifier(),
        "RandomForest": RandomForestClassifier(max_depth=2, n_estimators=100),
        "AdaBoost": AdaBoostClassifier(),
        "NaiveBayes": GaussianNB()
    }

    X, y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    sclf = SuperClassifier(classifiers=myclfs)
    sclf.fit(X_train, y_train)
    sclf.evaluate(X=X_test, y=y_test, print_report=True)


if __name__ == '__main__':
    run()
