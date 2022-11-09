from helper.Sentimeter import SentimeterModel
import helper.Scraper as Scraper
from collections import Counter

class DataAnalysis:
    def __init__(self):
        self.sentimeter = SentimeterModel()
    def word_freq(self,data):
        words_without_stopwords = []
        stopwords = ['','the', 'of', 'and', 'is','to','in','a','from','by','that', 'with', 'this', 'as', 'an', 'are','its', 'at', 'for','have','you','they','I','only','because','or','on','my','it','just']
        for word in data:
            words_list = word.split(' ')
            words_without_stopwords += [ word for word in words_list if word not in stopwords and not word.isdigit() ]
        res = []
        for ele in Counter(words_without_stopwords).most_common(30):
            res.append({"name":ele[0],"value":ele[1]})
        return res
    def analyze_reddit(self,post_id):
        data = Scraper.reddit_data(post_id)
        if len(data) == 0:
            return None
        print(len(data))
        self.sentimeter.feedData(data)
        word_freq = self.word_freq(data)
        return {"data":self.sentimeter.analyzeResult(0),"freq":word_freq}

    def analyze_twitter(self,hashtag):
        data = Scraper.twitter_data(hashtag)
        if len(data) == 0:
            return None
        self.sentimeter.feedData(data)
        word_freq = self.word_freq(data)
        return {"data":self.sentimeter.analyzeResult(0),"freq":word_freq}
    