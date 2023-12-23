from flask import Blueprint

bp_tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp_tasks.route('/', methods=['GET'])
def index():
    return 'tasks!'

@bp_tasks.route('/<int:id>', methods=['GET'])
def show(id):
    return 'tasks!'

@bp_tasks.route('/', methods=['POST'])
def store():
    return 'tasks!'

@bp_tasks.route('/<int:id>', methods=['PUT'])
def update(id):
    return 'tasks!'

@bp_tasks.route('/<int:id>', methods=['DELETE'])
def destroy(id):
    return 'tasks!'
