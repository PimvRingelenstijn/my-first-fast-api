from apimodels.api_user import APIUser
from mappers.user_mappers import UserMapper
from repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        pass

    @staticmethod
    def create_user(api_user: APIUser) -> dict:
        """Create a new user"""
        user = UserMapper.api_user_to_user(api_user)
        saved_user = UserRepository.save_new_user(user)
        return {
            "id": saved_user.id,
            "name": saved_user.name,
            "email": saved_user.email
        }
