from newsapi import NewsApiClient
import os
from flask import Flask

NEWS_API = "155c8de5b98a43aeb8b648d049e11028"
newsapi = NewsApiClient(api_key = NEWS_API)


app = Flask(__name__)

@app.route('/')
def home():
    return "Server Running Successfully"

@app.route('/news', methods = ['GET'])
def news():
    top_headlines = newsapi.get_everything(q = "Top headlines in India",
                                       sort_by='popularity',
                                       page_size=5,
                                       page = 1,
                                       from_param='2025-07-11',
                                       to = '2025-07-12')

    return top_headlines['articles']

if __name__ == "__main__":
    app.run(debug=True)
