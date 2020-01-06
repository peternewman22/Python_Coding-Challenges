import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "log_complex_polar.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

# make a root logger
logger = logging.getLogger()

test_list = [
    "1+j", #re > 0, im = 1
    "1-2j", #re > 0, im < 0
    "-5j",  # re = 0, im < 0
    "5j", # re = 0, im > 0
    "5", # re > 5, im = 0
    "-5", # re < -5, im = 0
    "-5+j" # re < 0, im = 1
    "-5-j"
]

# look for j to determine if im > 0 or im >0

for x in test_list:
    test = list(x)
    logger.debug(test)
