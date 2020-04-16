#!/usr/bin/python

"""
by Erick Gtz
04/09/2020
Fourth Script: release 1.4
Script version: 1.1 (04/11/20)
"""
from subprocess import check_call, check_output
import time
import datetime
from uiautomator import Device
import pytz


# ---------------------------------------------------------

def read_serial():
    """
    Method that reads the serial of the first android device detected by adb
    :return: serial of detected device
    """
    output = check_output(['adb', 'devices'])  # check the adb list of available devices
    lines = output.splitlines()
    first_dev = lines[1].split()[0]  # just use the first available device
    print ("Device detected = {}".format(first_dev))
    return first_dev


def open_settings(serial):
    """
    Method that retrieves all the processes to open settings menu
    :return: when the function is completed
    """
    # Wake up our cellphone
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])

    # Go to home page
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(0.01)

    # Start initial menu
    d(text='Apps', packageName='com.huawei.android.launcher').click()
    time.sleep(0.01)

    # Search for app allow scroll search to get the child called "Settings"
    d(className="android.support.v7.widget.RecyclerView", resourceId="com.huawei.android.launcher:id/apps_list_view") \
        .child_by_text(
        "Settings",
        allow_scroll_search=True,
        className="android.widget.TextView"
    ).click()
    time.sleep(0.01)

    return


def change_wifi_status(serial):
    """
    Method that retrieves all the processes to change our wifi status
    :return: when the function is completed
    """
    # Click on search bar and set in this text "wireless"
    d(text='Search').set_text("wireless")
    time.sleep(0.01)

    # Get to the first value that we found that contains Wi-Fi
    d(text='Wi-Fi', className='android.widget.TextView') \
        .click()
    time.sleep(0.01)

    # Change the status of our wifi just toggling
    d(text='', className='android.widget.Switch') \
        .click()
    time.sleep(0.01)

    # Go back to home after #time seconds
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(5)  # time to wait

    return


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    Where we manage who runs
    """
    try:
        first_serial = read_serial()  # get number serial of our cellphone, it has to be the first in our ~ adb devices
    except Exception as ex:  # Exception when there are no available adb devices
        print('Error: ' + ex)

    start_ts = datetime.datetime.now()  # get the timestamp at the exact moment that start running our test
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))  # format

    print('test start:  %s ' % start_ts_pst)
    print('serial: %s' % first_serial)

    try:
        d = Device(first_serial)
        print("Script Change Wi-Fi Status - Mode: On---------")
        open_settings(first_serial)
        change_wifi_status(first_serial)
        time.sleep(2)
    except Exception as ex:
        print(ex)
    finally:
        stop_ts = datetime.datetime.now()  # actual time when our script finished to know when it overs
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("-------------RESULTS  -------------------------------------------")  # results of out scripts
        print('test start:  %s' % start_ts_pst)  # our script start time parsed
        print('test end  :  %s' % stop_ts_pst)  # our script end time parsed
