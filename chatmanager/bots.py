
import re
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

    def __init__(self, setting_name, validator_hint="", validator=lambda x: True, parser=lambda x: x):
        def eval_func(manager, socket, args):
            msg = " Could not change " + setting_name + ". " + validator_hint
            msg_type = "error"
            try:
                if len(args) == 2:
                    user = manager.waiters[socket]
                    val = parser(args[1])
                    if validator(val):
                        user[setting_name] = val
                        msg = "Success! Changed " + setting_name + " to " + str(val) + "."
                        msg_type = "success"
            except:
                pass
            socket.write_message(message_out(msg, _COMMAND_PREFIX, msg_type))

        super().__init__(setting_name, eval_func)


bots = [
    UserSettingBot(
        "nickname",
        "Nicknames can only have letters, numbers and underscores (a-zA-Z0-9_).",
        lambda x: re.match(r'^[A-Za-z0-9_]+$', x)
    ),
    UserSettingBot(
        "radius",
        "Radii must be positive real numbers.",
        lambda x: x > 0,
        lambda x: float(x)
    )
]
