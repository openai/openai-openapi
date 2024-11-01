import yaml
import requests

class APIExplorer:
    def __init__(self, openapi_file):
        with open(openapi_file, 'r') as file:
            self.openapi_spec = yaml.safe_load(file)
        self.base_url = self.openapi_spec['servers'][0]['url']

    def call_api(self, endpoint, method, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data)
        return response.json()

    def simulate_api(self, endpoint, method, data=None):
        # Simulate API response based on OpenAPI spec
        for path, methods in self.openapi_spec['paths'].items():
            if path == endpoint and method.lower() in methods:
                return methods[method.lower()]['responses']['200']['description']
        return "Simulation not available for this endpoint and method."
