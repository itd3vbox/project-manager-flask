from flask import Blueprint

bp_projects = Blueprint('projects', __name__, url_prefix='/projects')

@bp_projects.route('/', methods=['GET'])
def index():
    return 'projects!'

@bp_projects.route('/<int:id>', methods=['GET'])
def show(id):
    return 'projects!'

@bp_projects.route('/', methods=['POST'])
def store():
    return 'projects!'

@bp_projects.route('/<int:id>', methods=['PUT'])
def update(id):
    return 'projects!'

@bp_projects.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    return 'projects!'
