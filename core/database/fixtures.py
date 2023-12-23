from core.database.database import db
from core.database.entities.User import User
from core.database.entities.Project import Project
from core.database.entities.Task import Task

def fixtures():
    # Delete tables
    db.drop_all()
    # Creaye tables
    db.create_all()
    
    # Add user
    db.session.add(User(username='john', email='john@example.com', password="azerty"))
    db.session.commit()

    # fetch all users
    users = User.query.all()
    print("users", users)