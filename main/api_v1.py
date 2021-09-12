from flask import Blueprint, current_app
from flask_restx import Api

from main.booking import ns as ns_booking


blueprint = Blueprint('api_1_0', __name__)


api = Api(
    blueprint,
    doc=current_app.config['API_DOCS_URL'],
    catch_all_404s=True
)
api.namespaces.clear()
api.add_namespace(ns_booking)
