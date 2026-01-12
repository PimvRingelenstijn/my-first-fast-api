"""Database viewer script to easily view database contents"""
from sqlmodel import Session, create_engine, select
from models.user_model import User

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})


def view_users():
    """View all users in the database"""
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        
        if not users:
            print("No users found in the database.")
            return
        
        print(f"\nFound {len(users)} user(s):")
        print("-" * 50)
        for user in users:
            print(f"ID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print("-" * 50)


if __name__ == "__main__":
    print("Viewing database contents...")
    view_users()

