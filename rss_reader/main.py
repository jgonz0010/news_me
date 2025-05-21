from config import reader_config
from tkinter import *
from reader import reader

cfg = reader_config.ReaderConfig()

root = Tk()
root.title("News Feed")
root.wm_attributes('-topmost', True)
root.attributes('-toolwindow', True)
root.resizable(width=False, height=False)
root.overrideredirect(1)
root.geometry(f"{root.winfo_screenwidth()//2}x20+{(root.winfo_screenwidth()//4)}+2")
app = reader.Reader(root, cfg)

# Start the process of displaying the feed entries
root.after(0, app.display_next_char)

root.mainloop()