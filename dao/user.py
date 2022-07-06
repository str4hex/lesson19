from dao.model.user import UserModel


class UserDao:

    def __init__(self, session):
        self.session = session

    def create_user(self, data):
        user_json = UserModel(**data)
        self.session.add(user_json)
        self.session.commit()
        return user_json

    def delete_user(self, uid):
        user = self.session.query(UserModel).get(uid)
        self.session.delete(user)
        self.session.commit()

    def update_user(self, data):
        user = UserModel(**data)
        self.session.add(user)
        self.session.commit()