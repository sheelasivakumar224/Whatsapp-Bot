from newsapi import NewsApiClient
import os

NEWS_API = "155c8de5b98a43aeb8b648d049e11028"

newsapi = NewsApiClient(api_key = NEWS_API)

top_headlines = newsapi.get_everything(q = "Top headlines in India",
                                       sort_by='popularity',
                                       page_size=5,
                                       page = 1,
                                       from_param='2025-07-11',
                                       to = '2025-07-12')

return top_headlines['articles']
