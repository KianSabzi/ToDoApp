from flask import Blueprint

task_api_blueprint = Blueprint('task_api', __name__)

from . import routes
