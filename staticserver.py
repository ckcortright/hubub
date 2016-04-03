

from settings_static import SETTINGS

#import logging
import tornado.escape
import tornado.ioloop
#import tornado.log
import tornado.options
import tornado.web
import tornado.websocket


tornado.log.enable_pretty_logging()


def make_app():
    return tornado.web.Application([
        #(r"/socket", ChatSocketHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {
            "path": SETTINGS.SERVER_STATIC_PATH,
            "default_filename": SETTINGS.SERVER_DEFAULT_FILENAME
        })
    ])


#class ChatSocketHandler(tornado.websocket.WebSocketHandler):
#    waiters = set()
#    cache = []
#    cache_size = 200

#    def get_compression_options(self):
#        # Non-None enables compression with default options.
#        return {}

#    def open(self):
#        logging.info("hello world")
#        ChatSocketHandler.waiters.add(self)

#    def on_close(self):
#        ChatSocketHandler.waiters.remove(self)

#    #@classmethod
#    #def update_cache(cls, chat):
#    #    cls.cache.append(chat)
#    #    if len(cls.cache) > cls.cache_size:
#    #        cls.cache = cls.cache[-cls.cache_size:]

#    @classmethod
#    def send_updates(cls, chat):
#        logging.info("sending message to %d waiters", len(cls.waiters))
#        for waiter in cls.waiters:
#            try:
#                waiter.write_message(chat)
#            except:
#                logging.error("Error sending message", exc_info=True)

#    def on_message(self, message):
#        logging.info("got message %r", message)
#        ChatSocketHandler.send_updates(message)
#        #parsed = tornado.escape.json_decode(message)
#        #chat = {
#        #
#        #}
#        #ChatSocketHandler.update_cache(chat)
#        #ChatSocketHandler.send_updates(chat)


if __name__ == "__main__":
    print("Starting server on port:", SETTINGS.SERVER_PORT)
    app = make_app()
    app.listen(SETTINGS.SERVER_PORT)
    tornado.ioloop.IOLoop.current().start()
