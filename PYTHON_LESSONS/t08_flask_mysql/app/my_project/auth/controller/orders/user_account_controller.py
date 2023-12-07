"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import user_account_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UserAccountController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = user_account_service

    def insert_user_account(self, nickname, follower_amount, photo_amount, storie_amount):
        result = self._service.insert_user_account(nickname, follower_amount, photo_amount, storie_amount)
        return result
