from sklearn import datasets
from sklearn.model_selection import train_test_split

from superml import SuperClassifier
from superml import DEFAULT_CLASSIFIERS


def run():
    X, y = datasets.load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    sclf = SuperClassifier(classifiers=DEFAULT_CLASSIFIERS)
    sclf.fit(X_train, y_train)
    sclf.evaluate(X=X_test, y=y_test, print_report=True)


if __name__ == '__main__':
    run()
