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
        # follower_info = []
        # for info in self.follower_info:
        #     follower_info_dto = ClientType.put_into_dto(info)
        #     follower_info.append(follower_info_dto)
        #
        # follower_info1 = []
        # for info in self.follower_info1:
        #     follower_info1_dto = ClientType.put_into_dto(info)
        #     follower_info1.append(follower_info1_dto)

        return {
            "follower_info": self.follower_info.put_into_dto(),
            "follower_info1":  self.follower_info1.put_into_dto(),
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
            follower_info1=dto_dict.get("follower_info1"),
        )
        return obj