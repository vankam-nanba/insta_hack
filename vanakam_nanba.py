#!/usr/bin/env python3

import os
import sys
import requests 
import speech_recognition as sr
from gtts import gTTS
import re

banner = '''
instafollow.py [user_name]
example: instafollow vanakam_nanba

author: vanakam_nanba
'''
##password input
##instagram hack
def followers(username):
     url = 'https://www.instagram.com/' + username
     r = requests.get(url).text
     start = '"edge_followed_by":{"count":'
     end = '},"followed_by_viewer"'
     start1 = '"edge_follow":{"count":'
     end1 = '},"follows_viewer"'
     post1 = '"edge_owner_to_timeline_media":{"count":'
     post2 = ',"page_info":{"has_next_page":false,"end_cursor":null},"edges":[{"' 
     post3 = ',"page_info":{"has_next_page":true,"end_'
     followers = str(r[r.find(start)+len(start):r.rfind(end)])
     follow = str(r[r.find(start1)+len(start1):r.rfind(end1)])
     l = re.findall(',"page_info":{"has_next_page":true,"end_',r) 
     if len(l) == 1:
        posts = str(r[r.find(post1)+len(post1):r.rfind(post3)])
     else:
        posts = str(r[r.find(post1)+len(post1):r.rfind(post2)])

     result = f"{username} currently have {int(followers):,} followers and {int(follow)} following and {posts} posts"
     return result
#Enter yes to hack account,

def hack(thala):
    if thala == "yes" or "Yes" or "YES" or "y" or "Y" or "yes " or "yas":
        vai = gTTS("vaaipeyy illaii raja!")
        vai.save("/tmp/vai.mp3")
        os.system("mpv /tmp/vai.mp3")
    else:
        bye = gTTS("pooidu va makarasa")
        bye.save("/tmp/bye.mp3")
        os.system("mpv /tmp/bye.mp3")

#voice 
def voice(username):
    t = gTTS(followers(username))
    t.save('/tmp/' + username + '.mp3')
    os.system("mpv " + '/tmp/' + username + '.mp3')

#recognize audio 
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            thala = r.recognize(audio)
            print(thala)
            hack(thala)
        except:
             print("vnakam nanba. hacked your pc ")
##enterance pass
if __name__ == "__main__":
    if len(sys.argv) <=1:
        print(banner)
        exit()
    username = sys.argv[1]
    #print(banner)
    print(followers(username))
    print(voice(username))    
    t1 = gTTS("do You Want to Hack this Account! say Yes or no ")
    t1.save("/tmp/hack.mp3")
    os.system("mpv /tmp/hack.mp3")
    speak()

