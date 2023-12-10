from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import report_controller
from t08_flask_mysql.app.my_project.auth.domain import Report

report_bp = Blueprint('reports', __name__, url_prefix='/reports')

@report_bp.get('')
def get_all_reports() -> Response:
    """
    Gets all objects from the follower table using the service layer.
    :return: Response object
    """
    return make_response(jsonify(report_controller.find_all()), HTTPStatus.OK)

@report_bp.post('')
def create_report() -> Response:
    """
    Creates a new follower using the service layer.
    :return: Response object
    """
    content = request.get_json()
    report = Report.create_from_dto(content)
    report_controller.create(report)
    return make_response(jsonify(report.put_into_dto()), HTTPStatus.CREATED)

@report_bp.get('/<int:report_id>')
def get_report(report_id: int) -> Response:
    """
    Gets a follower by ID using the service layer.
    :return: Response object
    """
    return make_response(jsonify(report_controller.find_by_id(report_id)), HTTPStatus.OK)

@report_bp.put('/<int:report_id>')
def update_report(report_id: int) -> Response:
    """
    Updates a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    statistic = Report.create_from_dto(content)
    report_controller.update(report_id, statistic)
    return make_response("Report updated", HTTPStatus.OK)

@report_bp.patch('/<int:report_id>')
def patch_report(report_id: int) -> Response:
    """
    Patches a follower by ID using the service layer.
    :return: Response object
    """
    content = request.get_json()
    report_controller.patch(report_id, content)
    return make_response("Report updated", HTTPStatus.OK)

@report_bp.delete('/<int:statistic_id>')
def delete_report(report_id: int) -> Response:
    """
    Deletes a follower by ID using the service layer.
    :return: Response object
    """
    report_controller.delete(report_id)
    return make_response("Report deleted", HTTPStatus.OK)

@report_bp.post('/insert-report')
def insert_report() -> Response:
    data = request.get_json()
    reportID = data.get('reportID')
    text = data.get('text')

    result = report_controller.insert_report(reportID, text)
    return make_response(jsonify({'message': result}), HTTPStatus.OK)

