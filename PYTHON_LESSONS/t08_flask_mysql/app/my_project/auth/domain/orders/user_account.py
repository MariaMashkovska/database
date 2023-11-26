"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.user_info import UserInfo

class UserAccount(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "user_account"

    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(30), nullable=False)
    follower_amount = db.Column(db.Integer, nullable=False)
    photo_amount = db.Column(db.Integer)
    storie_amount = db.Column(db.Integer)
    user_details = db.relationship("UserInfo", backref='user_account')
    follower_info = db.relationship('Follower', foreign_keys='Follower.user_account_userID', backref='follower_detail')
    follower_info1 = db.relationship('Follower', foreign_keys='Follower.user_account_userID1', backref='follower_detail1')


    #
    # def __repr__(self) -> str:
    #     return f"ClientType({self.id}, '{self.type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        user_info = []
        for info in self.user_details:
            user_info_dto = UserInfo.put_into_dto(info)
            user_info.append(user_info_dto)

        return {
            "userID": self.userID,
            "nickname": self.nickname,
            "follower_amount": self.follower_amount,
            "photo_amount": self.photo_amount,
            "storie_amount": self.storie_amount,
            "user_info": user_info
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserAccount:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = UserAccount(nickname=dto_dict.get("nickname"),
                         follower_amount=dto_dict.get("follower_amount"),
                         photo_amount=dto_dict.get("photo_amount"),
                         storie_amount=dto_dict.get("storie_amount"),
                         user_info=dto_dict.get("user_info"))
        return obj
