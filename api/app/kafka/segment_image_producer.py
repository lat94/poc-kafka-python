import json
from .schema import Message
from ..environment import KAFKA_TEST_TOPIC, KAFKA_BOOTSTRAP_SERVERS
from loguru import logger
import json
from aiokafka import AIOKafkaProducer


async def produce(message: Message):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    logger.info("producer started")
    try:
        logger.info(f"trying to send message: {message}")
        value_json = json.dumps(message.__dict__).encode('utf-8')
        await producer.send_and_wait(KAFKA_TEST_TOPIC, value_json)
    finally:
        await producer.stop()
