# twitter_sentiment_analysis
Twitter Sentiment Analysis Challenge for Learn Python for Data Science #2 by @Sirajology on Youtube

##Overview

The code uses the [tweepy](http://www.tweepy.org/)  library to access the Twitter API and the [TextBlob](https://textblob.readthedocs.io/en/dev/) library to perform Sentiment Analysis on each Tweet. We'll be able to see how positive or negative each tweet is about whatever topic we choose.

##Dependencies

* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

##Usage

Once you have your dependencies installed via pip, run the script in terminal via

```
python Twitter-Sentiment-Analysis.py
```

##Added

Instead of printing out each tweet, save each Tweet to a CSV file with an associated label. The label is either 'Positive' or 'Negative'.
