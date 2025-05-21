import tkinter as tk
import feedparser
import random

class Reader(object):
    def __init__(self, root, cfg):
        self.cfg = cfg
        self.root = root
        self.feed_urls = random.sample(cfg.feed_urls, len(cfg.feed_urls))
        self.character_speed = cfg.character_speed
        self.line_speed = cfg.line_speed
        self.ticker = tk.Label(root, text="", width=250, font=("Roboto", 12), bg="#27548A", fg="#DDA853")
        self.ticker.pack()

        self.feed_entries = self.get_feed_entries()
        self.current_url = 0
        self.current_char = 0


    def get_feed_entries(self):
        if len(self.feed_urls) <= 0:
            self.feed_urls = random.sample(self.cfg.feed_urls, len(self.cfg.feed_urls))

        # Parse the feeds and collect all the entries
        entries = []
        feed = feedparser.parse(self.feed_urls[0])
        for entry in feed.entries:
            try:
                line = f"{entry.title}:{entry.description}".upper()
            except:
                line = f"{entry.title}".upper()
            entries.append(line)
        return entries


    def display_next_char(self):
        # If we have lines to display
        if len(self.feed_entries) > 0:
            line = self.feed_entries[0]
            if self.current_char < len(line):
                # Update the ticker text with the next character
                self.ticker.config(text=line[:self.current_char + 1])
                self.current_char += 1
                # Schedule the next character to be displayed
                self.root.after(self.character_speed, self.display_next_char)
            else:
                # Move to the next line
                del self.feed_entries[0]
                self.current_char = 0
                # Schedule the next line to be displayed after a pause
                self.root.after(self.line_speed, self.display_next_char)
        else:
            del self.feed_urls[0]
            self.feed_entries = self.get_feed_entries()
            self.root.after(self.line_speed, self.display_next_char)