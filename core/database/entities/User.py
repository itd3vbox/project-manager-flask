from core.database.database import db
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(db.Model):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, nullable=False) 
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, nullable=False) 

    def __repr__(self):
        return f'<User(id={self.id}, username={self.username}, email={self.email}, ' \
               f'password={self.password}, created_at={self.created_at}, updated_at={self.updated_at})>'