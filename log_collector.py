# To push logs to Elasticsearch, you can use the elasticsearch Python client.
from elasticsearch import Elasticsearch
import logging
import time

# Elasticsearch client setup
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
index_name = 'application-logs'

# Configure Python logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('log_collector')

def log_message(message):
    """Log a message and send it to Elasticsearch."""
    logger.info(message)
    es.index(index=index_name, body={'message': message, 'timestamp': time.time()})

if __name__ == '__main__':
    while True:
        log_message('This is a sample log message.')
        time.sleep(5)  # Log every 5 seconds
