import argparse
import logging
import time

from rss_feed import main, utils

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

def cmd_runner():
    """
    Entry point of the application which handles all the command line input.

    """
    parser = argparse.ArgumentParser(description="Gets news from extracted sources")
    parser.add_argument('--source', help="Name of the news source. Available options are: 1. NYC,")
    args = parser.parse_args()
    if args.source:
        source_name = args.source
        logger.info('source argument found, validating...')
        time.sleep(1)
        logger.info('validated, now getting news of {}'.format(source_name))
        time.sleep(1)
        if source_name.lower() == 'nyc':
            rss_feed_url = 'http://rss.nytimes.com/services/xml/rss/nyt/World.xml'
        elif source_name.lower() == 'toi':
            rss_feed_url = 'https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms'
        elif source_name.lower() == 'it':
            rss_feed_url = 'https://www.indiatoday.in/rss/home'
        feed_data = main._get(rss_feed_url)
        utils.feed_viewer(feed_data)

            

# TODO: logic of __main
if __name__ == '__main__':
    cmd_runner()
