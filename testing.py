```python
# Import necessary libraries
import os
import json
import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

# Testing
class Testing:
    def __init__(self, model_filename, test_data_filename):
        self.model_filename = model_filename
        self.test_data_filename = test_data_filename

    def load_model(self):
        # Load the trained AI model
        model = joblib.load(self.model_filename)
        return model

    def load_test_data(self):
        # Load the test data
        df = pd.read_csv(self.test_data_filename)
        X_test = df.drop(['data', 'timestamp'], axis=1)
        y_test = df['data']
        return X_test, y_test

    def evaluate_model(self, model, X_test, y_test):
        # Use the model to make predictions on the test data
        y_pred = model.predict(X_test)

        # Calculate the mean squared error of the predictions
        mse = mean_squared_error(y_test, y_pred)
        return mse

# Initialize testing
testing = Testing('ai_model.joblib', 'test_data.csv')

# Load model
model = testing.load_model()

# Load test data
X_test, y_test = testing.load_test_data()

# Evaluate model
mse = testing.evaluate_model(model, X_test, y_test)

print(f"Mean Squared Error: {mse}")
```
