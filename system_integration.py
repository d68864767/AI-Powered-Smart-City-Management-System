```python
# Import necessary libraries
import os
import json
from data_collection import DataCollection, IoTDevice
from data_processing import DataProcessing
from ai_model import AIModel
from energy_management import EnergyManagement
from citizen_engagement_portal import CitizenEngagementPortal

# System Integration
class SystemIntegration:
    def __init__(self):
        # Initialize IoT devices
        self.devices = [IoTDevice(f"device_{i}", "sensor") for i in range(10)]

        # Initialize data collection
        self.data_collection = DataCollection(self.devices)

        # Initialize data processing
        self.data_processing = DataProcessing('collected_data.json')

        # Initialize AI model
        self.ai_model = AIModel('processed_data.csv')

        # Initialize energy management
        self.energy_management = EnergyManagement('ai_model.pkl', 'processed_data.csv')

        # Initialize citizen engagement portal
        self.citizen_engagement_portal = CitizenEngagementPortal()

    def run(self):
        # Collect data from devices
        collected_data = self.data_collection.collect_data_from_devices()

        # Save collected data
        self.data_collection.save_data(collected_data, 'collected_data.json')

        # Load data
        data = self.data_processing.load_data()

        # Preprocess data
        processed_data = self.data_processing.preprocess_data(data)

        # Save processed data
        self.data_processing.save_processed_data(processed_data, 'processed_data.csv')

        # Load data for AI model
        df = self.ai_model.load_data()

        # Prepare data for AI model
        X, y = self.ai_model.prepare_data(df)

        # Train AI model
        self.ai_model.train_model(X, y)

        # Save AI model
        self.ai_model.save_model('ai_model.pkl')

        # Load AI model for energy management
        model = self.energy_management.load_model()

        # Load data for energy management
        df = self.energy_management.load_data()

        # Predict energy consumption
        predictions = self.energy_management.predict_energy_consumption(model, df)

        # Save predictions
        self.energy_management.save_predictions(predictions, 'predictions.csv')

        # Run citizen engagement portal
        self.citizen_engagement_portal.run()

# Initialize system integration
system_integration = SystemIntegration()

# Run system integration
system_integration.run()
```
