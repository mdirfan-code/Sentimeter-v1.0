from fastapi import FastAPI, Depends, Request, Form, status
from helper.DataAnalysis import *
from fastapi.middleware.cors import CORSMiddleware
origins = [
    '*'
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
dataAnalysis = DataAnalysis()

@app.get("/tweet/{hashtag}")
def get_tweet_analysis(hashtag:str):
    print(hashtag)
    
    return dataAnalysis.analyze_twitter(hashtag)

@app.get("/reddit/post/{id}")
def get_tweet_analysis(id:str):
    return dataAnalysis.analyze_reddit(post_id=id)
