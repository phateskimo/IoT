#! /usr/bin/python3

# week 3 raspberry pi interface
# by Chris Larson
# 
from twython import Twython, TwythonError, TwythonStreamer

#saved Keys in seperate file, calling it
exec(open("./twitkeys.py").read())

IanCount = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global IanCount 
        if 'text' in data:
            IanCount += 1
                    
        
        if IanCount == 3:
            print("Ian G. Harris is popular!")
        else:    
            print("found something interesting, counting: " + str(IanCount))
            
stream = MyStreamer(C_KEY, C_SECRET, A_TOKEN, A_SECRET)
stream.statuses.filter(track="Ian G. Harris")