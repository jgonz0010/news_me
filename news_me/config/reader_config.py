class ReaderConfig(object):
    def __init__(self):
        self.feed_urls = list(open("rss_list.cfg", "r").readlines())
        self.character_speed = 75
        self.line_speed = 250