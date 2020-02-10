def feed_viewer(data):
    for index, item in enumerate(data):
        print("{0}. {1}\n".format( (index+1), item.get('title', '') ))