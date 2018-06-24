def nextDay(year, month, day):
    #Returns the year, month, day of the next day
    #Simple version: assume every month has 30 days
    if (day>=30):
        dayNext = 1
        if (month==12):
            monthNext = 1
            yearNext = year+1
            return (yearNext, monthNext, dayNext)            
        else:
            monthNext = month+1
            yearNext = year
            return (yearNext, monthNext, dayNext)
    elif (day<30):
        daysNext = day+1
        monthNext = month
        yearNext = year
        return (yearNext, monthNext, dayNext)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    #Returns true if date1 is before date2. Otherwise, return False.
    if year1<year2:
        return True
    elif year1==year2:
        if month1<month2:
            return True
        if month1==month2:
            return day1<day2
    return False 


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    # while (this is true):
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, mont1)
        days += 1
    return days
    assert not dateIsBefore(year1, month1, day1, year2, month2, day2) == False


def test():
    #test assuming months are of 30 days
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nestDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1) 
    print 'test is over!'



test()
