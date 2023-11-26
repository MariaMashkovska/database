from t08_flask_mysql.app.my_project.auth.service import statistic_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class StatisticController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = statistic_service