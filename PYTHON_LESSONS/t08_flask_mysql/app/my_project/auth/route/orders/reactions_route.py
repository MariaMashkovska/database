from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import reactions_controller
from t08_flask_mysql.app.my_project.auth.domain import Reactions

reactions_bp = Blueprint('reactions', __name__, url_prefix='/reactions')

@reactions_bp.get('')
def get_all_sreactions() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(reactions_controller.find_all()), HTTPStatus.OK)

@reactions_bp.post('')
def create_reactions() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    reactions = Reactions.create_from_dto(content)
    reactions_controller.create(reactions)
    return make_response(jsonify(reactions.put_into_dto()), HTTPStatus.CREATED)

@reactions_bp.get('/<int:reactions_id>')
def get_follower(reactions_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(reactions_controller.find_by_id(reactions_id)), HTTPStatus.OK)

@reactions_bp.put('/<int:reactions_id>')
def update_follower(reactions_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    reactions = Reactions.create_from_dto(content)
    reactions_controller.update(reactions_id, reactions)
    return make_response("Follower updated", HTTPStatus.OK)

@reactions_bp.patch('/<int:reactions_id>')
def patch_follower(reactions_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    reactions_controller.patch(reactions_id, content)
    return make_response("Follower updated", HTTPStatus.OK)

@reactions_bp.delete('/<int:reactions_id>')
def delete_follower(reactions_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    reactions_controller.delete(reactions_id)
    return make_response("Follower deleted", HTTPStatus.OK)
