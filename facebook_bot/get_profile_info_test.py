# So far it only works if the last action was to post a new status update!!!!!
# Otherwise what comes after message in posts_person file is something else

import fbconsole
from fbconsole import graph_url
from urllib import urlretrieve
import re
import mmap
import json
import requests
import os
import shutil
import facebook


fbconsole.authenticate()

f = open('posts_person3.json', 'w+r+b')
a = open('all.txt','w+r+b')
json_file = open('json_info.txt', 'w')
t = open('.fb_access_token', 'r+b')  			# get the token retrieved by fbconcole.authenticate()
t.seek(18)
mt = mmap.mmap(t.fileno(), 0)
mt.seek(0) # reset file cursor
token_find = re.search('scope', mt)
token_end = token_find.end()
token_point = token_end - 27
#token = t.read(token_point)
token = 'CAAI1wZCZCgJUEBAKofuzMEKuoHFklhbWLlqMVg8yjk7w39QZA1EKBoWOVoW8AeIpdOXYmBUzmWRHZAL2AYRzcQrCoxy3fZCRgBL3jULCnWPLfZAy0ZBsIbcbGRsFaWxlVubgdDGwwCcbRYJXa2kMZAr2MXVZCWZBgYgVzesHIEJsG7f7UoaUhkOvar8qO7DIB81ZBXCcShMjPRvLgZDZD'
#print(token)
graph = facebook.GraphAPI(token)
name = 'ralphharti'

newpath = 'data/' + name 
if not os.path.exists(newpath): os.makedirs(newpath)

#profile_pic = graph_url('/' + name + '/picture') #Request facebook profile pic
#filename = name + '.jpg'
#
#urlretrieve(profile_pic, filename)
#
#shutil.move('/Users/ralph/Desktop/' +filename, '/Users/ralph/Desktop/' + name )

last_activity = open('last_activity.txt' ,'w')
link = open('link.txt', 'w')

r = requests.get("https://graph.facebook.com/" + name + "/posts/" + '?access_token=' + token) 		# get the json file for the feed

raw = json.loads(r.text)
#json_file.write(r)
rawstr = str(raw)
a.write(rawstr)

activity = ''
activity_person = ''
activity_link = ''
#print (raw['data'][0])
#for i in range(len(raw['data'])):
#print raw['data'][0]
if ('story' in raw['data'][0]):
    activity = raw['data'][0]['story']
    activity_person = raw['data'][0]['from']['name']
    if ('link' in raw['data'][0]['story']):
        activity_link = raw['data'][0]['link']    
elif ('message' in raw['data'][0]):
    activity = raw['data'][0]['message']
    activity_person = raw['data'][0]['from']['name']
    if ('link' in raw['data'][0]['message']):
        activity_link = raw['data'][0]['link']  
elif ('picture' in raw['data'][0]):
    activity = raw['data'][0]['picture']
    activity_person = raw['data'][0]['from']['name']
    if ('link' in raw['data'][0]['story']):
        activity_link = raw['data'][0]['link']


total = 0 # Count for number of posts
for post in fbconsole.iter_pages(graph.get_object('/'+name+'/feed')): # Iterates over the feed and retrieves posts
    if ('message' in post): # Makes sure it is a post and not a 'like', comment etc.
        total += 1
        if (post['message'] != activity):
            print total,':', post['updated_time'], '\n', post['message'], '\n' # Prints posts
        if total > 0: break # Limits to three, change 2-> 4 if you want the last 5 posts etc.

print activity, 'From', activity_person
if (activity_link != ''):
    print 'Click for link:', activity_link



last_activity.close()
link.close()
f.close()
t.close()



