# To collect and expose custom metrics from your application, you can use the prometheus_client library in Python.

from prometheus_client import start_http_server, Gauge
import random
import time

# Create a metric to track the number of requests
REQUESTS = Gauge('app_requests_total', 'Total number of requests processed by the application')

def process_request():
    """Simulate processing a request."""
    REQUESTS.inc()  # Increment the request count

if __name__ == '__main__':
    # Start up the server to expose metrics
    start_http_server(8000)  # Metrics will be available at http://localhost:8000/metrics
    
    # Simulate processing requests
    while True:
        process_request()
        time.sleep(random.uniform(0.5, 1.5))  # Simulate random request intervals
