#!/usr/bin/python

"""
by Erick Gtz
04/09/2020
First Script: release 1.1
Script version: 1.1 (04/11/20)
"""
import re
from subprocess import check_output
import time
import datetime
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


def get_number():
    """
    Method that retrieves the user input of the number to call
    :return: a string variable of the number to call
    """
    return raw_input("Please, enter a number to call: ")


def validate_number(number):
    """
    Method that validate the length and regex of the number (only: digits and characters)
    :return: validation of the number entered
    """
    rule = re.match(r'^([\s\d\+\*\+\#]+)$', number)
    if 15 > len(number) > 2 and rule:
        return True
    print "Please, enter a valid number, try again..."
    call_number()


def call_number():
    """
    Method that retrieves the methods that allow us to do the call and run them in the correct order to make the call
    and append the number to commit the adb command
    """
    # Ask number to call
    number = get_number()
    if validate_number(number):
        check_output(['adb', 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:' + number])


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    Where we manage who runs
    """
    try:
        first_serial = read_serial()  # get number serial of our cellphone, it has to be the first in our ~ adb devices
    except Exception as ex:  # Exception when there are no available adb devices
        print('Error: ' + ex)

    start_ts = datetime.datetime.now()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    print('test start:  %s ' % start_ts_pst)  # get the control of when our script starts
    print('serial: %s' % first_serial)

    try:
        print("Script Call by Adb - Mode: On---------")
        call_number()
        time.sleep(2)

    except Exception as ex:
        print(ex)
    finally:

        stop_ts = datetime.datetime.now()  # actual time when our script finished to know when it overs
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("-------------RESULTS  -------------------------------------------")  # results of out scripts
        print('test start:  %s' % start_ts_pst)  # our script start time parsed
        print('test end  :  %s' % stop_ts_pst)  # our script end time parsed
