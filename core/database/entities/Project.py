from core.database.database import db
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Project(db.Model):

    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description_short: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False)  
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, nullable=False) 
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow, nullable=False) 

    def __repr__(self):
        return f'<Project(id={self.id}, name={self.name}, description_short={self.description_short}, ' \
               f'status={self.status}, created_at={self.created_at}, updated_at={self.updated_at})>'
