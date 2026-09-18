import sqlite3
import time
import pandas as pd
import glob

files = glob.glob("data_2/notices/*.csv")
notices = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

conn = sqlite3.connect("retrieval.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS retrieval_blocks")
cur.execute("""
CREATE TABLE retrieval_blocks (
    block_key TEXT NOT NULL,
    notice_id TEXT NOT NULL,
    PRIMARY KEY (block_key, notice_id)
)
""")

for _, r in notices.iterrows():
    key = str(r["estimated_value"]).strip().lower() + "_" + str(r["closing_date"]).strip()
    cur.execute(
        "INSERT OR IGNORE INTO retrieval_blocks VALUES (?,?)",
        (key, r["notice_id"])
    )

cur.execute("CREATE INDEX idx_block_key ON retrieval_blocks(block_key)")
conn.commit()

key = (
    str(notices.iloc[0]["estimated_value"]).strip().lower()
    + "_"
    + str(notices.iloc[0]["closing_date"]).strip()
)

print("================================")
print("B(d) RETRIEVAL ACCESS TEST")
print("================================")
print("TABLE: retrieval_blocks")
print("ACCESS METHOD: B-TREE INDEX")
print("LOOKUP KEY:", key)

start = time.perf_counter()
rows = cur.execute(
    "SELECT notice_id FROM retrieval_blocks WHERE block_key = ?", (key,)
).fetchall()
indexed_time = time.perf_counter() - start

print("INDEXED PATH: B-TREE INDEX")
print("ROWS RETURNED:", len(rows))
print("WALL TIME:", indexed_time)

cur.execute("DROP INDEX idx_block_key")
conn.commit()

start = time.perf_counter()
rows2 = cur.execute(
    "SELECT notice_id FROM retrieval_blocks WHERE block_key = ?", (key,)
).fetchall()
seq_time = time.perf_counter() - start

print("REJECTED ALTERNATIVE: SEQUENTIAL SCAN")
print("ROWS RETURNED:", len(rows2))
print("WALL TIME:", seq_time)

print("================================")
print("SCHEMA PERSISTED IN: retrieval.db")
print("INDEXED LOOKUP TIME:", indexed_time)
print("SEQUENTIAL LOOKUP TIME:", seq_time)
print("DONE")
print("================================")

conn.close()