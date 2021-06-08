from datetime import date
from datetime import timedelta


def getdaydate(Occurrence: str = 'Second', DayOfWeek: str = 'Tuesday', Month: int = date.today().month, Year: int = date.today().year):
    """
    Overivew:
        return the date for occurrence of a day of the week
    Description:
        function returns the date for a giving day of the week and occurrence of giving month and year  
    Parameters:
        Occurrence
            Specifies the occurance of the day of week (First,Second,Thrid,Fourth or last), the default is Second
        DayOfWeek
            Specifies DayOfWeek ( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday )to find the date of default is Tuesday
        Month
            Specifies the month number to find the day of, default is the current month
        Year
            Specifies the yeah of what month and day to return the date, default is current year
    Example:
          getdaydate() # return date for second Tuesday for this month
          getdaydate('Last','Monday') # Return date for Last Monday for this month
          getdaydate(Year = 2025,Occurrence='First',DayOfWeek= 'Monday',Month = 12) # Return date for fist Monday for December 2025

          # Return date for second Tuesday of every month for this year.     
          Months = range(1,12)
          for n in Months:
              getdaydate(Month=n)
    Link:
        https://github.com/JB405/Python
    """
    WeekDays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")
    tOccurrence = ("First", "Second", "Third", "Fourth", "Last")

    if Occurrence not in tOccurrence:
        raise TypeError(f"Error: {Occurrence} is not in {tOccurrence}")
    if DayOfWeek not in WeekDays:
        raise TypeError(f"Error: {DayOfWeek} is not in {WeekDays}")
    if Month not in range(1, 12):
        raise TypeError(f"Error: {Month} is not in range (1 - 12)")
    if Year not in range(1000, 10000):
        raise TypeError(f"Error: {Year} is not in range  (1000 - 9999)")

    StartDate = date(Year, Month, 1)

    # get first Occurrence of weekday for them month
    while WeekDays[StartDate.weekday()] != DayOfWeek:
        StartDate = StartDate + timedelta(days=1)

    if Occurrence == 'First':
        return StartDate
    elif Occurrence == 'Second':
        return StartDate + timedelta(days=7)
    elif Occurrence == 'Third':
        return StartDate + timedelta(days=14)
    elif Occurrence == 'Fourth':
        return StartDate + timedelta(days=21)
    elif Occurrence == 'Last':
        while StartDate.month == Month:
            newdate = StartDate + timedelta(days=7)
            if newdate.month != Month:
                return StartDate
            StartDate = newdate


if __name__ == '__main__':    
    print("{} is the date of the Second Tuesday.".format(getdaydate()))