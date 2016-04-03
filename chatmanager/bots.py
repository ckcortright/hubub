
import re
import logging
from .message import message_out


_COMMAND_PREFIX = "@$"


class CommandBot:

    """
        A bot to respond to a given command.
    """

    def __init__(self, command, eval_func):
        self.command = command
        self.parse = eval_func

    def is_match(self, parsed_msg):
        return _COMMAND_PREFIX + self.command == parsed_msg[0]


class UserSettingBot(CommandBot):

    def __init__(self, cmd_name, setting_name, validator_hint="", validator=lambda x: True, parser=lambda x: x):
        def eval_func(manager, socket, args):
            msg = " Could not change " + cmd_name + ". " + validator_hint
            msg_type = "error"
            try:
                if len(args) == 2:
                    user = manager.waiters[socket]
                    val = parser(args[1])

                    if validator(val):
                        setattr(user, setting_name, val)
                        msg = "Success! Changed " + cmd_name + " to " + str(val) + "."
                        msg_type = "success"
            except Exception as err:
                logging.warning(str(err.msg))
            socket.write_message(message_out(msg, self.command, msg_type))

        super().__init__(cmd_name, eval_func)


bots = [
    UserSettingBot(
        "nickname",
        "nickname",
        "Nicknames can only have letters, numbers and underscores (a-zA-Z0-9_).",
        lambda x: re.match(r'^[A-Za-z0-9_]+$', x) is not None
    ),
    UserSettingBot(
        "radius",
        "rad",
        "Radii must be positive real numbers.",
        lambda x: x > 0,
        lambda x: float(x)
    ),
    UserSettingBot(
        "latitude",
        "lat",
        "Latitude is a real number between -90 and 90.",
        lambda x: -90 <= x <= 90,
        lambda x: float(x)
    ),
    UserSettingBot(
        "longitude",
        "lng",
        "Longitude is a real number between -180 and 180.",
        lambda x: -180 <= x <= 180,
        lambda x: float(x)
    )
]
