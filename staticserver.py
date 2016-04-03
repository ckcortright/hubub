

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


if __name__ == "__main__":
    print("Starting server on port:", SETTINGS.SERVER_PORT)
    app = make_app()
    app.listen(SETTINGS.SERVER_PORT)
    tornado.ioloop.IOLoop.current().start()
