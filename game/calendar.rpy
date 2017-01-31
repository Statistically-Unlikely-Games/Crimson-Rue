﻿##############################################################################
# Calendar
#
# Keeps track of the day, month, year, leap year, and lunar calendar.
# Thanks to xela from the lemmasoft forums!

init python:
    class Calendar(object):
        '''Provides time-related information.
        Cheers to Rudi for mooncalendar calculations.
        '''
        def __init__(self, day=1, oldday = 0, month=1, oldmonth=0, year=1, oldyear=0, leapyear=False):
            """
            Expects day/month/year as they are numbered in normal calender.
            If you wish to add leapyear, specify a number of the first Leap year to come.
            """
            self.day = day
            self.oldday = oldday
            self._month = month - 1
            self.oldmonth = oldmonth
            self.year = year
            self.oldyear = oldyear
            if not leapyear:
                self.leapyear = self.year + 4
            else:   
                self.leapyear = leapyear
           
            self.daycount_from_gamestart = 0
           
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            self.month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                               'August', 'September', 'October', 'November', 'December']
            self.days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
           
            self.mooncycle = 29
            self.newmoonday = 1
           
        @property   
        def game_day(self):
            """
            Returns amount of days player has spent in game.
            Counts first day as day 1.
            """
            return self.daycount_from_gamestart + 1
       
        @property   
        def game_week(self):
            '''Returns the number of weeks, starting at 1 for the first week.
            '''
            weekidx = self.daycount_from_gamestart / len(self.days)
            return weekidx + 1

        @property   
        def weekday(self):
            '''Returns the name of the current day according to daycount.'''
            daylistidx = self.daycount_from_gamestart % len(self.days)
            return self.days[daylistidx]
           
        @property
        def month_number(self):
            return self._month + 1
           
        @property
        def month(self):
            return self.month_names[self._month]
           
        @property   
        def lunarprogress(self):
            '''Returns the progress in the lunar cycle since new moon as percentage.
            '''
            newmoonidx = self.newmoonday - 1
            dayidx = self.daycount_from_gamestart - newmoonidx
            moonidx = dayidx % self.mooncycle
            moondays = moonidx + 1
            percentage = moondays * 100.0 / self.mooncycle
            return int(round(percentage))

        @property   
        def moonphase(self):
            '''Returns the lunar phase according to daycount.

            Phases:
            new moon -> waxing crescent -> first quater -> waxing moon ->
                full moon -> waning moon -> last quarter -> waning crescent -> ...
            '''
            # calculate days into the cycle
            newmoonidx = self.newmoonday - 1
            dayidx = self.daycount_from_gamestart - newmoonidx
            moonidx = dayidx % self.mooncycle
            moondays = moonidx + 1
            # substract the number of named days
            unnamed_days = self.mooncycle - 4
            # calculate the days per quarter
            quarter = unnamed_days / 4.0
            # determine phase
            if moonidx<1:
                phase = "new moon"
            elif moonidx<(quarter+1):
                phase = "waxing crescent"
            elif moonidx<(quarter+2):
                phase = "first quarter"
            elif moonidx<(2*quarter+2):
                phase = "waxing moon"
            elif moonidx<(2*quarter+3):
                phase = "full moon"
            elif moonidx<(3*quarter+3):
                phase = "waning moon"
            elif moonidx<(3*quarter+4):
                phase = "last quarter"
            else:
                phase = "waning crescent"
            return phase
           
        @property
        def last_day_of_the_month(self):
            if self.leapyear == self.year and self._month == 1:
                return self.day == self.days_count[self._month] + 1
            else:   
                return self.day == self.days_count[self._month]
           
        @property       
        def string(self):
            return "(%s) - %s %d %d"%(self.weekday, self.month, self.day, self.year)
       
        def next(self, days=1):
            """
            Next day counter.
            Now supports skipping.
            """
            self.daycount_from_gamestart += days
            while days:
                self.oldday = self.day
                self.day += 1
                days -= 1
                if self.leapyear == self.year and self._month == 1:
                    if self.day > self.days_count[self._month] + 1:
                        self.oldmonth = self.month
                        self._month += 1
                        self.day = 1
                        self.leapyear += 4
                elif self.day > self.days_count[self._month]:
                    self.oldmonth = self.month
                    self._month += 1
                    self.day = 1
                    if self._month > 11:
                        self._month = 0
                        self.oldyear = self.year
                        self.year += 1
                       
           
screen calendar_testing:
    vbox:
        xminimum 500
        xfill True
        spacing 10
        align(0.5, 0.1)
        text ("Day: %d"%calendar.game_day)
        text ("Date: %d"%calendar.day)
        text ("Yesterday's Date: %d"%calendar.oldday)
        text ("Month: %d"%calendar.month_number)
        text ("Last Month: %s"%calendar.oldmonth)
        text ("Year: %d"%calendar.year)
        text ("Last Year: %d"%calendar.oldyear)
        text ("Week: %d"%calendar.game_week)
        text ("Full Date: %s"%calendar.string)
        text ("Next Leap Year: %s"%calendar.leapyear)
        text ("Lunar Progress: %d%%"%calendar.lunarprogress)
        text ("Moon Phase: %s"%calendar.moonphase.capitalize())
        text ("Last day of the month: %s"%calendar.last_day_of_the_month)
        
screen calendar:
    
    tag menu
    
    python:
        if calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])
        
    add month_img xpos 22 ypos 12
    add day_img xpos 22 ypos 12
    add dotw_img xpos 22 ypos 12
    add moon_img align(0.17, 0.02)
    add time_img align(0.02, 0.135)
    
    
