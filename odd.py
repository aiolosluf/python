from datetime import datetime
import time
import random

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,
        31,33,35,37,39,41,43,45,47,49,51,53,55,
        57,59]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("this minute seems a little odd.")
        wait_time = random.randint(1, 5)
        print("wait for:" + str(wait_time))
        time.sleep(wait_time)
    else:
        print("Not an odd minute.")
        wait_time = random.randint(1,60)
        print("wait for:" + str(wait_time))
        time.sleep(wait_time)


# import os
# print(os.environ)
# print(os.getcwd())
# print(os.getenv('HOME'))

# import datetime
# print(datetime.date.today())
# print(datetime.datetime.today())
# print(datetime.date.isoformat(datetime.date.today()))

# import time,datetime
# print(time.strftime("%Y %H %M %a %P"))
# print(datetime.date.today())
# today = time.strftime("%A")
# print(today)
# if today == "thursday":
#     print("work!")
# elif today == "Thursday":
#     print("WORK!")
# else:
#     print("hmm")