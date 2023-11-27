from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import views_controller
from t08_flask_mysql.app.my_project.auth.domain import Views

views_bp = Blueprint('views', __name__, url_prefix='/views')

@views_bp.get('')
def get_all_views() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(views_controller.find_all()), HTTPStatus.OK)

@views_bp.post('')
def create_views() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    views = Views.create_from_dto(content)
    views_controller.create(views)
    return make_response(jsonify(views.put_into_dto()), HTTPStatus.CREATED)

@views_bp.get('/<int:views_id>')
def get_views(views_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(views_controller.find_by_id(views_id)), HTTPStatus.OK)

@views_bp.put('/<int:views_id>')
def update_views(views_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    views = Views.create_from_dto(content)
    views_controller.update(views_id, views)
    return make_response("Follower updated", HTTPStatus.OK)

@views_bp.patch('/<int:views_id>')
def patch_views(views_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    views_controller.patch(views_id, content)
    return make_response("Follower updated", HTTPStatus.OK)

@views_bp.delete('/<int:views_id>')
def delete_views(views_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    views_controller.delete(views_id)
    return make_response("Follower deleted", HTTPStatus.OK)
