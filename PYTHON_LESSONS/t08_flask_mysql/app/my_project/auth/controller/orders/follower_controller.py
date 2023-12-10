from t08_flask_mysql.app.my_project.auth.service import follower_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class FollowerController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = follower_service

    def insert_follower(self, user_account_userID, user_account_userID1):
        result = self._service.insert_follower(user_account_userID, user_account_userID1)
        return result
