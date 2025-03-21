# import the time module
import time


# define the countdown func.
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time up!")


# input time in seconds
t = int(input("Enter the time in seconds: "))

# function call
countdown(t)
