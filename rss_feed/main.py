import feedparser as fp

#TODO: use common logger module

def _get(url=None):
    
    fetched_all_data = []
    all_data = fp.parse(url)
    for index, data in enumerate(all_data.entries):

        fetched_single_data = dict()
        fetched_title = data.title
        
        fetched_single_data['title'] = fetched_title
        item_url = data.link
        # strip extra params
        item_url =  item_url.split("?emc=rss&partner=rss")[0]
        # fetched_single_data['nyt_url'] = item_url

        fetched_all_data.append(fetched_single_data)
    return fetched_all_data
