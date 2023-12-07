"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserAccount


class UserAccountDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = UserAccount

    def insert_user_account(self, nickname, follower_amount, photo_amount, storie_amount):
        try:
            self._session.execute(text(
                f"CALL InsertUserAccount('{nickname}', {follower_amount}, {photo_amount}, {storie_amount})"
            ))

            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"