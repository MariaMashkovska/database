from t08_flask_mysql.app.my_project.auth.dao import report_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ReportService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = report_dao
