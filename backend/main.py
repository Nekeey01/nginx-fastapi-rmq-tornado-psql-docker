import asyncio
import json
import os
import tornado.escape
import tornado.ioloop
import tornado.web
from aio_pika import connect, Message
from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    async def post(self):
        body_json = tornado.escape.json_decode(self.request.body)

        print(f'body_json - {body_json}')

        await send_rabbitmq(body_json)


async def send_rabbitmq(data):
    # connection = await connect("amqp://guest:guest@localhost/")
    connection = await connect("amqp://guest:guest@rabbit1:5672/")

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(data).encode("utf-8")),
        routing_key="tornado_json"
    )

    await connection.close()


async def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),

        ],
        cookie_secret="11412412414",
        template_path=os.path.join(os.path.dirname(__file__), "../frontend"),
        xsrf_cookies=False,
        debug=options.debug,
    )
    app.listen(8888)

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
