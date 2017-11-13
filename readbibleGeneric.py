#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#enter the corresponding information from your Twitter application:
consumerKey = ''
consumerSecret = ''
accessKey = ''
accessSecret = ''
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

#keep track of which line we are at
currentLinetxt=open("currentLine.txt","r")
currentLine=currentLinetxt.readlines()
currentLinetxt.close()
print(currentLine)

with open('bible.txt') as fp:
    for line in fp:
        #api.update_status(status=line)
        print(line)

        #update currentLine.txt file
        currentLinetxt=open("currentLine.txt","w")
        currentLinetxt.truncate()
        currentLinetxt.write(str(line))
        currentLinetxt.close()

        time.sleep(2)#Tweet every 2 seconds
        #time.sleep(900)#Tweet every 15 minutes