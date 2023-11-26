from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import statistic_controller
from t08_flask_mysql.app.my_project.auth.domain import Statistic

statistic_bp = Blueprint('statistics', __name__, url_prefix='/statistics')

@statistic_bp.get('')
def get_all_statistic() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(statistic_controller.find_all()), HTTPStatus.OK)

@statistic_bp.post('')
def create_statistic() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    statistic = Statistic.create_from_dto(content)
    statistic_controller.create(statistic)
    return make_response(jsonify(statistic.put_into_dto()), HTTPStatus.CREATED)

@statistic_bp.get('/<int:statistic_id>')
def get_follower(statistic_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(statistic_controller.find_by_id(statistic_id)), HTTPStatus.OK)

@statistic_bp.put('/<int:statistic_id>')
def update_follower(statistic_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    statistic = Statistic.create_from_dto(content)
    statistic_controller.update(statistic_id, statistic)
    return make_response("Follower updated", HTTPStatus.OK)

@statistic_bp.patch('/<int:statistic_id>')
def patch_follower(statistic_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    statistic_controller.patch(statistic_id, content)
    return make_response("Follower updated", HTTPStatus.OK)

@statistic_bp.delete('/<int:statistic_id>')
def delete_follower(statistic_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    statistic_controller.delete(statistic_id)
    return make_response("Follower deleted", HTTPStatus.OK)
