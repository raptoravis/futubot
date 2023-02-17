from datetime import datetime
from datetime import timezone
from datetime import timedelta

from typing import Any
from typing import List
from typing import Dict
from typing import Union
from typing import Optional
from typing import Tuple

import tests.test_utils.test_configs as test_configs

import tests.test_futubot.test_robot as test_robot
import tests.test_futubot.test_stockframe as test_stockframe
import tests.test_futubot.test_accounts as test_accounts
import tests.test_futubot.test_portfolio as test_portfolio
import tests.test_futubot.test_indicators as test_indicators


import tests.test_strategy.test_strategies as test_strategies

#######################################################################

test_configs.test_parse_config('demo/configs/futubot_config_demo.py')

test_robot.test_create_portfolio()
test_robot.test_create_stockframe()
test_robot.test_get_latest_bar()
test_robot.test_execute_signals()

test_stockframe.test_create_frame()
test_stockframe.test_add_rows()

test_accounts.test_get_max_power()

test_portfolio.test_calculate_portfolio_metrics()

test_indicators.test_bollinger_bands()


test_strategies.test_bollinger_bands_strategy()


class Trade():

    """
    Object Type:
    ----
    `pyrobot.Trade`

    Overview:
    ----
    Reprsents the Trade Object which is used to create new trades,
    add customizations to them, and easily modify existing content.
    """

    def __init__(self):
        """Initalizes a new order."""

        self.order = {}
        self.trade_id = ""
        self.order_id = ""
        self.account = ""
        self.order_status = "NOT_PLACED"
    
    def to_dict(self) -> dict:

        # Initialize the Dict.
        obj_dict = {
            "__class___": self.__class__.__name__,
            "__module___": self.__module__
        }

        # Add the Object.
        obj_dict.update(self.__dict__)

        return obj_dict

    def new_trade(self, trade_id: str, order_type: str, side: str, enter_or_exit: str, price: float = 0.00, stop_limit_price: float = 0.00) -> dict:
        return self.order