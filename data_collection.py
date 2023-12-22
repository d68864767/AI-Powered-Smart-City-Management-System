```python
# Import necessary libraries
import os
import json
from datetime import datetime
from random import randint
import requests

# IoT devices for data collection
class IoTDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type

    def collect_data(self):
        # This is a placeholder for the actual data collection process
        # In a real-world scenario, this method would interface with the device's sensors to collect data
        data = {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "timestamp": datetime.now().isoformat(),
            "data": randint(1, 100)  # Random data for demonstration purposes
        }
        return data

# Data Collection
class DataCollection:
    def __init__(self, devices):
        self.devices = devices

    def collect_data_from_devices(self):
        collected_data = []
        for device in self.devices:
            data = device.collect_data()
            collected_data.append(data)
        return collected_data

    def save_data(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)

    def send_data_to_cloud(self, data, cloud_endpoint):
        # This is a placeholder for the actual data sending process
        # In a real-world scenario, this method would send the collected data to a cloud storage system
        response = requests.post(cloud_endpoint, data=json.dumps(data))
        return response.status_code

# Initialize IoT devices
devices = [IoTDevice(f"device_{i}", "sensor") for i in range(10)]

# Initialize data collection
data_collection = DataCollection(devices)

# Collect data from devices
collected_data = data_collection.collect_data_from_devices()

# Save data locally
data_collection.save_data(collected_data, 'collected_data.json')

# Send data to cloud
cloud_endpoint = "http://cloud_storage_system.com/api/v1/data"  # Placeholder cloud endpoint
response_status = data_collection.send_data_to_cloud(collected_data, cloud_endpoint)

print(f"Data sent to cloud with status code: {response_status}")
```
