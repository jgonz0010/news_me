import os
import sys

class ReaderConfig(object):
    def __init__(self):
        self.config_file = self.resource_path("news_me/rss_list.cfg")
        self.feed_urls = list(open(self.config_file, "r").readlines())
        self.character_speed = 75
        self.line_speed = 250
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    
