import os
from dotenv import load_dotenv

load_dotenv('app/.env')

# kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS') or "localhost"
KAFKA_TEST_TOPIC = os.getenv('KAFKA_SEGMENT_TOPIC') or "INVALID_TOPIC"
KAFKA_MY_GROUP_GROUP_ID = os.getenv('MY_GROUP_GROUP_ID')
