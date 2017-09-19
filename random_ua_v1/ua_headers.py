import random

def random_header():
    #def LoadUserAgents(uafile="user_agents.txt"):
    def load_useragents(uafile="user_agents.txt"):
            """
            uafile : string
                path to text file of user agents, one per line
            """
            uas = []
            with open(uafile, 'rb') as uaf:
                for ua in uaf.readlines():
                    if ua:
                        uas.append(ua.strip()[1:-1-1])
            random.shuffle(uas)
            return uas

    # load the user agents, in random order
    uas = load_useragents(uafile="user_agents.txt")
    # load user agents and set headers
    ua = random.choice(uas)  # select a random user agent
    headers = {
        "Connection" : "close",  # another way to cover tracks
        "User-Agent" : ua}
    return headers

# get random headers
headers = random_header()

print(headers)
