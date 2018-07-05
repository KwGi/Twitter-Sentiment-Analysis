import tweepy
from textblob import TextBlob
import csv
import os



# Step 1 - Authenticate
consumer_key= 'pEOTMRP4XSnCMZ7HJLqIQXXeA'
consumer_secret= 'frVYbCn6HCZmi2cvc9bDPgfEUBKgFEadgfzbyoU7tNC7tPGDrH'

access_token='1014841337856872449-3uw0K8Uxi003pdnzouVdbk1cOgBAQA'
access_token_secret='0NG4ELaf99Vtt4LHH4FV8HVaLbGnC3vASk9SE17N7tbbp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
input_search = input("Enter keyword topic: ")
public_tweets = api.search(input_search)



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself
#open a file and setting writer

with open('sentiment_analysis.csv','w',newline='') as f :

    wrt = csv.writer(f)
    wrt.writerow(['Tweet','Label'])
    #Step 4 Perform Sentiment Analysis on Tweets
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        #polarity evaluation
        if float(analysis.sentiment.polarity) > 0 :
            polarity = 'positive'
        elif float(analysis.sentiment.polarity) < 0:
            polarity = 'negative'
        else :
            polarity = 'neutral'

        #writting in csv
        wrt.writerow([tweet.text.encode("utf-8").strip(),polarity])

    print("Sentiment Analysis Successful")
    #prompt the user if he/her wants to open file in sheets
    ans = input("Do you want to open sentiment_analysis.csv?:(y/n) ").lower()
    if ans == 'y':
        os.startfile('sentiment_analysis.csv')
