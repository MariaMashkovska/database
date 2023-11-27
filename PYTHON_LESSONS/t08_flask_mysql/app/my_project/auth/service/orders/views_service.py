from t08_flask_mysql.app.my_project.auth.dao import views_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ViewsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = views_dao
