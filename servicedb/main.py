from aio_pika import connect, IncomingMessage
import json
from fastapi import FastAPI
from sql_app import crud
from sql_app.db import db

app = FastAPI()

async def create_rmq(message: IncomingMessage):

    txt = message.body.decode("utf-8")
    json_txt = json.loads(txt)
    print(f'json_txt - {json_txt}')

    await crud.create_user(user=json_txt)


@app.on_event("startup")
async def main():

    await db.connect()
    print("Startup FastApi")
    print(f'db - {db.url}')

    # connection = await connect("amqp://guest:guest@localhost/")
    connection = await connect("amqp://guest:guest@rabbit1:5672/")

    channel = await connection.channel()

    queue = await channel.declare_queue("tornado_json")

    await queue.consume(create_rmq, no_ack = True)

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
