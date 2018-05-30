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

    print("şarj:            %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print("durum:           %s" % ("şarj oluyor" if batt.percent < 100 else "batarya tam dolu"))
        print("fişe takılı:     evet")
    else:
        print("kalan süre:      %s" % secs2hours(batt.secsleft))
        print("durum:           %s" % "şarj olmuyor")
        print("fişe takılı:     hayır")


#if __name__ == '__main__':
#    main()
