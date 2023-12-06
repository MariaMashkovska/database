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

    account = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)
    followed_by = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)

    # account = db.relationship('UserAccount', foreign_keys=[user_account_userID])
    # followed_by = db.relationship('UserAccount', foreign_keys=[user_account_userID1])

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """


        return {
            "account":  {
                "userID": self.account_obj.userID,
                "nickname": self.account_obj.nickname,
                "follower_amount": self.account_obj.follower_amount,
                "photo_amount": self.account_obj.photo_amount,
                "storie_amount": self.account_obj.storie_amount,
            },
            "followed_by": {
                "userID": self.followed_by_obj.userID,
                "nickname": self.followed_by_obj.nickname,
                "follower_amount": self.followed_by_obj.follower_amount,
                "photo_amount": self.followed_by_obj.photo_amount,
                "storie_amount": self.followed_by_obj.storie_amount,
            }
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Follower:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Follower(
            followed_by=dto_dict.get("followed_by"),
            account=dto_dict.get("account"),
        )
        return obj
