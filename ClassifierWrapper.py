"""
A wrapper class for a Classifier.
"""
from sklearn.metrics import *


class ClassifierWrapper:
    def __init__(self, classifier, x_train, x_test, y_train, y_test):
        """
        Initializes the Classifier and trains it
        :param classifier: A classifier object from the sklearn library
        :param x_train: Training data for the X input feature vector
        :param x_test:  The input feature vector to test classifier on
        :param y_train: The output vector Y to train classifier
        :param y_test: The correct values of the test data
        """
        self.tx = x_train  # tx is the train data for X
        self.px = x_test  # px is the test input data for X
        self.ty = y_train  # ty is the train input data for Y
        self.py = y_test  # py is the test input data for Y
        self.classifier = classifier

        self.classifier.fit(self.tx, self.ty)
        self.predictions = self.classifier.predict(self.px)

    def values(self) -> tuple:
        """
        Computes successes, fails, precision, recall, accuracy, F1 score,
        false positives and negatives, and a classification report string.
        :rtype: tuple
        :return: Tuple with the computed values in the above order
        """
        success = 0
        fail = 0
        fp = 0  # false positives
        fn = 0  # false negatives

        f1 = f1_score(self.py, self.predictions, average='weighted')
        for i in range(0, len(self.px)):
            if self.py[i] == self.predictions[i]:
                success += 1
            elif self.py[i] == 1 and self.predictions[i] == 0:
                fn += 1
                fail += 1
            elif self.py[i] == 0 and self.predictions[i] == 1:
                fp += 1
                fail += 1
        accuracy = accuracy_score(self.py, self.predictions)
        precision = precision_score(self.py, self.predictions)
        recall = recall_score(self.py, self.predictions)
        report = classification_report(self.py, self.predictions)

        return success, fail, precision, recall, accuracy, f1, fp, fn, report
