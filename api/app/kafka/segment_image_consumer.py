from ..environment import KAFKA_TEST_TOPIC, KAFKA_BOOTSTRAP_SERVERS, KAFKA_MY_GROUP_GROUP_ID
from loguru import logger
from aiokafka import AIOKafkaConsumer


async def consume_messages_from_kafka():
    consumer = AIOKafkaConsumer(
        KAFKA_TEST_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_MY_GROUP_GROUP_ID
    )
    await consumer.start()
    logger.info(f"consumer started")
    try:
        async for msg in consumer:
            logger.info(f'received message: {msg}')
    finally:
        await consumer.stop()
