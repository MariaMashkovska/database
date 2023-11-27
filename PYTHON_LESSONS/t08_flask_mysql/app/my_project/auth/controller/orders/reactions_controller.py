from t08_flask_mysql.app.my_project.auth.service import reactions_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ReactionsController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = reactions_service