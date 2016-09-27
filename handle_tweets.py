import json
import numpy
import matplotlib.pyplot as plt
import plotly.plotly as py

class utilities:
    def __init__(self, file_name):
        self.file = file_name
        self.tweets = []
        self.keywords = {'Trump':0, 'Hillary':0}
        print 'intialzing...'
        
        #read json file into list
    def readFile(self):
        f = open(self.file,'r')
        for item in f:
            if item == '' or item == '\n':
                continue
            #print item
            self.tweets.append(json.loads(item))
            
        #get count for each of the keywords - chinese, japanese, english
    def getCount(self):
        count = 0
        for item in self.tweets:
            count += 1
            if 'text' not in item:
                print "missing text.."
                continue
            print item['text']
            if 'Hillary'.lower() in item['text'].lower():
                self.keywords['Hillary'] = self.keywords['Hillary'] + 1
            elif 'Trump'.lower() in item['text'].lower():
                self.keywords['Trump'] = self.keywords['Trump'] + 1
        print "total items are "+str(count)
        
        #draw the graph
    def drawGraph(self):
        #x = ['Chinese','Japanese','English']
        #y = [self.keywords[x[0].lower()],self.keywords[x[1].lower()],self.keywords[x[2].lower()]]
        plt.bar(range(len(self.keywords)), self.keywords.values(), align='center')
        plt.xticks(range(len(self.keywords)), self.keywords.keys())
        plt.xlabel("President")
        plt.ylabel("Counts")


if __name__ == '__main__':
    file = 'USA_President_new.json'
    obj = utilities(file)
    obj.readFile()
    obj.getCount()
    obj.drawGraph()
    print obj.keywords
    
