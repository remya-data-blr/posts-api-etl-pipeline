# Posts API ETL Pipeline

## What I did
Built ETL pipeline to extract 100 posts from REST API and load into SQLite.

## Flow
API -> Pandas (json_normalize) -> SQLite -> SQL Query

## Steps
1. **Extract:** GET https://jsonplaceholder.typicode.com/posts
2. **Transform:** Cleaned flat JSON using `pd.json_normalize()` 
3. **Load:** Loaded into `posts.db` - 100 rows
4. **Query:** Filtered posts where userId = 1

5. 
10 posts found for userId 1.

## Tech Used
- Python
- Requests
- Pandas
- SQLite

## How to Run
```bash
python posts_api.py
```
