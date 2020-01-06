from collections import Counter
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "log_collections_challenge.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

# make a root logger
logger = logging.getLogger()

"""10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50"""
total = 0
logger.debug(f"total: {total}")
shoes = Counter("2 3 4 5 6 8 7 6 5 18".split())
logger.debug(f"Shoes: {shoes}")
customers = ["6 55",
"6 45",
"6 55",
"4 40",
"18 60",
"10 50"]
for x in customers:
    xs = x.split()
    i = xs[0]
    logger.debug(f"Checking for a size {i}: there are {shoes[i]} in stock")
    if shoes[i] > 0:
        logger.debug(f"Adding the price of the shoes to the total: {xs[1]}")
        total += int(xs[1])
        shoes[i] -= 1
    else:
        logger.debug("None left in stock. No Sale.")

print(total)
