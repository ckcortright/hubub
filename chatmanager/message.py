
import tornado.escape


def message_in(json):
    """
        A function to parse an incoming message object.
    """

    data = tornado.escape.json_decode(json)
    return {
        "text": data["text"]
    }


def message_out(text, user, msg_type=""):
    """
        A class to represent an outgoing message object.
    """

    return tornado.escape.json_encode({
        "text": text,
        "user": user,
        "type": msg_type
      })
