##############################################################################
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
            
            #Because you don't enter a day of the week, the date you enter is set to the first day on this list
            #If you want to start your game on any day other than Monday, you'll need to change the order so that day is first
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            self.month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                               'August', 'September', 'October', 'November', 'December']
            self.days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
           
            self.mooncycle = 29
            self.newmoonday = 1
            
            self.future_daycount = 0
            self.future_days_count = 0
            self.future_date = 0
            self._futuremonth = 0
            self.future_year = 0
            self.future_leapyear = 0
            
            self.past_daycount = 0
            self.past_days_count = 0
            self.past_date = 0
            self._pastmonth = 0
            self.past_year = 0
            self.past_leapyear = 0
            
            self.dates_diff = 0
           
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
        def future_weekday(self):
            '''Returns the name of the current day according to daycount.'''
            daylistidx = self.future_daycount % len(self.days)
            return self.days[daylistidx]
            
        @property   
        def past_weekday(self):
            '''Returns the name of the current day according to daycount.'''
            daylistidx = self.past_daycount % len(self.days)
            return self.days[daylistidx]
           
        @property
        def month_number(self):
            return self._month + 1
            
        @property
        def future_month_number(self):
            return self._futuremonth + 1
        
        @property
        def past_month_number(self):
            return self._pastmonth + 1
           
        @property
        def month(self):
            return self.month_names[self._month]
            
        @property
        def future_month(self):
            return self.month_names[self._futuremonth]
        
        @property
        def past_month(self):
            return self.month_names[self._pastmonth]
           
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


        #This function allows you to check the date X days in the future without changing the current date. 
        def getfuture(self, days=1):
            """
            Next day counter.
            Now supports skipping.
            """
            self.future_daycount = self.daycount_from_gamestart
            self.future_days_count = self.days_count
            self.future_daycount += days
            self.future_date = self.day
            self._futuremonth = self._month
            self.future_year = self.year
            self.future_leapyear = self.leapyear
            while days:
                self.future_date += 1
                days -= 1
                if self.future_leapyear == self.future_year and self._futuremonth == 1:
                    if self.future_date > self.future_days_count[self._futuremonth] + 1:
                        self._futuremonth += 1
                        self.future_date = 1
                        self.future_leapyear += 4
                elif self.future_date > self.future_days_count[self._futuremonth]:
                    self._futuremonth += 1
                    self.future_date = 1
                    if self._futuremonth > 11:
                        self._futuremonth = 0
                        self.future_year += 1
                        
        
        #This function allows you to check the date X days in the past without changing the current date. 
        def getpast(self, days=1):
            """
            Next day counter.
            Now supports skipping.
            """
            self.past_daycount = self.daycount_from_gamestart
            self.past_days_count = self.days_count
            self.past_daycount -= days
            self.past_date = self.day
            self._pastmonth = self._month
            self.past_year = self.year
            self.past_leapyear = self.leapyear - 4
            while days:
                self.past_date -= 1
                days -= 1
                if self.past_leapyear == self.past_year and self._pastmonth == 2:
                    if self.past_date < 1:
                        self._pastmonth -= 1
                        self.past_date = self.past_days_count[self._pastmonth] + 1
                        self.past_leapyear -= 4
                elif self.past_date < 1:
                    if self._pastmonth == 0:
                        self._pastmonth = 11
                        self.past_date = self.past_days_count[self._pastmonth]
                        self.past_year -= 1
                    else:
                        self._pastmonth -= 1
                        self.past_date = self.past_days_count[self._pastmonth]
        
        
        #This function tells you how many days have passed between two dates. 
        #Calculates using daycount/future_daycount/past_daycount
        def between_dates(self, cnt1=0, cnt2=0):
            self.dates_diff = abs(cnt1) + abs(cnt2)
        
        #Eventually, I want to use this in order to check how long something has been fermenting, soaking, etc.
        #I would need a new function, possibly in the inventory, which stores the date when the item was obtained.
        #Then, when you check on the item in the root cellar, it uses between_dates to tell you how long it's been there. 
        #If the dates_diff is > a specific number, then the item would change into a different item. (Ex. juice into wine.)
                       
           
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
        
screen future_testing:
    vbox:
        xminimum 500
        xfill True
        spacing 10
        align(0.5, 0.1)
        text ("Future Date: %d"%calendar.future_date)
        text ("Future Weekday: %s"%calendar.future_weekday)
        text ("Future Month: %s"%calendar.future_month)
        text ("Future Year: %d"%calendar.future_year)
        
screen past_testing:
    vbox:
        xminimum 500
        xfill True
        spacing 10
        align(0.5, 0.1)
        text ("Day Count: %d"%calendar.past_daycount)
        text ("Past Date: %d"%calendar.past_date)
        text ("Past Weekday: %s"%calendar.past_weekday)
        text ("Past Month: %s"%calendar.past_month)
        text ("Past Year: %d"%calendar.past_year)
        
screen between_testing:
    vbox:
        xminimum 500
        xfill True
        spacing 10
        align(0.5, 0.1)
        text ("Days Count: %d"%calendar.daycount_from_gamestart)
        text ("Future Days Count: %d"%calendar.past_daycount)
        text ("Past Days Count: %d"%calendar.past_daycount)
        text ("Difference: %d"%calendar.dates_diff)
        
screen calendar:
    
    tag menu
    
    python:
        cal_base = "cal/cal base.png"
        if calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])
        
    add cal_base xpos 0 ypos 0
    add month_img xpos 0 ypos 0
    add day_img xpos 0 ypos 0
    add dotw_img xpos 0 ypos 0
    add moon_img xpos 0 ypos 0
    add time_img xpos 0 ypos 0
    
    
