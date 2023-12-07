"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Follower


class FollowerDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Follower

    def insert_follower(self, user_account_userID, user_account_userID1):
        try:
            self._session.execute(text(
                f"CALL InsertFollower({user_account_userID}, '{user_account_userID1}')",
            ))
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"

    def create_dynamic_databases(self):
        try:
            self._session.execute("CALL CreateDynamicDataBases()")
            self._session.commit()
            return "Created successfully"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"