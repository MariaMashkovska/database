"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class UserInfo(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "user_info"

    user_infoID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(30))
    user_account_userID = db.Column(db.Integer, db.ForeignKey('user_account.userID'))

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"UserInfo({self.user_infoID}, '{self.name}', '{self.age}', '{self.gender}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "user_infoID": self.user_infoID,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "user_account_userID": self.user_account_userID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserInfo:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = UserInfo(
            name=dto_dict.get("name"),
            age=dto_dict.get("age"),
            gender=dto_dict.get("gender"),
            user_account_userID=dto_dict.get("user_account_userID"),
        )
        return obj