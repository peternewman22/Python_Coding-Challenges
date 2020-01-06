import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "log_substrings.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

# make a root logger
logger = logging.getLogger()

def merge_the_tools(string, k):
    n = len(string)
    #split the string into n/k equal lengths k long
    for i in range(n//k+1):
        logger.debug(f"index {i} in range({n//k}) going up by {k})")
        t_i = string[i*k:k*(i+1)]
        logger.debug(f"string[{i*k}:{i*(k+1)}] gives t_i = {string[i*k:k*(i+1)]}")
        logger.debug(f"list t_{i}: {list(t_i)}, set: {sorted(set(list(t_i)), key=t_i.index)}")
        u_i = "".join(sorted(set(t_i), key=t_i.index))
        print(u_i)

merge_the_tools("AABCAADA", 3)
