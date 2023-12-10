"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Report


class ReportDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Report

    def insert_report(self, reportID, text1):
        try:
            self._session.execute(text(
                f"CALL InsertReport('{reportID}', {text1})"
            ))

            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
