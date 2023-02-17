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