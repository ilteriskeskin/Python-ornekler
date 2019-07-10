from __future__ import print_function
import sys

import psutil


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def main():
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")

    print("charge:            %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print("status:           %s" % ("It's charging" if batt.percent < 100 else "battery full"))
        print("plugged in:     yes")
    else:
        print("remaining time:      %s" % secs2hours(batt.secsleft))
        print("status:           %s" % "It's not charging")
        print("plugged in:     No")
