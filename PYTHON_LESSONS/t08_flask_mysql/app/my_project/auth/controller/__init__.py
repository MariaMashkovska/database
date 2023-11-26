"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.user_info_controller import UserInfoController
from .orders.user_account_controller import UserAccountController
from .orders.follower_controller import FollowerController
from .orders.statistic_controller import StatisticController
from .orders.storie_controller import StorieController
from .orders.media_controller import MediaController


user_info_controller = UserInfoController()
user_account_controller = UserAccountController()
follower_controller = FollowerController()
statistic_controller = StatisticController()
storie_controller = StorieController()
media_controller = MediaController()
