from src.mynews_bot.rss_feed import main as rss_feed_main
from mynews_bot.data import main as rss_data_main
from mynews_bot.rss_feed.utils import feed_viewer

available_rss_feed_sources = rss_data_main._get_available_rss_feed_sources()
        
# TODO: simulate cmd input & output

def test_all_rss_feed_return_data():
    """
    All rss feed sources should return data without error
    """
    for source_name in available_rss_feed_sources:
        rss_feed_details = {
            'rss_feed_url': '',
            'source': source_name,
            'top': 1
        }
        rss_feed_url = rss_data_main._get_rss_feed_url_by_source(source_name)
        if not rss_feed_url:
            raise ValueError('RSS url not found for source {}'.format(source_name))
        
        rss_feed_details['rss_feed_url'] = rss_feed_url
        feed_data = rss_feed_main._get(rss_feed_details)
        assert len(feed_data) > 0
    


