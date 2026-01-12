from apimodels.api_user import APIUser
from models.user_model import User


class UserMapper:
    def __init__(self):
        pass

    @staticmethod
    def api_user_to_user(api_user: APIUser) -> User:
        """Convert APIUser to SQLModel User"""
        return User(name=api_user.name, email=api_user.email)