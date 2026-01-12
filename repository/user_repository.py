from models.user_model import User
from repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    """User repository with CRUD methods"""
    
    def __init__(self):
        pass

    @classmethod
    def save_new_user(cls, user: User) -> User:
        """Save a new user to the database"""
        with cls._get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

