from t08_flask_mysql.app.my_project.auth.service import storie_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class StorieController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = storie_service