import fbconsole
from fbconsole import graph_url
from urllib import urlretrieve

profile_pic = graph_url('/ralphharti/picture')  # define the person you want to have the profile pic from - Facebook name
urlretrieve(profile_pic, 'YOURFACE.jpg')
