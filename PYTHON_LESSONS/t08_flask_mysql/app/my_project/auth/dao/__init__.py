"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.user_info_dao import UserInfoDAO
from .orders.user_account_dao import UserAccountDAO
from .orders.follower_dao import FollowerDAO


user_info_dao = UserInfoDAO()
user_account_dao = UserAccountDAO()
follower_dao = FollowerDAO()
