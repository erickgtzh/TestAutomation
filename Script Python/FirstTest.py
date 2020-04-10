#!/usr/bin/python

"""
by Erick Gtz
04/09/2020
First Script: release 1.1
"""
from subprocess import check_output
import time
import datetime
import pytz


# ---------------------------------------------------------

def read_serial():
    """ Method that reads the serial of the first android device detected by adb """
    output = check_output(['adb', 'devices'])  # check the adb list of available devices
    lines = output.splitlines()
    first_dev = lines[1].split()[0]  # just use the first available device
    print ("Device detected = {}".format(first_dev))
    return first_dev


def get_command(number):
    """ Method that returns the adb command used to call cellphone and to the concatenation with the number to call """
    return check_output(['adb', 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:' + number])


def get_number():
    """ Method that retrieves the user input of the number to call """
    print("Please, enter number to call:")
    return input()


def call_number():
    """ Method that retrieves the methods that allow us to do the call and run them in the correct order to make the
    call """
    number = str(get_number())
    get_command(number)


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """Where our code runs"""
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
