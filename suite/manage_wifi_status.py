import time
import datetime
import pytz
from models.utils import call_adb_number, wait, read_serial, open_app, toggle_wifi_status, get_wifi_status, \
    wait_process_completed

"""
by Erick Gtz
04/15/2020
1.3 & 1.4 script

script version: 1.1 (04/11/20)
script version: 1.2 (04/15/20)
script version: 1.3 (04/17/20)
"""


def suite_info():
    name = 'toggle wifi status'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)
    return info


def suite_methods():
    """
    suite methods that we're going to run
    """
    if not get_wifi_status(1):  # 0 == turn off | 1 == turn on
        open_app('Settings')
        toggle_wifi_status()
    wait_process_completed()


def get_time():
    """
    actual time when our script when we call this method
    :return: actual time
    """
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    return start_ts_pst
