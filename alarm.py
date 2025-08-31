import time 
import playsound


def alarm_main():
    print("Welcome to the Alarm Clock!")
    print("Please set the time for your alarm.\n")

    while True:
        alarm_hour = int(input("Enter hour (1-12): ")) 
        if alarm_hour not in range(1,13): 
            print("Invalid input. Hour must be between 1 and 12.")
        else: 
            break 

    while True:
        alarm_minute = int(input("Enter minutes (0-59): ")) 
        if alarm_minute not in range(0,60): 
            print("Invalid input. Minutes must be between 0 and 59.")
        else: 
            break 

    while True:
        alarm_am_pm = input("Enter AM or PM: ").strip().lower()
        if alarm_am_pm not in ["am", "pm"]:
            print("Invalid input. Please enter 'AM' or 'PM'.")
        else:
            break

    # Calculation for alarm
    cur_hour = int(time.strftime("%I"))
    cur_min = int(time.strftime("%M")) 
    cur_am_pm = time.strftime("%p").lower()
    
    h = cur_hour 
    m = cur_min
    hour = 0 
    min = 0

    while True: 
        if h == alarm_hour and m == alarm_minute:
            break 
        if h == 13: 
            h = 1
        if m == 59: 
            h += 1 
            m = -1
        if min == 59: 
            min = -1
            hour += 1 
        m += 1
        min += 1

    if cur_am_pm == alarm_am_pm:
        if alarm_hour < cur_hour:
            print(f"\nYour alarm is set to go off in {hour+12} hour(s) and {min} minute(s).")
        else:
            print(f"\nYour alarm is set to go off in {hour} hour(s) and {min} minute(s).")
    else: 
        if alarm_hour > cur_hour: 
            print(f"\nYour alarm is set to go off in {hour+12} hour(s) and {min} minute(s).")
        else:
            print(f"\nYour alarm is set to go off in {hour} hour(s) and {min} minute(s).")

    # Alarm main logic
    print("\nWaiting for the alarm time...")

    while True: 
        if cur_hour == alarm_hour and cur_min == alarm_minute and cur_am_pm == alarm_am_pm: 
            print("\nAlarm time reached.") 
            break 
        cur_hour = int(time.strftime("%I"))
        cur_min = int(time.strftime("%M")) 
        cur_am_pm = time.strftime("%p").lower()
        
    # Play the alarm sound 3 times
    for i in range(3): 
        playsound.playsound(r"d:\Fun project\Timer\homelender.mp3")
