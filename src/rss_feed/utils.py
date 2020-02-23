def feed_viewer(data):
    for index, item in enumerate(data):
        print("{0} - {1} - {2}\n"
        .format(
            item['source'].upper(),
            item.get('title', ''),
            item.get('published', '') 
        ))

