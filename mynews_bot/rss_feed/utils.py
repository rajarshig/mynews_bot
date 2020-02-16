def feed_viewer(data):
    for index, item in enumerate(data):
        print("{0} - {1}. {2}\n"
        .format(item['source'].upper(), (index+1), item.get('title', '') ))

