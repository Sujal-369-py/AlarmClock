import time 
from stopwatch import Stopwatch
from timer_main import timer_working
from alarm import alarm_main

class Main:
    def gui(self): 
        menu = "Press 1 for Current Time | 2 for Current Date | 3 for Stopwatch | 4 for Timer | 5 for Alarm"
        print("-" * 100)
        print("Welcome to the --Terminal Watch")
        print("-" * 100)
        while True:
            print()
            print(menu)
            print()
            try:
                choice = int(input("Your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number 1-5.")
                continue
            
            if choice == 1:
                print(f"Current Time: {time.strftime('%I')}:{time.strftime('%M')}:{time.strftime('%S')} {time.strftime('%p')}")
            elif choice == 2: 
                day = time.strftime("%d")
                mon = time.strftime("%B")
                year = time.strftime("%Y")
                print(f"Current Date: {day}-{mon}-{year}")
                print(f"Today is {time.strftime('%A')}")
            elif choice == 3: 
                Stopwatch()
            elif choice == 4: 
                timer_working()
            elif choice == 5: 
                alarm_main()
            else: 
                print("Invalid choice. Please try again..")
                
obj = Main() 
obj.gui()
