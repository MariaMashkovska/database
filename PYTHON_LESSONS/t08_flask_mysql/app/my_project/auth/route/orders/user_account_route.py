"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_account_controller
from t08_flask_mysql.app.my_project.auth.domain import UserAccount

user_account_bp = Blueprint('user-accounts', __name__, url_prefix='/user-accounts')


@user_account_bp.get('')
def get_all_user_accounts() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(user_account_controller.find_all()), HTTPStatus.OK)


@user_account_bp.post('')
def create_user_account() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    user_account = UserAccount.create_from_dto(content)
    user_account_controller.create(user_account)
    return make_response(jsonify(user_account.put_into_dto()), HTTPStatus.CREATED)


@user_account_bp.get('/<int:user_account_id>')
def get_user_account(user_account_id: int) -> Response:
    """
    Gets client_type by ID.
    :return: Response object
    """
    return make_response(jsonify(user_account_controller.find_by_id(user_account_id)), HTTPStatus.OK)


@user_account_bp.put('/<int:user_account_id>')
def update_user_account(user_account_id: int) -> Response:
    """
    Updates client_type by ID.
    :return: Response object
    """
    content = request.get_json()
    client_type = UserAccount.create_from_dto(content)
    user_account_controller.update(user_account_id, client_type)
    return make_response("Client updated", HTTPStatus.OK)


@user_account_bp.patch('/<int:user_account_id>')
def patch_user_account(user_account_id: int) -> Response:
    """
    Patches client_type by ID.
    :return: Response object
    """
    content = request.get_json()
    user_account_controller.patch(user_account_id, content)
    return make_response("Client updated", HTTPStatus.OK)


@user_account_bp.delete('/<int:user_account_id>')
def delete_user_account(user_account_id: int) -> Response:
    """
    Deletes client_type by ID.
    :return: Response object
    """
    user_account_controller.delete(user_account_id)
    return make_response("Client deleted", HTTPStatus.OK)
