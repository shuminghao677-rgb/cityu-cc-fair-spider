# import sqlite3
# import pandas as pd

# df=pd.read_csv("stem_fair_2026_raw.csv")

# conn = sqlite3.connect('stem_fair_2026.db')
# df.to_sql("jobs_raw",conn,if_exists="replace",index=False)


import sqlite3
import pandas as pd

df=pd.read_csv("stem_fair_2026_raw.csv")

conn=sqlite3.connect()