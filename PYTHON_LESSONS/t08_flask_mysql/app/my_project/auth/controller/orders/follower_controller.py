from t08_flask_mysql.app.my_project.auth.service import follower_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FollowerController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = follower_service