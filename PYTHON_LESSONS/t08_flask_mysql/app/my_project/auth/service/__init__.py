"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.user_info_service import UserInfoService
from .orders.user_account_service import UserAccountService
from .orders.follower_service import FollowerService
from .orders.statistic_service import StatisticService
from .orders.storie_service import StorieService
from .orders.media_service import MediaService
from .orders.views_service import ViewsService
from .orders.reactions_service import ReactionsService
from .orders.report_service import ReportService


user_info_service = UserInfoService()
user_account_service = UserAccountService()
follower_service = FollowerService()
statistic_service = StatisticService()
storie_service = StorieService()
media_service = MediaService()
views_service = ViewsService()
reactions_service = ReactionsService()
report_service = ReportService()
