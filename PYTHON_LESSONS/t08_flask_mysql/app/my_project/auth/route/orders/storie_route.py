from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import storie_controller
from t08_flask_mysql.app.my_project.auth.domain import Storie

storie_bp = Blueprint('stories', __name__, url_prefix='/stories')


@storie_bp.get('')
def get_all_stories() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(storie_controller.find_all()), HTTPStatus.OK)


@storie_bp.post('')
def create_stories() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    storie = Storie.create_from_dto(content)
    storie_controller.create(storie)
    return make_response(jsonify(storie.put_into_dto()), HTTPStatus.CREATED)


@storie_bp.get('/<int:storie_id>')
def get_stories(storie_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(storie_controller.find_by_id(storie_id)), HTTPStatus.OK)


@storie_bp.put('/<int:storie_id>')
def update_stories(storie_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    storie = Storie.create_from_dto(content)
    storie_controller.update(storie_id, storie)
    return make_response("Follower updated", HTTPStatus.OK)


@storie_bp.patch('/<int:storie_id>')
def patch_stories(storie_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    storie_controller.patch(storie_id, content)
    return make_response("Follower updated", HTTPStatus.OK)


@storie_bp.delete('/<int:storie_id>')
def delete_stories(storie_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    storie_controller.delete(storie_id)
    return make_response("Follower deleted", HTTPStatus.OK)


@storie_bp.post('/insert-storie')
def insert_storie() -> Response:
    data = request.get_json()
    storieID = data.get('storieID')
    follower_id = data.get('follower_id')
    views_amount = data.get('views_amount')
    user_account_userID = data.get('user_account_userID')

    result = storie_controller.insert_storie(storieID, follower_id, views_amount, user_account_userID)
    return make_response(jsonify({'message': result}), HTTPStatus.OK)
