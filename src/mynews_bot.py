import argparse
import time
import sys

from rss_feed import main as rss_feed_main
from rss_feed.utils import feed_viewer
from data import main as rss_data_main
from multiprocessing import Pool, cpu_count

available_rss_feed_sources = rss_data_main._get_available_rss_feed_sources()
available_rss_feed_sources_user_prompt = rss_data_main._get_available_rss_feed_sources(True)
RSS_FEED_TOP_COUNT = 10
AVIALABLE_CPU_COUNT = cpu_count()

__version__ = '0.1.1'


def cmd_runner():
    """
    Entry point of the application which handles all the command line input.

    """
    parser = argparse.ArgumentParser(description="Get news from extracted sources")
    parser.add_argument('-s', '--source', help="Name of the news source. Available options are: {}"
    .format(', '.join(
        available_rss_feed_sources_user_prompt
        )
    ))
    parser.add_argument('-t', '--top', help="Count of news items to show from top order. Default: 10")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    
    rss_feed_top_count = RSS_FEED_TOP_COUNT
    if args.top:
        if not args.top.isnumeric():
            raise argparse.ArgumentTypeError('Provide a positive integer for --top argument')
            
        else:
            rss_feed_top_count = int(args.top)

    if args.source:
        source_name = args.source.lower()
        print('Source argument found, validating...')
        time.sleep(1)
        source_name_is_valid = source_name in available_rss_feed_sources
        
        if not source_name_is_valid:
            print(
                'Invalid input {0} for source. Available sources are {1} '
                .format(source_name, ', '.join(available_rss_feed_sources_user_prompt)))
            sys.exit()
        
        
        rss_feed_details = {
            'rss_feed_url': '',
            'top': rss_feed_top_count,
            'source': source_name
        }
        rss_feed_url = rss_data_main._get_rss_feed_url_by_source(source_name)
        if not rss_feed_url:
            raise ValueError('RSS url not found for source {}'.format(source_name))
        
        rss_feed_details['rss_feed_url'] = rss_feed_url

            
        rss_feed_details['top'] = rss_feed_top_count
            
        print('Getting news...\n\n')
        time.sleep(1)
        
        feed_data = rss_feed_main._get(rss_feed_details)
        feed_viewer(feed_data)
    else:
        print('--source argument not provided, getting data for all available sources...')
        rss_feed_details_list = []
        for source_name in available_rss_feed_sources:
            rss_feed_details = {
                'rss_feed_url': '',
                'source': source_name,
                'top': rss_feed_top_count
            }
            rss_feed_url = rss_data_main._get_rss_feed_url_by_source(source_name)
            if not rss_feed_url:
                raise ValueError('RSS url not found for source {}'.format(source_name))
            
            rss_feed_details['rss_feed_url'] = rss_feed_url
            rss_feed_details_list.append(rss_feed_details)
        
        with Pool(AVIALABLE_CPU_COUNT) as p:
            feed_data_list = p.map(rss_feed_main._get, rss_feed_details_list) 
        # put list of lists in a single list
        feed_data_flattened_list = []
        for feed_data in feed_data_list:
            feed_data_flattened_list.extend(feed_data) 

        feed_viewer(feed_data_flattened_list)
            
            

# TODO: logic of __main
if __name__ == '__main__':
    cmd_runner()
