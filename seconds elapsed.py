def check_input(hour, minute, day, month, year):
    try:
        hour, minute, day, month, year = int(hour), int(minute), int(day), int(month), int(year)
    except Exception:
        return False
    isleap_year = False
    if year%4==0:
        if year%100!=0:isleap_year = True
        elif year%400==0:isleap_year = True
    
    if hour<0 or hour>23 or minute<0 or minute>59 or day<0 or day>31 or month<0 or month>12 or year<0 or year>3000 or (month in (4,6,9,11) and day==31) or(month==2 and ((day>28 and not isleap_year) or (day>29 and isleap_year))):
        return False
    return True

def Start(message = None):
    print("\n*********************************************")
    if message:print(f"{message}\n*********************************************")

    hour = [0,0]
    minute = [0,0]
    day = [0,0]
    month = [0,0]
    year = [0,0]
    isleap_year = [False, False]

    for pos in range(2):
        var = ['Start', 'End']
        hour[pos], minute[pos] = input(f"Enter {var[pos]} Time seperated by ':' ->").split(':')
        day[pos], month[pos], year[pos] = input(f"Enter {var[pos]} Date seperated by '/' ->").split('/')
        
        if not check_input(hour[pos], minute[pos], day[pos], month[pos], year[pos]):
            Start("Invalid Input")
            return
        else:hour[pos], minute[pos], day[pos], month[pos], year[pos] = int(hour[pos]), int(minute[pos]), int(day[pos]), int(month[pos]), int(year[pos])

        if year[pos]%4==0:
            if year[pos]%100!=0:isleap_year[pos] = True
            elif year[pos]%400==0:isleap_year[pos] = True

    days = [day[0],day[1]]
    for pos in range(2):
        for val in range(1,month[pos]):
            if val in (4,6,9,11):
                days[pos]+=30
            elif val in (1,3,5,7,8,10,12):
                days[pos]+=31
            elif val==2:
                if isleap_year[pos]:days[pos]+=29
                else:days[pos]+=28

    years = year[1] - year[0]
    year_days = 0
    for val in range(1,years+1):
        this_year = val + year[0] - 1
        if this_year%4==0:
            if this_year%100!=0:year_days+=366
            elif this_year%400==0:year_days+=366
        else:year_days+=365

    total_days = year_days+days[1]-days[0]
    total_minutes = (total_days)*24*60 + (minute[1] + hour[1]*60) - (minute[0]+ hour[0]*60)
    total_seconds = total_minutes*60

    print(f"Seconds -> {total_seconds}")

    if input("Again?('yes'->y, 'no'->Any)")=='y':Start()

Start()
    
