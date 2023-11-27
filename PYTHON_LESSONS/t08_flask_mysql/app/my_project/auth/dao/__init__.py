"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.user_info_dao import UserInfoDAO
from .orders.user_account_dao import UserAccountDAO
from .orders.follower_dao import FollowerDAO
from .orders.statistic_dao import StatisticDAO
from .orders.storie_dao import StorieDAO
from .orders.media_dao import MediaDAO
from .orders.views_dao import ViewsDAO
from .orders.reactions_dao import ReactionsDAO
from .orders.report_dao import ReportDAO


user_info_dao = UserInfoDAO()
user_account_dao = UserAccountDAO()
follower_dao = FollowerDAO()
statistic_dao = StatisticDAO()
storie_dao = StorieDAO()
media_dao = MediaDAO()
views_dao = ViewsDAO()
reactions_dao = ReactionsDAO()
report_dao = ReportDAO()