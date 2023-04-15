from ..kafka import segment_image_producer
from fastapi import APIRouter, BackgroundTasks
from ..kafka.schema import Message
import lorem


router = APIRouter(
    prefix="/test",
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def send_message(background_tasks: BackgroundTasks):
    background_tasks.add_task(
        segment_image_producer.produce, Message(content=lorem.sentence())
    )
    return {'message': 'Message sent to Kafka'}
