from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


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
    account_info = db.relationship('Follower', foreign_keys='Follower.account', backref='account_obj')
    subscriptions_info = db.relationship('Follower', foreign_keys='Follower.followed_by', backref='followed_by_obj')
    stories_list = db.relationship('Storie', backref='user_account')
    views_details = db.relationship('Views', backref='user_account')

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        subscriptions = [{"userID": subscription.account_obj.userID,
                          "nickname": subscription.account_obj.nickname} for subscription in self.subscriptions_info]

        followers = [{"userID": subscription.followed_by_obj.userID,
                      "nickname": subscription.followed_by_obj.nickname} for subscription in self.account_info]

        user_info = [{"name": info.name,
                      "age": info.age,
                      "gender": info.gender} for info in self.user_details]

        stories_list = [{
            "storieID": storie.storieID,
            "views_amount": storie.views_amount,
        } for storie in self.stories_list]

        return {
            "userID": self.userID,
            "nickname": self.nickname,
            "follower_amount": self.follower_amount,
            "photo_amount": self.photo_amount,
            "storie_amount": self.storie_amount,
            "user_info": user_info,
            "stories_list": stories_list,
            "subscriptions": subscriptions,
            "followers": followers
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserAccount:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = UserAccount(
            nickname=dto_dict.get("nickname"),
            follower_amount=dto_dict.get("follower_amount"),
            photo_amount=dto_dict.get("photo_amount"),
            storie_amount=dto_dict.get("storie_amount"),
        )
        return obj
