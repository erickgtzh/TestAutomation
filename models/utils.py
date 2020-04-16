import re
import time
from subprocess import check_output, check_call

from uiautomator import Device

package_name = 'com.huawei.android.launcher'


def read_serial(position=1):
    """
    Method that reads the serial of the first android device detected by adb on the send position ::default = 1
    :return: serial of detected device
    """
    output = check_output(['adb', 'devices'])  # check the adb list of available devices
    lines = output.splitlines()
    detected_device = lines[position].split()[0]  # just use the first available device
    return detected_device


def get_serial_and_device(serial=read_serial()):
    return [serial, Device(serial)]


def open_app(app_name):
    """
    Method that retrieves all the processes to open menu
    :return: when the process ends
    """
    serial, d = get_serial_and_device()
    # Wake up our cellphone
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])

    # Go to home page
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    wait()

    # Start initial menu
    d(text='Apps', packageName=package_name).click()
    wait()

    # Search for app allow scroll search to get the child called #app_name parameter
    d(className="android.support.v7.widget.RecyclerView", resourceId="{0}:id/apps_list_view".format(package_name)) \
        .child_by_text(
        app_name,
        allow_scroll_search=True,
        className="android.widget.TextView"
    ).click()
    wait()

    return


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


def call_adb_number():
    """
    Method that retrieves the methods that allow us to do the call and run them in the correct order to make the call
    and append the number to commit the adb command
    """
    serial, d = get_serial_and_device()
    # Ask number to call
    number = get_number()
    if validate_number(number):
        check_output(['adb', 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:' + number])
    d.wait.update()


def get_number():
    """
    Method that retrieves the user input of the number to call
    :return: a string variable of the number to call
    """
    serial, d = get_serial_and_device()
    number = raw_input("Please, enter number to call: ")
    if validate_number(number):
        print 'calling: {}'.format(number)
        return number


def clear_phone_display(d):
    d(text='1').set_text('1')
    wait()
    # long click backspace to delete all on display
    d(className="android.widget.LinearLayout", resourceId="com.android.contacts:id/deleteButton") \
        .child_by_text("", className="android.widget.ImageView") \
        .long_click()


def call_number():
    """
    Method that retrieves all the processes to ask a number and call it
    :return: when the process ends
    """
    serial, d = get_serial_and_device()
    # clear display
    clear_phone_display(d)

    # Iterate and put down every digit of the number to call
    for i in str(get_number()):
        d(text=i).set_text(i)
        wait()

    # Search and click in phone icon to call
    d(className="android.widget.LinearLayout",
      resourceId="com.android.contacts:id/dialpadAdditionalButtonsWithIpCall") \
        .child_by_text(
        "",
        className="android.widget.ImageButton"
    ).click()
    d.wait.update()
    d.press.back()
    return


def change_wifi_status():
    """
    Method that retrieves all the processes to change our wifi status
    :return: when the function is completed
    """
    serial, d = get_serial_and_device()
    # Click on search bar and set in this text "wireless"
    d(text='Search').set_text("wireless")
    wait()

    # Get to the first value that we found that contains Wi-Fi
    d(text='Wi-Fi', className='android.widget.TextView') \
        .click()
    wait()

    # Change the status of our wifi just toggling
    d(text='', className='android.widget.Switch') \
        .click()
    wait()

    d.wait.update()
    d.press.back()
    d.press.back()
    d.press.home()
    return


def wait(sleep_time=0.01):
    time.sleep(sleep_time)
