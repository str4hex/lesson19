from dao.model.user import UserModel


class UserDao:

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(UserModel).get(uid)

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

    def get_by_username(self, usernames):
        return self.session.query(UserModel).filter(UserModel.username == usernames).first()