
import os.path


class SETTINGS:

    """
        A static class to hold all settings for this application.
    """

    """
        generic server settings
    """

    BASE_URL = os.path.dirname(__file__)

    SERVER_PORT = 8000
    SERVER_STATIC_PATH = os.path.join(BASE_URL, "frontend")
    SERVER_DEFAULT_FILENAME = "index.html"

