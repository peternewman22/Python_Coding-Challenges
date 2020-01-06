import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "log_miniongame.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

# make a root logger
logger = logging.getLogger()

def minion_game(string):
    string = string.upper()
    vowels = ["A","E","I","O","U"]
    substrings = []
    Kevin = []
    Stuart = []
    for length_index in reversed(range(1,len(string)+1)):
        # logger.debug(f"index = {length_index}")
        for x in range(1+len(string) - length_index):
            sliver = string[x:length_index+x]
            # logger.debug(f"Making a slice {length_index} long {1+len(string)- length_index} times starting at index {x}")
            # logger.debug(f"This gives us: {sliver}")
            substrings.append(sliver)
    for eachWord in substrings:
        # logger.debug(f"Checking the first letter of {eachWord}: {eachWord[0]}")
        if eachWord[0] in vowels:
            # logger.debug(f"point to Kevin")
            Kevin.append(eachWord)
        else:
            # logger.debug(f"point to Stuart")
            Stuart.append(eachWord)

    if len(Kevin) > len(Stuart):
        return f"Kevin {len(Kevin)}"
    elif len(Stuart) > len(Kevin):
        return f"Stuart {len(Stuart)}"
    else:
        return "Draw"

print(minion_game("BANANA"))

"""
This took WAY Too long
"""

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"
