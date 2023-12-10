"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserInfo


class UserInfoDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = UserInfo

    def insert_names_into_user_info(self):
        try:
            self._session.execute(text(
                f"CALL InsertNamesIntoUserInfo()"
            ))

            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"

    def get_max_age_user_info(self):
        try:
            result = self._session.execute(text("SELECT getMaxAgeUserInfo();"))
            max_age = result.scalar()  # Use scalar() to get a single value from the query
            return max_age
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
