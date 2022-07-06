from dao.model.user import UserModel


class UserDao:

    def __init__(self, session):
        self.session = session

    def create_user(self, data):
        user_json = UserModel(**data)
        self.session.add(user_json)
        self.session.commit()
        return user_json

    def delete_user(self,uid):
        user = self.session.get(uid)
        self.session.delete(user)
        self.session.commit()



