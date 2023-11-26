"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao.orders import user_info_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserInfoService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = user_info_dao
