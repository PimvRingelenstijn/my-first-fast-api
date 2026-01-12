from os import name

from apimodels.api_user import APIUser
from apimodels.db_user import DbUser


class UserMapper:
    def __init__(self):
        pass

    def api_user_to_db_user(api_user: APIUser) -> DbUser:
        db_user = DbUser(name=api_user.name, password=api_user.password)
        print("mappers")
        return db_user