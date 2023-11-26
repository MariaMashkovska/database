from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import media_controller
from t08_flask_mysql.app.my_project.auth.domain import Media

media_bp = Blueprint('media', __name__, url_prefix='/media')

@media_bp.get('')
def get_all_media() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(media_controller.find_all()), HTTPStatus.OK)

@media_bp.post('')
def create_media() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    media = Media.create_from_dto(content)
    media_controller.create(media)
    return make_response(jsonify(media.put_into_dto()), HTTPStatus.CREATED)

@media_bp.get('/<int:media_id>')
def get_media(media_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(media_controller.find_by_id(media_id)), HTTPStatus.OK)

@media_bp.put('/<int:media_id>')
def update_media(media_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    media = Media.create_from_dto(content)
    media_controller.update(media_id, media)
    return make_response("Follower updated", HTTPStatus.OK)

@media_bp.patch('/<int:media_id>')
def patch_media(media_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    media_controller.patch(media_id, content)
    return make_response("Follower updated", HTTPStatus.OK)

@media_bp.delete('/<int:media_id>')
def delete_media(media_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    media_controller.delete(media_id)
    return make_response("Follower deleted", HTTPStatus.OK)
