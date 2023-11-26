from t08_flask_mysql.app.my_project.auth.dao import storie_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class StorieService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = storie_dao
