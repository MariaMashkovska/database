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
