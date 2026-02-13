from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

def create_user(db: Session, email: str, password: str, role: str) -> User:
    hashed_pw = hash_password(password)

    user = User(
        email=email,
        hashed_password=hashed_pw,
        role=role,
        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
