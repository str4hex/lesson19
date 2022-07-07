import hashlib
import base64
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDao


class UserService:

    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def user_create(self, data):
        data['password'] = self.get_hash(data.get('password'))
        return self.dao.create_user(data)

    def delete_user(self, uid):
        return self.dao.delete_user(uid)

    def update_user(self, data):
        return self.dao.update_user(data)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self,password, password_hash):
        return hmac.compare_digest(self.get_hash(password), password_hash)