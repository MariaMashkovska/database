"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import user_account_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserAccountService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = user_account_dao

    def insert_user_account(self, nickname, follower_amount, photo_amount, storie_amount):
        result = self._dao.insert_user_account(nickname, follower_amount, photo_amount, storie_amount)
        return result

