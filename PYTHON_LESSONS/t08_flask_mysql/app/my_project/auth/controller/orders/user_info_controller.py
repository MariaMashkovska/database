"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import user_info_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UserInfoController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = user_info_service

    def insert_names_into_user_info(self):
        result = self._service.insert_names_into_user_info()
        return result

    def get_max_age_user_info(self):
        result = self._service.get_max_age_user_info()
        return result