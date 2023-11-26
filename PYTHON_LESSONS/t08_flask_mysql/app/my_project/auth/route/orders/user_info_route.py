"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_info_controller
from t08_flask_mysql.app.my_project.auth.domain import UserInfo

user_info_bp = Blueprint('user-info', __name__, url_prefix='/users-info')


@user_info_bp.get('')
def get_all_user_info() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(user_info_controller.find_all()), HTTPStatus.OK)


@user_info_bp.post('')
def create_user_info() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    client = UserInfo.create_from_dto(content)
    user_info_controller.create(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED)


@user_info_bp.get('/<int:user_info_id>')
def get_user_info(user_info_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(user_info_controller.find_by_id(user_info_id)), HTTPStatus.OK)


@user_info_bp.put('/<int:user_info_id>')
def update_user_info(user_info_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    user_info = UserInfo.create_from_dto(content)
    user_info_controller.update(user_info_id, user_info)
    return make_response("Client updated", HTTPStatus.OK)


@user_info_bp.patch('/<int:user_info_id>')
def patch_user_info(user_info_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    user_info_controller.patch(user_info_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@user_info_bp.delete('/<int:user_info_id>')
def delete_user_info(user_info_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    user_info_controller.delete(user_info_id)
    return make_response("Client deleted", HTTPStatus.OK)
