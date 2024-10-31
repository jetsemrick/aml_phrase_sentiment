import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression

class LogisticRegression:
  def __init__(self, **kwargs):
    """Initialize the Logistic Regression model with optional scikit-learn parameters."""
    self.model = SklearnLogisticRegression(**kwargs)

  def fit(self, X, y):
    """Fit the logistic regression model to the data."""
    self.model.fit(X, y)

  def predict(self, X):
    """Predict class labels for each data point and return as a pandas DataFrame."""
    labels = self.model.predict(X)
    labels_df = pd.DataFrame(labels, columns=["Predicted Label"])
    return labels_df

  def predict_proba(self, X):
    """Return probabilities for each class for each data point as a pandas DataFrame."""
    probabilities = self.model.predict_proba(X)
    class_names = [f"Class {i}" for i in range(probabilities.shape[1])]
    probabilities_df = pd.DataFrame(probabilities, columns=class_names)
    return probabilities_df

  def score(self, X, y):
    """Calculate the accuracy of the model on the given data."""
    return self.model.score(X, y)