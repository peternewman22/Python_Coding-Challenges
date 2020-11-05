from time import sleep
from random import randint
from datetime import datetime, timedelta
import keyboard

wait_time = randint(1,5)

print("Welcome to the waiting game!\n")
print("Press enter to begin!")
keyboard.wait('enter')
print(f"Wait {wait_time} seconds in")
print("3...")
sleep(1)
print("2...")
sleep(1)
print("1...")
sleep(1)
print("Go!")
start_time = datetime.now()
keyboard.wait('enter')
end_time = datetime.now()
duration = end_time - start_time
error = duration - timedelta(seconds=wait_time)
fast_or_slow = "fast" if error.seconds < 0 else "slow"
percentage_error = error.total_seconds()/wait_time*100
print(f"You waited {duration.total_seconds()} seconds which was {abs(error.total_seconds())}s ({percentage_error}%) too {fast_or_slow}!")