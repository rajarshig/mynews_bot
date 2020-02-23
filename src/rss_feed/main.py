import feedparser as fp
from time import sleep

RSS_FEED_GET_DELAY = 2


def _get(rss_feed_details={}):
    """
    Get feed data for a single rss feed detail object
    """
    url = rss_feed_details.get('rss_feed_url')
    sleep(RSS_FEED_GET_DELAY)
    source_name = rss_feed_details.get('source')
    top = rss_feed_details.get('top')
    fetched_all_data = []
    all_data = fp.parse(url)
    print('Fetched data for {}'.format(source_name.upper()))
    for index, data in enumerate(all_data.entries):
        if index >= top:
            break
        fetched_single_data = dict()
        fetched_title = data.get('title')
        item_url = data.get('link')
        published_parsed = data.get('published_parsed')
        published = data.get('published')
        fetched_single_data['url'] = item_url 
        fetched_single_data['source'] = source_name
        fetched_single_data['title'] = fetched_title
        fetched_single_data['published'] = published
        fetched_single_data['published_parsed'] = published_parsed
        fetched_all_data.append(fetched_single_data)
    
    return fetched_all_data

