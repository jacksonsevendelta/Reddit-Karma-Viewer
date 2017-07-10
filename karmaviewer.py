try: input = raw_input # checks to see if in Python 3x or 2x to get input() command
except NameError: pass

import praw #Makes sure we can use the module
#The next part will tell reddit that we are who we are, so that we can
#grab info from accounts.
reddit = praw.Reddit(client_id='<YOUR CLIENT ID HERE>',
                     client_secret='<YOUR CLIENT SECRET HERE>',
                     user_agent='RPi Karma Viewer') # This can be the title of the project

me = reddit.redditor(input("Enter a reddit username: ")) #Defines the reddit username
linkkarma = me.link_karma #Defines the variable linkkarma as the username's link karma
commentkarma = me.comment_karma #Defines the variable commentkarma as the username's comment karma
totalkarma = linkkarma + commentkarma #This will make a variable called totalkarma that will add both of the karma variables together.

print "Reddit username karma viewer (RAKV) Version 1.1"
print "Script available at https://github.com/jacksonsevendelta/Reddit-Karma-Viewer"
print "You selected reddit username u/{}.".format(me)
print "TOTAL KARMA:",totalkarma
print "LINK KARMA:",linkkarma
print "COMMENT KARMA:",commentkarma
print "Finished for username",me
print "Additionally, you can find this user's page at https://reddit.com/u/{}.".format(me)
