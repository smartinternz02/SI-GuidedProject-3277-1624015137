# -*- coding: utf-8 -*-
#importing required libraries
from flask import Flask, request, render_template
import numpy as np
import re
import requests
import pandas as pd
import json
# from gevent.pywsgi import WSGIServer
import os

#initializing the flask app
app = Flask(__name__)

def check(user_inp):

    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/stories/list"
    querystring = {"template":user_inp,"id":"usdjpy"}
    headers = {
    'x-rapidapi-key': "d730d682demshbfaf2fc584babdap15184djsnd2eec3eec4be",
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    df = pd.DataFrame(columns = ['Card', 'Title', 'Thumbnail Link','Link to source of news'])
    if result['stories']:
        for story in result['stories']:
            # print(story['thumbnailImage'])
            story.setdefault('card','')
            story.setdefault('title','')
            story.setdefault('thumbnailImage','')
            story.setdefault('longURL','')
            # print(len(story))
            df.loc[len(df.index)] =[story['card'],story['title'],story['thumbnailImage'],story['longURL']]
        print(df)
    return df
    

#home page
@app.route('/')
def home():
    return render_template('base.html')

#News results page
@app.route('/predict',methods=['POST'])
def y_predict():
    output=request.form['news1']
    df=check(output)
    print(df)
    if df.empty:
        str="data is not available sorry!"
        return render_template('base.html',main=str)
    str="Check out the news articles on "+output
    return render_template('base.html',main=str,
                           img1=df["Thumbnail Link"][0],img2=df["Thumbnail Link"][1],img3=df["Thumbnail Link"][2],
                           img4=df["Thumbnail Link"][3],img5=df["Thumbnail Link"][4],img6=df["Thumbnail Link"][5],
                           img7=df["Thumbnail Link"][6],img8=df["Thumbnail Link"][7],img9=df["Thumbnail Link"][8],
                           img10=df["Thumbnail Link"][9],
                           src1=df["Link to source of news"][0],src2=df["Link to source of news"][1],src3=df["Link to source of news"][2],
                           src4=df["Link to source of news"][3],src5=df["Link to source of news"][4],src6=df["Link to source of news"][5],
                           src7=df["Link to source of news"][6],src8=df["Link to source of news"][7],src9=df["Link to source of news"][8],
                           src10=df["Link to source of news"][9],
                           data1=df["Title"][0],data2=df["Title"][1],data3=df["Title"][2],data4=df["Title"][3],data5=df["Title"][4],
                           data6=df["Title"][5],data7=df["Title"][6],data8=df["Title"][7],data9=df["Title"][8],data10=df["Title"][9])

if __name__ == "__main__":
    port = os.getenv('VCAP_APP_PORT','8080')
    app.secret_key=os.urandom(12)
    # app.run(debug=True,port=port,host='0.0.0.0')
    app.run(debug=True)
    