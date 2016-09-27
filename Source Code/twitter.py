#import necessary methods from tweepy lib
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import time

#variables that contains the user credentials to access Twitter API
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"

#This is a basic listener that just prints received tweets to stdout.
class MyStreamListener(StreamListener):
    
    #constructor
    def __init__(self, start_time, time_limit = 60):
        print "Stream listener"
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
        self.count = 0

    def on_data(self, data):
        print "on_data",data
        saveFile = open('USA_President_new.json','w')
        self.count += 1
        while(time.time() - self.time) < self.limit:
            try:
                #print 'processing '+str(self.count)
                self.tweet_data.append(data)
                return
            except BaseException, e:
                print str(e)
                pass
        print 'start writing..'
        for item in self.tweet_data:
            saveFile.write(item+'\n')
        saveFile.close()
        print 'finished...'
        exit()
        
        
    def on_status(self, status):
        print status.text

    def on_error(self, status_error):
        if status_error == 401:
            print "authentication failed..."

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    #create OAuthHandler instance
    auth = OAuthHandler("9fOLNbAi9RGjENqI4k2KAEg1p", "Pi0CrpzLILQ2o10UVBfDplO38UZCfToOVjA1QXV8WxwqqYyfzb")
    auth.set_access_token("772031126323990528-0Qx516BxgOtzPFrraT0MpCE8AWb3b6P", "mDmFIRchXVKw2crrqsxuwhwDTx970nMR35I0Loxd4QzBK")
    
    api = API(auth)
    
    #------------- this will return the lastest 20 tweets content----------------#
    
    public_tweets = api.home_timeline()
    count = 0
    for tweet in public_tweets:
        print tweet.text+"\n"
        count += 1
    print count
    
    #----------------------------------#
    current_time = time.time()
    stream = Stream(auth, MyStreamListener( current_time, time_limit = 2600))
    
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Donald Trump','Trump','Hillary Clinton','Hillary'])
