from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import follower_controller
from t08_flask_mysql.app.my_project.auth.domain import Follower

follower_bp = Blueprint('followers', __name__, url_prefix='/followers')

@follower_bp.get('')
def get_all_followers() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(follower_controller.find_all()), HTTPStatus.OK)

@follower_bp.post('')
def create_follower() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    follower = Follower.create_from_dto(content)
    follower_controller.create(follower)
    return make_response(jsonify(follower.put_into_dto()), HTTPStatus.CREATED)

@follower_bp.get('/<int:follower_id>')
def get_follower(follower_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(follower_controller.find_by_id(follower_id)), HTTPStatus.OK)

@follower_bp.put('/<int:follower_id>')
def update_follower(follower_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    follower = Follower.create_from_dto(content)
    follower_controller.update(follower_id, follower)
    return make_response("Follower updated", HTTPStatus.OK)

@follower_bp.patch('/<int:follower_id>')
def patch_follower(follower_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    follower_controller.patch(follower_id, content)
    return make_response("Follower updated", HTTPStatus.OK)

@follower_bp.delete('/<int:follower_id>')
def delete_follower(follower_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    follower_controller.delete(follower_id)
    return make_response("Follower deleted", HTTPStatus.OK)

@follower_bp.post('/insert-follower')
def insert_follower() -> Response:
    data = request.get_json()
    user_account_userID = data.get('user_account_userID')
    user_account_userID1 = data.get('user_account_userID1')


    result = follower_controller.insert_follower(user_account_userID, user_account_userID1)
    return make_response(jsonify({'message': result}), HTTPStatus.OK)
