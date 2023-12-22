```python
# Import necessary libraries
from flask import Flask, request, jsonify
import json

# Citizen Engagement Portal
class CitizenEngagementPortal:
    def __init__(self):
        self.app = Flask(__name__)
        self.issues = []

    def report_issue(self):
        data = request.get_json()
        self.issues.append(data)
        return jsonify({"message": "Issue reported successfully."}), 200

    def get_issues(self):
        return jsonify({"issues": self.issues}), 200

    def run_portal(self):
        self.app.add_url_rule('/report_issue', 'report_issue', self.report_issue, methods=['POST'])
        self.app.add_url_rule('/get_issues', 'get_issues', self.get_issues, methods=['GET'])
        self.app.run(debug=True)

# Initialize Citizen Engagement Portal
portal = CitizenEngagementPortal()

# Run portal
portal.run_portal()
```
