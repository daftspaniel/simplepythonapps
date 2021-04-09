"""
    Prints out a random story from the newsboat database.
"""
import sqlite3
import re
from pathlib import Path

newsboat_folder = Path.joinpath(Path.home(), '.newsboat')

connection = sqlite3.connect(Path.joinpath(newsboat_folder, "cache.db"))
cursor = connection.cursor()
rows = cursor.execute("SELECT title,content,url FROM rss_item ORDER BY random() LIMIT 1").fetchall()
text = re.sub('<[^<]+?>', '', rows[0][1]).replace('\n','').strip()

print(rows[0][0][:78])
print(text[:78])
print(rows[0][2])
