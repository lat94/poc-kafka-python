import asyncio
from fastapi import FastAPI
from datetime import datetime
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .routers import test_kafka_producer
from .kafka import segment_image_consumer
from loguru import logger

app = FastAPI()
app.include_router(test_kafka_producer.router)

UPTIME = datetime.utcnow().strftime('%c')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def start_kafka_consumer():
    await segment_image_consumer.consume_messages_from_kafka()


async def startup_event():
    asyncio.ensure_future(start_kafka_consumer())

app.add_event_handler('startup', startup_event)


@app.get('/')
async def health_check():
    response = {
        'name': 'poc-kafka-python',
        'status': 'ON',
        'started_time': UPTIME,
        'now': datetime.utcnow().strftime('%c'),
    }

    return response


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(2050))
