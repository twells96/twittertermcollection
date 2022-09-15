import mysql.connector
import tweepy

auth = tweepy.AppAuthHandler(consumer_key='', consumer_secret='')
api = tweepy.API(auth)
conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='', auth_plugin='mysql_native_password')

search_words = ""
date_since = ""

tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(10000)

for i in tweets:
    #cant get full_text
    tweet = i.text
    print (tweet)
    date = i.created_at
    print (date)
    screenname = i.user.screen_name

    if conn.is_connected() and hasattr(i, 'retweeted_status') == False:
                """
                Insert twitter data
                """
                cursor = conn.cursor()
                # twitter, golf
                query = "INSERT INTO tweetstorage (tweet, date, screenname) VALUES (%s, %s, %s)"
                cursor.execute(query, (tweet, date, screenname))
                conn.commit()
    else:
        print("this is a retweet")
conn.close()