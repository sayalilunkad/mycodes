#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import datetime
from datetime import date

# 1. Use the datetimemodule to write a program that gets the current date
# and prints the day of the week.
# 2. Write a program that takes a birthday as input and prints the user’s
# age and the number of days, hours, minutes and seconds until their next
# birthday.
# 3. For two people born on different days, there is a day when one is twice
# as old as the other.That’s their Double Day. Write a program that takes two
# birthdays and computes their Double Day.
# 4. For a little more challenge, write the more general version that computes
# the day when oneperson is n times older than the other


def curr_date():
    current_date = datetime.date.today().isoformat()
    return current_date


def day_of_week():
    dow = {'0': 'Sunday', '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday'}
    week_count = datetime.datetime.today().weekday()
    weekday = dow[str(week_count)]
    return weekday


def birthday(dob):
    today = curr_date()
    dob = dob.split('-')
    today = today.split('-')
    dob = [int(x) for x in dob]
    today = [int(x) for x in today]
    age = today[0]-dob[0]
    dob_next = dob
    dob_next = [int(x) for x in dob_next]
    dob_next[0] = today[0] + 1
    diff = datetime.datetime(dob_next[0], dob_next[1], dob_next[2]) - datetime.datetime(today[0], today[1], today[2])
    nos = diff.seconds + diff.days * 86400
    nom = diff.seconds + diff.days * 86400/60
    noh = diff.seconds + diff.days * 86400/3600
    nod = noh / 24
    return [age, dob_next, nos, noh, nom, nod]


def double_day(dob1, dob2):
    dob1 = dob1.split('-')
    dob2 = dob2.split('-')
    dob1 = [int(x) for x in dob1]
    dob2 = [int(x) for x in dob2]
    dob1 = date(dob1[0], dob1[1], dob1[2])
    dob2 = date(dob2[0], dob2[1], dob2[2])
    assert dob1 > dob2
    delta = dob1-dob2
    d_day = dob1 + delta
    return d_day



if __name__ == '__main__':
    print curr_date()
    print day_of_week()
    b1 = birthday('1992-07-20')
    print "Age: %s" % b1[0]
    print "Next Birthday: %s" % b1[1]
    print "Number of days left: %s" % b1[5]
    print "Number of seconds left: %s secs" % b1[2]
    print "Number of minutes left: %s mins" % b1[4]
    print "Number of hours left: %s hours" % b1[3]
    print "Double day is: %s" % double_day('2006-12-26', '2003-10-11')

