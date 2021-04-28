"""
    Prints out a random story from the newsboat database.
"""
import sqlite3
import re
from pathlib import Path

# Connect to the sqlite database in newsboat's config folder.
newsboat_folder = Path.joinpath(Path.home(), '.newsboat')
connection = sqlite3.connect(Path.joinpath(newsboat_folder, "cache.db"))

# Run a query to pull out a randome story from the database.
cursor = connection.cursor()
QUERY = "SELECT title,content,url FROM rss_item ORDER BY random() LIMIT 1"
rows = cursor.execute(QUERY).fetchall()

# Format the text to remove HTML tags and new lines.
text = re.sub('<[^<]+?>', '', rows[0][1]).replace('\n', '').strip()

# Display the output to the terminal.
print(rows[0][0][:78])
print(text[:78])
print(rows[0][2])
