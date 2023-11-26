from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.storie import Storie
from t08_flask_mysql.app.my_project.auth.domain.orders.user_account import UserAccount

class Media(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "media"

    mediaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    media_url = db.Column(db.String(250), nullable=False)
    media_type = db.Column(db.String(10), nullable=True)
    storie_storieID = db.Column(db.Integer, db.ForeignKey('storie.storieID'), primary_key=True)
    storie_user_account_userID = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)

    storie_info = db.relationship('Storie', foreign_keys=[storie_storieID], backref="media_detail")
    user_account_info = db.relationship('UserAccount', foreign_keys=[storie_user_account_userID], backref="media_detail2")

    def __repr__(self) -> str:
        return f"Media(mediaID={self.mediaID}, media_url={self.media_url}, media_type={self.media_type}, storie_storieID={self.storie_storieID}, storie_user_account_userID={self.storie_user_account_userID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "mediaID": self.mediaID,
            "media_url": self.media_url,
            "media_type": self.media_type,
            "storie_storieID": self.storie_storieID,
            "storie_user_account_userID": self.storie_user_account_userID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Media:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Media(
            media_url=dto_dict.get("media_url"),
            media_type=dto_dict.get("media_type"),
            storie_storieID=dto_dict.get("storie_storieID"),
            storie_user_account_userID=dto_dict.get("storie_user_account_userID"),
        )
        return obj
