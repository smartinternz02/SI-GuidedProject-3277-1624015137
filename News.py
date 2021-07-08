import requests
import json
import pandas as pd

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199
url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/stories/list"
user_inp = ''
#Choice of templates are :  COMMODITY|CURRENCY|INDEX|INDEXFUTURE|RATE|STOCK
# querystring = {"template":user_inp,"id":"usdjpy"}

headers = {
    'x-rapidapi-key': "d730d682demshbfaf2fc584babdap15184djsnd2eec3eec4be",
    # 'x-rapidapi-key': "fa9edf3718mshfb79e7af9facba9p167875jsna5cc6604f396", my api-key
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

user_inp = str(input("Enter the topic you want to get the latest news on : \n1. COMMODITY\n2. CURRENCY\n3. INDEX\n4. INDEXFUTURE\n5. RATE\n6. STOCK\n : ")).upper()

querystring = {"template":user_inp,"id":"usdjpy"}
response = requests.request("GET", url, headers=headers, params=querystring)

result = response.json()

df = pd.DataFrame(columns = ['Card', 'Title', 'Thumbnail Link','Link to source of news'])

# print(result)
if result['stories']:
    for story in result['stories']:
        print(story)
        print(len(story))
        story.setdefault('card','')
        story.setdefault('title','')
        story.setdefault('thumbnailImage','')
        story.setdefault('longURL','')
        df.loc[len(df.index)] =[story['card'],story['title'],story['thumbnailImage'],story['longURL']]
print(result)
if result['stories']:
    print("have stories")
print(result['stories'])
# print(df["Thumbnail Link"][0])
# print(df["Link to source of news"][0])


cards =[]
titles =[]
thumbnails = []
links=  []  

# for story in result['stories']:
#     # print(story)
#     # print(len(story))
#     cards.append(story['card'])
#     titles.append(story['title'])
#     thumbnails.append(story['thumbnailImage'])
#     links.append(story['longURL'])    
    
print("cards are: ",cards)    
print("titles are: ",titles)
print("thumbnail are: ",thumbnails)
print("links are: ",links)
print("df is: ",df)