"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.user_info_service import UserInfoService
from .orders.user_account_service import UserAccountService
from .orders.follower_service import FollowerService


user_info_service = UserInfoService()
user_account_service = UserAccountService()
follower_service = FollowerService()

