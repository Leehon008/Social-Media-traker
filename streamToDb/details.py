TRACK_TERMS = ['Zimbabwe WildLife', 'Zimbabwe Tourism Authority', 'Zimbabwe Parks','Zimbabwe Parks and WildLife',
               'Zimbabwe Tourism', 'Zimbabwe Parks and Wildlife', 'Zimbabwe BeautifulZim']
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "Converted_tweets.csv"
TABLE_NAME = "business_postings"

try:
    from streamToDb.private import *
except Exception:
    pass
