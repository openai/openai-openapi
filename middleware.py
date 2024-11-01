import time

class Middleware:
    def __init__(self):
        self.requests = []
        self.responses = []

    def collect_request(self, endpoint, method, data):
        request_info = {
            'timestamp': time.time(),
            'endpoint': endpoint,
            'method': method,
            'data': data
        }
        self.requests.append(request_info)

    def collect_response(self, endpoint, method, response):
        response_info = {
            'timestamp': time.time(),
            'endpoint': endpoint,
            'method': method,
            'response': response
        }
        self.responses.append(response_info)

    def collect_metrics(self):
        metrics = {
            'total_requests': len(self.requests),
            'total_responses': len(self.responses),
            'average_response_time': self.calculate_average_response_time()
        }
        return metrics

    def calculate_average_response_time(self):
        if not self.requests or not self.responses:
            return 0
        total_time = 0
        for request, response in zip(self.requests, self.responses):
            total_time += response['timestamp'] - request['timestamp']
        return total_time / len(self.requests)
