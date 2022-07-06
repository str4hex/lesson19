import hashlib
import base64
base64.b64encode(bytes('your string', 'utf-8'))
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDao

class UserService:

    def __init__(self, dao: UserDao):
        self.dao = dao

    def user_create(self,data):
        data['password'] = self.get_hash(data.get('password'))
        return self.dao.create_user(data)

    def delete_user(self, uid):
        return self.dao.delete_user(uid)

    def get_hash(self, password):

        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))
