from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Reactions(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "reactions"

    reactionsID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reactions_type = db.Column(db.String(3663), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)
    views_viewsID = db.Column(db.Integer, db.ForeignKey('views.viewsID'), primary_key=True)
    views_storie_storieID = db.Column(db.Integer, db.ForeignKey('views.storie_storieID'), primary_key=True)

    user_account = db.relationship('UserAccount', backref='reactions_detail')

    def __repr__(self) -> str:
        return f"Reactions(reactionsID={self.reactionsID}, reactions_type={self.reactions_type}, userID={self.userID}, views_viewsID={self.views_viewsID}, views_storie_storieID={self.views_storie_storieID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "reactionsID": self.reactionsID,
            "reactions_type": self.reactions_type,
            "userID": self.userID,
            # "views_viewsID": self.views_viewsID,
            # "views_storie_storieID": self.views_storie_storieID,
            "user_info": {
                "userID": self.user_account.userID,
                "nickname": self.user_account.nickname,
                "follower_amount": self.user_account.follower_amount,
                "photo_amount": self.user_account.photo_amount,
                "storie_amount": self.user_account.storie_amount,
            }
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reactions:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Reactions(
            reactions_type=dto_dict.get("reactions_type"),
            userID=dto_dict.get("userID"),
            # views_viewsID=dto_dict.get("views_viewsID"),
            # views_storie_storieID=dto_dict.get("views_storie_storieID"),
        )
        return obj
