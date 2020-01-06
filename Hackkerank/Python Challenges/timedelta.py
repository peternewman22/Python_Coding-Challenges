
from datetime import datetime, timedelta
from math import fabs


tests = [
    "Sun 10 May 2015",
    "Sun 10 May 2015 13:54:36",
    "Sun 10 May 2015 13:54:36 -0700"
]
#"%a %d %m %Y %H:%M:%S %z"

# print(datetime.strptime(tests[0], "%a %d %b %Y"))
# print(datetime.strptime(tests[1], "%a %d %b %Y %H:%M:%S"))
# print(datetime.strptime(tests[2], "%a %d %b %Y %H:%M:%S %z"))


def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, format_str)
    t2 = datetime.strptime(t2, format_str)
    #print(t1)
    #print(t2)
    time_delta = t1 - t2
    print(int(fabs(time_delta.total_seconds())))


time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
