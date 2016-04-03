
import math


class User:

    def __init__(self, socket):
        self.nickname = None
        self.lat = 0
        self.lng = 0
        self.rad = 0

    def in_range(self, user):
        """
            Uses the haversine formula (for great circle distance)
            to tell if self and user are in range.
        """
        dlat = self.lat - user.lat
        dlng = self.lng - user.lng

        a = math.sin(dlat/2)**2 + \
            math.cos(self.lat)*math.cos(user.lat)*math.sin(dlng/2)**2
        c = 2 * math.asin(math.sqrt(a))

        m = 6367000 * c
        rad = min(self.rad, user.rad)

        return m <= rad

