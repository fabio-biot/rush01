from ..models.tables import *
from .database_management import SessionLocal, engine
from ..services.context_sql_makers import *

db = SessionLocal()

def update_user_table(data_user: dict):
    new_user = User(
        username=data_user.get("username"),
        email=data_user.get("email"),
        password_hash=data_user.get("password_hash")
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()