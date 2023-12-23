from flask import Flask
from core.projects.routes import bp_projects
from core.tasks.routes import bp_tasks
from core.settings.routes import bp_settings
from core.database.database import db
from core.database.fixtures import fixtures

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register blueprints
app.register_blueprint(bp_projects)
app.register_blueprint(bp_tasks)
app.register_blueprint(bp_settings)

db.init_app(app)

with app.app_context():
    fixtures()
    
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)