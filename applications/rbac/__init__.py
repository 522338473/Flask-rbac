from flask import Blueprint

rbac = Blueprint('rbac', __name__)

from . import templatetags
from . import views
