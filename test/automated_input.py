import datetime
import io

import pytz
from models.utils import read_serial, wait
from suite import call_adb, call_uia, manage_wifi_status

local_number = io.StringIO(u'4499113728')

national_number = io.StringIO(u'3957850261')


def test_local_number(monkeypatch):
    """
    Automated method using pytest for local calls and let us to run it
    without input by the user, it's introduced by this library.
    :param monkeypatch:
    :return: the result of the suite
    """
    monkeypatch.setattr('sys.stdin', local_number)
    print call_uia.suite_methods()


def test_national_number(monkeypatch):
    """
    Automated method using pytest for national calls and let us to run it
    without input by the user, it's introduced by this library.
    :param monkeypatch:
    :return: the result of the suite
    """
    monkeypatch.setattr('sys.stdin', national_number)
    print call_uia.suite_methods()


def test_wifi_manager():
    """
    Automated method using for change wifi status
    :param monkeypatch:
    :return: the result of the suite
    """
    print manage_wifi_status.suite_methods()


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    """
    Where is managed what methods are going to run
    """
    test_local_number()
    test_national_number()
    test_wifi_manager()