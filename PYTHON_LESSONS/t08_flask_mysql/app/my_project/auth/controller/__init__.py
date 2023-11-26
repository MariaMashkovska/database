"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.user_info_controller import UserInfoController
from .orders.user_account_controller import UserAccountController
from .orders.follower_controller import FollowerController


user_info_controller = UserInfoController()
user_account_controller = UserAccountController()
follower_controller = FollowerController()
