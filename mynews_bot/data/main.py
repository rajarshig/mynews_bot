NEWS_SOURCE_RSS_MAPPING = {
    'toi':{
        'default': 'https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms'
    },
    'nyt':{
        'default': 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml'
    },
    'it':{
        'default': 'https://www.indiatoday.in/rss/home'
    },
    'gnews':{
        'default': 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US%3Aen&x=1571747254.2933'
    },
    'quint':{
        'default': 'https://prod-qt-images.s3.amazonaws.com/production/thequint/feed.xml'
    },
    'reddit':{
        'default': 'https://www.reddit.com/r/worldnews/.rss'
    },
    'bbc':{
        'default': 'http://feeds.bbci.co.uk/news/world/rss.xml'
    },
    'buzzfeed':{
        'default': 'https://www.buzzfeed.com/world.xml'
    },
    'aljazeera':{
        'default': 'http://www.aljazeera.com/xml/rss/all.xml'
    },
    'yahoonews':{
        'default': 'https://www.yahoo.com/news/world/rss'
    },
    'cnn':{
        'default': 'http://rss.cnn.com/rss/edition_world.rss'
    },
    'guardian':{
        'default': 'https://www.theguardian.com/world/rss'
    },
    'washington_post':{
        'default': 'http://feeds.washingtonpost.com/rss/world'
    },
    'cnbc':{
        'default': 'https://www.cnbc.com/id/100727362/device/rss/rss.html'
    },
    'reuters':{
        'default': 'http://feeds.reuters.com/Reuters/worldNews'
    },
    'independent':{
        'default': 'http://www.independent.co.uk/news/world/rss'
    },
    'business_standard':{
        'default': 'https://www.business-standard.com/rss/home_page_top_stories.rss'
    }
}


"""
Test cases
- if source key not found
- if source['default'] key not found
- if empty value in source['default']
"""
def _get_available_rss_feed_sources(user_prompt=False):
    if user_prompt:
        return [source.upper() for source in NEWS_SOURCE_RSS_MAPPING.keys()]
    else:
        return NEWS_SOURCE_RSS_MAPPING.keys()


def _get_rss_feed_url_by_source(source):
    
    try:
        source_rss_feed_url = NEWS_SOURCE_RSS_MAPPING[source]['default']
    except KeyError:
        raise
    return source_rss_feed_url