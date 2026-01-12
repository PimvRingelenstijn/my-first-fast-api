from fastapi import APIRouter

from Services.user_service import UserService
from apimodels.api_user import APIUser


class UserRouter:
    router = APIRouter()

    @router.get("/hi")
    def root():
        return {"message": "Hello World"}

    @router.post("/create-user")
    def create_user(api_user: APIUser):
        """Create a new user"""
        return UserService.create_user(api_user)