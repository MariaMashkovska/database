"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Storie


class StorieDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Storie

    def insert_storie(self):
        try:
            self._session.execute(text(
                f"CALL InsertStorie()"
            ))

            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
