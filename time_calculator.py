def add_time(start, duration):
    hour_array = start.split()
    start_time = hour_array[0]
    am_pm = hour_array[1]
    start_hours = hour_array[0].split(":")[0]
    start_mins = hour_array[0].split(":")[1]
    duration_hours = duration.split(":")[0]
    duration_mins = duration.split(":")[1]

    end_mins = int(start_mins) + int(duration_mins)
    additional_hours = 0
    while(end_mins > 60 ):
        end_mins = end_mins - 60
        additional_hours = additional_hours + 1
    if(end_mins < 10):
        end_mins = "0"+str(end_mins)
    elif(end_mins == 60):
        end_mins = "00"
        additional_hours = additional_hours + 1
    end_hours = int(start_hours) + int(duration_hours) + additional_hours
    num_days = 0
    while(end_hours >= 12):
        end_hours = end_hours - 12
        if(am_pm == 'AM'):
            am_pm = 'PM'
        else:
            am_pm = 'AM'
            num_days += 1
    if(end_hours == 0):
        end_hours = 12
    if(num_days == 0):
        days_message = ""
    elif(num_days > 1):
        days_message = " ("+str(int(num_days))+" days later)"
    else:
        days_message = " (next day)"
    new_time = str(end_hours)+":"+str(end_mins)+" "+am_pm+days_message

    return new_time
