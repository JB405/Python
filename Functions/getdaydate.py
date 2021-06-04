from datetime import date
from datetime import timedelta  

def getdaydate (Occurrence = 'Second',DayOfWeek = 'Tuesday',Month: int = date.today().month,Year: int = date.today().year):
    """
    Overivew:
      return the date for occurrence of a day of the week
    Description:
      function returns the date for a giving day of the week and occurrence of giving month and year  
    Parameters:
      Occurrence
        Specifies the occurance of the day of week (First,Second,Thrid,Fourth or last), the default is Second
      DayOfWeek
        Specifies DayOfWeek ( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday )to find the date of default is Tuesda
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
    """
    WeekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    tOccurrence = ("First","Second","Third","Fourth","Last")

    if Occurrence not in tOccurrence:
        print ("Error: {} is not in {}".format(Occurrence,tOccurrence))
        return
    if DayOfWeek not in WeekDays:
        print ("Error: {} is not in {}".format(DayOfWeek,WeekDays))
        return
    if Month not in range(1,12):
        print ("Error: {} is not in range (1 - 12)".format(Month))
        return
    if Year not in range(1000,10000):
        print ("Error: {} is not in range (1000 - 9999)".format(Year))
        return

    vdate = date(Year,Month,1)

    #get first Occurrence of weekday for them month
    while WeekDays[vdate.weekday()]  != DayOfWeek :
        vdate = vdate + timedelta(days=1)  
    
    if Occurrence == 'First' :
        return vdate
    elif Occurrence == 'Second' :
         return vdate + timedelta(days=7)
    elif Occurrence == 'Third' :
         return vdate + timedelta(days=14)
    elif Occurrence == 'Fourth' :
        return vdate + timedelta(days=21)
    elif Occurrence == 'Last' :
        while vdate.month == Month:
            newdate = vdate + timedelta(days=7) 
            if newdate.month != Month :
                return vdate
            vdate =  newdate

if __name__ == '__main__':
  #print ("{} is the date of the Second Tuesday.".format(getdaydate()))