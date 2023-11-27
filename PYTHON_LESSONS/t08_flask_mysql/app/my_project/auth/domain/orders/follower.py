"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Follower(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "follower"

    user_account_userID = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)
    user_account_userID1 = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)

    follower_info = db.relationship('UserAccount', foreign_keys=[user_account_userID])
    follower_info1 = db.relationship('UserAccount', foreign_keys=[user_account_userID1])

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        return {
            "follower_info": self.follower_info.put_into_dto(),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Follower:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Follower(
            follower_info=dto_dict.get("follower_info"),
        )
        return obj