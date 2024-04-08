import re

class DecryptPassword:
    def __init__(self, string:str):
        self.original = ""

        # find numbers
        f = re.search("^\d+", string) # looking for numbers
        numbers = list(string[f.start():f.end()])
        # print(string, numbers)
        string = string[f.end():]
        # print(string, " -->new string:")
        # replace 0 with numbers
        for i in range(len(numbers)):
            string = re.sub('0',numbers.pop(),string, count=1)
        # print(string)

        # reverse upper case and lower case
        # first, split the word basing on the stars
        g = re.split(r"(?<=[A-Z][a-z])\*", string) # looking for upper-lower-* characters as they appear
        # print(g)
        if len(g)>1:
            for i in range(len(g)-1):
                self.original += g[i][:-2]+g[i][-2:][::-1]
            else:
                self.original += g[-1]
        else:
            self.original = string

        
    def __repr__(self):
        return str(self.original)

if __name__ == "__main__":
    print(DecryptPassword("43Ah*ck0rr0nk")) # "hAck3rr4ank"