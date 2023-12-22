```python
# Import necessary libraries
import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# AI Model
class AIModel:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        df = pd.read_csv(self.filename)
        return df

    def prepare_data(self, df):
        # This is a placeholder for the actual data preparation process
        # In a real-world scenario, this method would include feature engineering and selection
        X = df.drop(['data', 'timestamp'], axis=1)
        y = df['data']
        return X, y

    def train_model(self, X, y):
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize model
        model = RandomForestRegressor(n_estimators=100, random_state=42)

        # Train model
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Calculate RMSE
        rmse = mean_squared_error(y_test, y_pred, squared=False)

        print(f"Model trained with RMSE: {rmse}")

        return model

    def save_model(self, model, filename):
        joblib.dump(model, filename)

# Initialize AI model
ai_model = AIModel('processed_data.csv')

# Load data
data = ai_model.load_data()

# Prepare data
X, y = ai_model.prepare_data(data)

# Train model
model = ai_model.train_model(X, y)

# Save model
ai_model.save_model(model, 'ai_model.joblib')

print("AI model training completed.")
```
