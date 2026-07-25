from ..models.tables import *
from .database_management import SessionLocal, engine
from ..services.context_sql_makers import *

db = SessionLocal()

def update_user_table(data_user: dict):
    new_user = User(
        username=data_user.get("username"),
        email=data_user.get("email"),
        first_name = data_user.get("first_name"),
        last_name = data_user.get("last_name"),
        password_hash=data_user.get("password_hash")
    )
    print(new_user.password_hash)
    print(new_user.first_name)
    print(new_user.last_name)
    print(new_user.email)
    print(new_user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()