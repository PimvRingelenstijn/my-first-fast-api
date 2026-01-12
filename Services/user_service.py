from apimodels.api_user import APIUser
from mappers.user_mappers import UserMapper
from repositories.user_repositories import UserRepository


class UserService:
    def __init__(self):
        pass

    def create_user(api_user: APIUser):
        print("service")
        db_user = UserMapper.api_user_to_db_user(api_user)
        print("service")
        UserRepository.save_new_user(db_user)
