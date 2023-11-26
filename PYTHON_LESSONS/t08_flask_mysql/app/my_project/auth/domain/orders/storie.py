from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class Storie(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "storie"

    storieID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    views_amount = db.Column(db.Integer)
    user_account_userID = db.Column(db.Integer, db.ForeignKey('user_account.userID'), primary_key=True)

    storie_info = db.relationship('UserAccount', foreign_keys=[user_account_userID], backref='storie_detail')

    def __repr__(self) -> str:
        return f"Storie(storieID={self.storieID}, views_amount={self.views_amount}, user_account_userID={self.user_account_userID})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "storieID": self.storieID,
            "views_amount": self.views_amount,
            "user_account_userID": self.user_account_userID,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Storie:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Storie(
            views_amount=dto_dict.get("views_amount"),
            user_account_userID=dto_dict.get("user_account_userID"),
        )
        return obj
