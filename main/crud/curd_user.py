from db.model.db_user import User
from db.database import SessionLocal

def get_user(user_email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == user_email).first()
    if user:
        return user.__dict__
    else:
        return None

def create_user(user):
    db = SessionLocal()
    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(id):
    db = SessionLocal()
    user = db.query(User).filter_by(id = id).first()
    if user:
        user.is_active = 0
        db.commit()
        return "successful"
    return "Not found"