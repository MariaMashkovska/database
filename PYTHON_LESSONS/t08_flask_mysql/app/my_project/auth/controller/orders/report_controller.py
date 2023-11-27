from t08_flask_mysql.app.my_project.auth.service import report_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ReportController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = report_service