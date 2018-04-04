
# coding: utf-8

# In[ ]:


#A basic Twitter web scrape program. This can search for users or hashtags.
#The benefit of using this program over the API is this allows for the user to scrape tweets from any date.
#The API only allows scraping tweets within the last week if a hashtag is what is being scraped.


# In[1]:


#Import required libraries
import sys
import pandas as pd


# In[3]:


#Import got depending on the version of python being used
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got


# In[4]:


#Grab tweets based on criteria
#Set setQuerySearch() to desired hashtag and setSince and setUntil to the desired date
#Change setQuerySearch to setUsername if interested in a tweets a user posted rather than a hashtag
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#WWDinCA').setSince("2018-03-20").setUntil("2018-03-24").setMaxTweets(1000)

#create empty dataframa and name columns.
twitterdata = pd.DataFrame(columns=['Date','Retweets','Hashtags','Text','Mentions'])


# In[5]:


#For loop for scraping actual tweets. Always start loop at 0.
for x in range(0, 50):
    
    #grab tweets per loop iteration
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[x]
    #Add scraped data to dataframe
    twitterdata = twitterdata.append({'Date': tweet.date, 'Retweets': tweet.retweets, 'Hashtags': tweet.hashtags, 'Text': tweet.text, "Mentions": tweet.mentions}, ignore_index=True)

#View data
twitterdata


# In[7]:


#Save twitter data to .csv
#Data is ready for analysis in Python or another program
twitterdata.to_csv("WWDinCAScrape.csv", index = False)

