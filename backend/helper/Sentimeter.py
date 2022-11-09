from copy import deepcopy
import re
from transformers import pipeline


class SentimeterModel():
    def __init__(self) -> None:
        # initializing model 
        self.model = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment")
        self.data = []
        self.recentData = [] 
        self.result = {}
    
    def feedData(self,data):
        if(self.data):
            self.data = []
            self.result = {}
        self.data = data

    def fetchHistory(self):
        return self.recentData

    def analyzeResult(self,timeline):
        print(timeline)
        if(len(self.data)<3):
            return {"success":0, 'message':'Insufficient data to analyse'}
        if(len(self.data)<10):
            return {"success":0, 'message':'Not a popular topic.'}
        
        self.result[timeline] = []
        resCategory = {"5 stars":0,"4 stars":0,"3 stars":0,"2 stars":0,"1 star":0}
        for text in self.data:
            pred = self.model(text)
            res  = (text,pred)
            # self.result[timeline].append(res)
            resCategory[pred[0]['label']] += 1
        

        positive = resCategory["5 stars"] + resCategory["4 stars"]
        nuteral  = resCategory["3 stars"]
        negative = resCategory["1 star"]  + resCategory["2 stars"]

        positivePercentage = (positive * 100) / len(self.data) 
        negativePercentage = (negative * 100) / len(self.data) 
        nuteralPercentage  = (nuteral  * 100) / len(self.data) 

        self.result[timeline].append({'Positive':positivePercentage, 'Negative':negativePercentage, 'Nuteral': nuteralPercentage})
        self.recentData.append((deepcopy(self.data), deepcopy(self.result[timeline])))

        return {'success':1,'result':{'Positive':positivePercentage, 'Negative':negativePercentage, 'Nuteral': nuteralPercentage}}  

    def addRecord(self):
        pass
