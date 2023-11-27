from t08_flask_mysql.app.my_project.auth.dao import reactions_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ReactionsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = reactions_dao
