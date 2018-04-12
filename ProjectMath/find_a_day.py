__author__ = 'Robert W. Curtiss'
__project__ = 'NASFAN'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: Find A Day
    File: find_a_day
    Created: Apr, 08, 2018

    Description:

===================================================
"""


class FindADay(object):
    """
    Year = Year
    Month = (1 Jan to 12 Dec)
    WeekDay = (0 Sun to 6 Sat)

    """
    t = (5, 1, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2)
    S = 0
    week_days = ['Sunday',
                 'Monday',
                 'Tuesday',
                 'Wednesday',
                 'Thursday',
                 'Friday',
                 'Saturday']

    def __init__(self, year, month, week_day):
        """Check for Feb, leap year problem"""
        if month <= 2:
            self.year = year - 1
        else:
            self.year = year
        S = ((int(self.year / 100)) - int((self.year / 400))) - 2

        self.week_day = int((self.year + self.year / 4 - S + self.t[month - 1] + week_day) % 7)

    def __str__(self):
        return "{} {}".format(self.year, self.week_days[self.week_day])

#change the range of years you want
for i in range(2018, 2051):
    # change the month abd day below to get
    spd = FindADay(i, 3, 17)
    # if spd.week_day == 6:
    #     print(spd)
