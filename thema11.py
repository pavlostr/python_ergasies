#!/usr/bin/env python
# -*- coding: iso-8859-7 -*-


#ΒΙΒΛΙΟΘΗΚΗ ΑΠΑΡΑΙΤΗΤΗ ΓΙΑ ΝΑ ΤΡΕΞΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ
import tweepy


#ΚΛΕΙΔΙΑ ΓΙΑ ΧΡΗΣΗ ΤΟΥ TWITTER API
CONSUMER_KEY = 'p6RzAga4CLkKUROGWrPwPlWKb'
CONSUMER_SECRET = 'sRLOZZGhJZZjLnqMZ4iHBY0AdnHLiX2FmUIzX9DOjjxWqq8vxI'
ACCESS_TOKEN = '707976846407761920-J4SXJjZkT3mPjJi90yfgbN0c843t24P'
ACCESS_SECRET = 'vpv3tZPxE53RWtN6kSCA4AjDuJyt9eB8pHgLAJq0AELco'



if __name__ == '__main__':

     auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
     auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
     auth.secure = True
     api = tweepy.API(auth)


     x=raw_input('ΔΩΣΤΕ ΤΟ ΠΡΩΤΟ ΟΝΟΜΑ')#ΕΙΣΑΓΩΓΗ ΟΝΟΜΑΤΩΝ ΑΠΤΟ ΧΡΗΣΤΗ
     y=raw_input('ΔΩΣΤΕ ΤΟ ΔΕΥΤΕΡΟ ΟΝΟΜΑ')


     data = api.get_user(x)
     data2 = api.get_user(y)


#ΕΚΤΥΠΩΣΗ DATA ΠΡΩΤΟΥ ΟΝΟΜΑΤΟΣ
     print 'Profile@ ' + str(data.name)
     print 'Followers: ' + str(data.followers_count)
     print 'Following: ' + str(data.friends_count)
     print 'Likes: ' + str(data.favourites_count)
     print 'Tweets: ' + str(data.statuses_count)
     print '\n'

#ΕΚΤΥΠΩΣΗ DATA ΔΕΥΤΕΡΟΥ ΟΝΟΜΑΤΟΣ
     print 'Profile@ ' + str(data2.name)
     print 'Followers: ' + str(data2.followers_count)
     print 'Following: ' + str(data2.friends_count)
     print 'Likes: ' + str(data2.favourites_count)
     print 'Tweets: ' + str(data2.statuses_count)
     print '\n'




score1=0
score2=0

#ΣΥΝΘΗΚΗ IF-ELIF ΓΙΑ ΕΚΤΥΠΩΣΗ ΣΚΟΡ
if int(str(data.followers_count)) > int(str(data2.followers_count)):
     score1 = score1 + 1
elif int(str(data.followers_count)) < int(str(data2.followers_count)):
     score2 = score2 + 1

if int(str(data.friends_count)) > int(str(data2.friends_count)) :
     score1 = score1 + 1
elif int(str(data.friends_count)) < int(str(data2.friends_count)):
     score2 = score2 + 1    

if int(str(data.favourites_count)) > int(str(data2.favourites_count)) :
     score1 = score1 + 1
elif int(str(data.favourites_count)) < int(str(data2.favourites_count)):
     score2 = score2 + 1
     
if int(str(data.statuses_count)) > int(str(data2.statuses_count)) :
     score1 = score1 + 1
elif int(str(data.statuses_count)) < int(str(data2.statuses_count)):
     score2 = score2 + 1
 

#ΕΚΤΥΠΩΝΕΙ ΤΟ ΣΚΟΡ
print "ΣΚΟΡ",score1,"-" , score2


















