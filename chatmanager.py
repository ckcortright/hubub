

from settings_chatmanager import SETTINGS

import logging
import shlex
import tornado.ioloop
import tornado.log
import tornado.options
import tornado.web
import tornado.websocket

import chatmanager.bots
from chatmanager.user import User
from chatmanager.message import message_in, message_out


tornado.log.enable_pretty_logging()


def make_app():
    return tornado.web.Application([
        (r"/socket", ChatSocketHandler)
    ])


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    bots = chatmanager.bots.bots
    waiters = {}
    cache_size = 200

    def check_origin(self, origin):
        return True

    def open(self):
        ChatSocketHandler.waiters[self] = User(self)

    def on_close(self):
        del ChatSocketHandler.waiters[self]

    @classmethod
    def send_updates(cls, sender, msg):
        user = cls.get_user(sender)
        msg_text = message_in(msg)["text"]
        parsed_text = shlex.split(msg_text)
        for bot in cls.bots:
            if bot.is_match(parsed_text):
                sender.write_message(message_out(msg_text, user.nickname))
                bot.parse(cls, sender, parsed_text)
                return

        if not user.nickname or user.rad == 0:
            sender.write_message(message_out("User setup incomplete. Please set nickname/radius using the `@$nickname <name>`, `@$radius <radius-in-feet>` commands.", "@$setup", "error"))
            return

        logging.info("%s sending message to %d waiters", user.nickname, len(cls.waiters))
        for socket, waiter in cls.waiters.items():
            try:
                if waiter.nickname and waiter.rad and user.in_range(waiter):
                    socket.write_message(message_out(msg_text, user.nickname))
            except:
                logging.error("Error sending message", exc_info=True)

    @classmethod
    def get_user(cls, socket):
        return cls.waiters[socket]

    def on_message(self, message):
        logging.info("got message %r", message)
        ChatSocketHandler.send_updates(self, message)


if __name__ == "__main__":
    print("Starting server on port:", SETTINGS.SERVER_PORT)
    app = make_app()
    app.listen(SETTINGS.SERVER_PORT)
    tornado.ioloop.IOLoop.current().start()
