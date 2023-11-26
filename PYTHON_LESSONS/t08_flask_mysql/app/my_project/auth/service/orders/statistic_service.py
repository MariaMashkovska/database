from t08_flask_mysql.app.my_project.auth.dao import statistic_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class StatisticService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = statistic_dao
