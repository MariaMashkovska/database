from t08_flask_mysql.app.my_project.auth.dao import follower_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class FollowerService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = follower_dao

    def insert_follower(self, user_account_userID, user_account_userID1):
        result = self._dao.insert_follower(user_account_userID, user_account_userID1)
        return result