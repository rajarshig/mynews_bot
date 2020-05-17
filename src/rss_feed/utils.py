def feed_viewer(data):
    for index, item in enumerate(data):
        print("{0} - {1}\n{2}\n{3}\n\n"
        .format(
            item['source'].upper(),
            item.get('title', ''),
            item.get('published', ''),
            item.get('url', '')
        ))

