import sqlite3
import pandas as pd

df=pd.read_csv("stem_fair_2026_raw.csv")

conn = sqlite3.connect('stem_fair_2026.db')