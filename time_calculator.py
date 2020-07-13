def add_time(start, duration, weekday=None):
    hour_array = start.split()
    am_pm = hour_array[1]
    start_hours = int(hour_array[0].split(":")[0])
    start_mins = int(hour_array[0].split(":")[1])
    duration_hours = int(duration.split(":")[0])
    duration_mins = int(duration.split(":")[1])
    days_message = ""
    week = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }

    num_days = int(duration_hours/24)
    additional_hours = duration_hours%24
    additional_hours += int(duration_mins/60)
    additional_mins = duration_mins%60

    end_hours = start_hours + additional_hours
    end_mins = start_mins + additional_mins

    if(end_mins >= 60):
        end_hours += 1
        end_mins -= 60

    if(end_hours >= 12):
        if(am_pm == 'PM'):
            num_days += 1
            am_pm = 'AM'
        else:
            am_pm = 'PM'
        if(end_hours > 12):
            end_hours -= 12

    end_mins = format(end_mins, '02')
    end_hours = str(end_hours)

    if(num_days == 1):
        days_message = " (next day)"
    if(num_days > 1):
        days_message = " ("+str(num_days)+" days later)"

    if(weekday != None):
        if(weekday.lower() in week):
            weekday_num = week[weekday.lower()]
            key_list = list(week.keys())
            val_list = list(week.values())
            add_weekday = num_days%7
            if((weekday_num+add_weekday) > 7):
                end_weekday = key_list[val_list.index(weekday_num+add_weekday-7)]
            else:
                end_weekday = key_list[val_list.index(weekday_num+add_weekday)]
            new_time = end_hours+":"+end_mins+" "+am_pm+", "+end_weekday.capitalize()+days_message
            return new_time
        else:
            return "Error: wrong day name"

    new_time = str(end_hours)+":"+end_mins+" "+am_pm+days_message

    return new_time
