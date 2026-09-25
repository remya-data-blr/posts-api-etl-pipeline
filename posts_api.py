import requests
import pandas as pd
import sqlite3

url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)
data = r.json()

df = pd.json_normalize(data)
print(df.columns)  # You will see id, title, userId, body

# Pick 4 columns
df_clean = df[['id', 'title', 'userId', 'body']]

conn = sqlite3.connect("posts.db")
df_clean.to_sql("posts", conn, if_exists="replace", index=False)

# Query
result = pd.read_sql("SELECT * FROM posts WHERE userId = 1", conn)
print(result)
print(f"Count: {len(result)}")

conn.close()