from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Views(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "views"

    viewsID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    storie_storieID = db.Column(db.Integer, db.ForeignKey('storie.storieID'), primary_key=True)
    user_account_userID = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)
    report_reportID = db.Column(db.Integer, db.ForeignKey('report.reportID'), primary_key=True)

    # Add relationship to user_account
    user_account1 = db.relationship('UserAccount', foreign_keys=[user_account_userID], backref='views_detail')

    def __repr__(self) -> str:
        return f"Views(viewsID={self.viewsID}, storie_storieID={self.storie_storieID}, user_account_userID={self.user_account_userID}, report_reportID={self.report_reportID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "viewsID": self.viewsID,
            "storie_storieID": self.storie_storieID,
            "user_account_userID": self.user_account_userID,
            "user_info": {
                "userID": self.user_account1.userID,
                "nickname": self.user_account1.nickname,
                "follower_amount": self.user_account1.follower_amount,
                "photo_amount": self.user_account1.photo_amount,
                "storie_amount": self.user_account1.storie_amount,
            }
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Views:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Views(
            storie_storieID=dto_dict.get("storie_storieID"),
            user_account_userID=dto_dict.get("user_account_userID"),
        )
        return obj
