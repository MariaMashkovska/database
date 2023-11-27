from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Report(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "report"

    reportID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(3663), nullable=False)

    views = db.relationship('Views', backref='report_info')

    def __repr__(self) -> str:
        return f"Report(reportID={self.reportID}, text={self.text})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "reportID": self.reportID,
            "text": self.text
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Report:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Report(
            text=dto_dict.get("text"),
        )
        return obj
