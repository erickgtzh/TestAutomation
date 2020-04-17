import datetime
import pytz
from models.utils import read_serial, wait
from suite import dial_adb, dial_adb_uia, change_wifi_status

script_manager = [change_wifi_status]


def suite_execution():
    for suite in script_manager:
        try:
            serial = suite.read_serial()
        except Exception as ex:
            print('Error: ' + ex)
            pass

        start_ts_pst = suite.get_time()
        print 'test start:  {}'.format(start_ts_pst)
        print 'serial    :  {}'.format(serial)

        try:
            print suite.suite_info()
            suite.suite_methods()
            wait()

        except Exception as ex:
            print(ex)
            pass
        finally:
            stop_ts_pst = suite.get_time()

            print "-------------RESULTS-------------"  # results of out scripts
            print 'test start: {0}\ntest end: {1}'.format(start_ts_pst, stop_ts_pst)  # our script end time parsed


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    Where is managed what methods are going to run
    """
    suite_execution()
