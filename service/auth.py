import calendar
import datetime

from constants import JWT_ALG, JWT_SECRET
import jwt
from service.user import UserService


class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)
        if not user:
            return False
        if not is_refresh:
            if not self.user_service.compare_password(password, user.password):
                return False

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALG)

        min30 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALG)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def refresh_token(self, token):
        data = jwt.decode(token, JWT_SECRET, JWT_ALG)
        username = data["username"]
        user = self.user_service.get_by_username(username)

        if not user:
            return False

        now = calendar.timegm((datetime.datetime.utcnow().timetuple()))
        expired = data['exp']
        if now > expired:
            return False
        return self.generate_tokens(username, user.password, is_refresh=True)
