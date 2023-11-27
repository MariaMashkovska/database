from t08_flask_mysql.app.my_project.auth.service import views_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ViewsController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = views_service