#!/usr/bin/python

"""
by Erick Gtz
04/09/2020
Second Script: release 1.2
"""
from subprocess import check_call, check_output
import time
import datetime
from uiautomator import Device
import pytz


# ---------------------------------------------------------

def read_serial():
    """ Method that reads the serial of the first android device detected by adb """
    output = check_output(['adb', 'devices'])  # check the adb list of available devices
    lines = output.splitlines()
    first_dev = lines[1].split()[0]  # just use the first available device
    print ("Device detected = {}".format(first_dev))
    return first_dev


def get_number():
    """ Method that retrieves and return the user input of the number to call """
    print("Please, enter number to call:")
    return str(input())


def call_number(serial):
    """ Method that retrieves all the processes to make the call """
    number = get_number()  # get number to call

    # Wake up our cellphone
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])

    # Go to home page
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(0.01)

    # Start initial menu
    d(text='Apps', packageName='com.huawei.android.launcher').click()
    time.sleep(0.01)

    # Search for app allow scroll search to get the child called "Phone"
    d(className="android.support.v7.widget.RecyclerView", resourceId="com.huawei.android.launcher:id/apps_list_view") \
        .child_by_text(
        "Phone",
        allow_scroll_search=True,
        className="android.widget.TextView"
    ).click()
    time.sleep(0.01)

    # Enter (+) character
    d(text='0', packageName='com.android.contacts').long_click()
    time.sleep(0.01)

    # Enter 5 number
    d(text='5', packageName='com.android.contacts').click()
    time.sleep(0.01)

    # Enter 2 number
    d(text='2', packageName='com.android.contacts').click()
    time.sleep(0.01)

    # Iterate and put down every digit of the number to call
    for n in number:
        d(text=n).set_text(n)
        time.sleep(0.01)

    # Search and click in phone icon
    d(className="android.widget.LinearLayout",
      resourceId="com.android.contacts:id/dialpadAdditionalButtonsWithIpCall") \
        .child_by_text(
        "",
        className="android.widget.ImageButton"
    ).click()
    time.sleep(0.01)

    # Go back to home after #time seconds
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(10)  # time to wait

    return


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """Where our code runs"""
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
        print("Script Call by UiAutomator - Mode: On---------")
        call_number(first_serial)
        time.sleep(2)
    except Exception as ex:
        print(ex)
    finally:
        stop_ts = datetime.datetime.now()  # actual time when our script finished to know when it overs
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("-------------RESULTS  -------------------------------------------")  # results of out scripts
        print('test start:  %s' % start_ts_pst)  # our script start time parsed
        print('test end  :  %s' % stop_ts_pst)  # our script end time parsed
