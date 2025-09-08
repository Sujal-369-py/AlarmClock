from playsound import playsound
import time 

def timer_working():
    print("Welcome to the Timer.\nYou can set timer by specifying the hours,minutes and seconds") 
    hour = int(input("Enter the hours : "))

    while True:
        minutes = int(input("Enter the minutes : "))
        if minutes not in range(0,60):
            print("Invalid Minutes.Minutes range is from(0,59)")
        else: 
            break 

    while True: 
        sec = int(input("Enter the seconds : ")) 
        if sec not in range(0,60): 
            print("Invalid Seconds.Seconds range is from(0-59)")
        else: 
            break 

    print("Timer had started...")
    time.sleep(1)
    while True: 
        if hour == minutes == sec == 0: 
            print(f"00:00:00:00")
            break
        if minutes == 0 and sec == -1 and hour > 0: 
            hour-=1
            minutes = 60
        if sec == -1:
            minutes-=1 
            sec = 59
        for ms in range(99, -1, -1):
            print(f"{hour:02}:{minutes:02}:{sec:02}:{ms:02}", end="\r")
            time.sleep(0.01)
        sec -= 1

    print("Timer had Ended.")

    playsound("t.mp3")

# timer_working()
