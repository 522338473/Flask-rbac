from flask import Blueprint

rbac = Blueprint('rbac', __name__)

from . import views
