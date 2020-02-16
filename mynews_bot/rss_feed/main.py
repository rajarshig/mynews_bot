import feedparser as fp
from time import sleep
from mynews_bot.utils.logger import logger    
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
    logger.info('Fetched data for {}'.format(source_name.upper()))
    for index, data in enumerate(all_data.entries):
        if index >= top:
            break
        fetched_single_data = dict()
        fetched_title = data.title
        fetched_single_data['source'] = source_name
        fetched_single_data['title'] = fetched_title
        item_url = data.link
        # strip extra params
        item_url =  item_url.split("?emc=rss&partner=rss")[0]
        fetched_all_data.append(fetched_single_data)
    
    return fetched_all_data

