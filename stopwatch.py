import time

def Stopwatch():
    print("To stop stopwatch press (CTRL + C)")
    time.sleep(1)
    print("Stopwatch has started...")

    start_time = time.perf_counter()

    try:
        while True:
            elapsed = time.perf_counter() - start_time
            hours = int(elapsed // 3600)
            minutes = int((elapsed % 3600) // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed - int(elapsed)) * 1000)
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}", end="\r")
            time.sleep(0.01)  # updates every 10ms
    except KeyboardInterrupt:
        print("\nStopwatch has been stopped.")
# Stopwatch()
