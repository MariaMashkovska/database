from t08_flask_mysql.app.my_project.auth.dao import follower_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class FollowerService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = follower_dao
