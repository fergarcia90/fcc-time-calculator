def add_time(start, duration):
    hour_array = start.split()
    start_time = hour_array[0]
    am_pm = hour_array[1]
    start_hours = int(hour_array[0].split(":")[0])
    start_mins = int(hour_array[0].split(":")[1])
    duration_hours = int(duration.split(":")[0])
    duration_mins = int(duration.split(":")[1])
    days_message = ""

    if(duration_hours >= 24):
        num_days = int(duration_hours/24)
        additional_hours = duration_hours%24
    else:
        num_days = 0
        additional_hours = duration_hours

    if(duration_mins >= 60):
        additional_hours += duration_mins/60
        additional_mins = duration_mins%60
    else:
        additional_mins = duration_mins

    end_hours = start_hours + additional_hours
    end_mins = start_mins + additional_mins

    if(end_mins >= 60):
        end_hours += 1
        if(end_mins > 60):
            end_mins -= 60
        else:
            end_mins = 0

    if(end_hours >= 12):
        if(am_pm == 'PM'):
            num_days += 1
            am_pm = 'AM'
        else:
            am_pm = 'PM'
        if(end_hours > 12):
            end_hours -= 12

    if(end_mins < 10):
        end_mins = "0"+str(end_mins)

    if(num_days == 1):
        days_message = " (next day)"
    if(num_days > 1):
        days_message = " ("+str(num_days)+" days later)"

    new_time = str(end_hours)+":"+str(end_mins)+" "+am_pm+days_message

    return new_time
