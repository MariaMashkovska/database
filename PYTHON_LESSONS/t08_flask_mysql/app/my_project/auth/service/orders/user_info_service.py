"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import user_info_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserInfoService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = user_info_dao

    def insert_names_into_user_info(self):
        result = self._dao.insert_names_into_user_info()
        return result

    def get_max_age_user_info(self):
        result = self._dao.get_max_age_user_info()
        return result
