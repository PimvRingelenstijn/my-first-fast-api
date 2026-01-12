from apimodels.db_user import DbUser
from repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    """User repository with CRUD methods"""
    
    def __init__(self):
        pass

    def save_new_user(db_user: DbUser):
        print("repositories")
        print(f"User {db_user.name} has been created.")

