from t08_flask_mysql.app.my_project.auth.dao import report_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ReportService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = report_dao

    def insert_report(self):
        result = self._dao.insert_report()
        return result
