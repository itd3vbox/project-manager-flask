from flask import Blueprint

bp_settings = Blueprint('settings', __name__, url_prefix='/settings')

@bp_settings.route('/', methods=['GET'])
def index():
    return 'settings!'

@bp_settings.route('/<int:id>/username', methods=['PUT'])
def updateUsername(id):
    return 'settings!'

@bp_settings.route('/<int:id>/email', methods=['PUT'])
def updateEmail(id):
    return 'settings!'

@bp_settings.route('/<int:id>/email', methods=['PUT'])
def updatePassword(id):
    return 'settings!'
