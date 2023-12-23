from core.database.database import db
from sqlalchemy import Integer, String, DateTime, JSON
from sqlalchemy.orm import  Mapped, mapped_column
from datetime import datetime

class Task(db.Model):

    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description_short: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(JSON, nullable=False)
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False)  
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, nullable=False) 
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, nullable=False) 

    def __repr__(self):
        return f'<Task(id={self.id}, title={self.title}, description_short={self.description_short}, ' \
               f'description={self.description}, status={self.status}, created_at={self.created_at}, ' \
               f'updated_at={self.updated_at})>'