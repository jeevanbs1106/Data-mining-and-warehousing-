import os
import re
import pandas as pd
import hashlib

SOURCE = "sales"

pattern = re.compile(
    r"SALES_(S\d{2})_(\d{8})(?:__R\d+)?\.(csv|parquet)$",
    re.I
)

frames = []

for root, _, files in os.walk(SOURCE):
    for filename in files:
        m = pattern.match(filename)
        if not m:
            continue

        store = m.group(1)
        date = m.group(2)

        path = os.path.join(root, filename)

        if filename.lower().endswith(".csv"):
            df = pd.read_csv(
                path,
                sep=";" if store in ["S06","S07","S08","S09"] else ",",
                encoding="utf-8-sig"
            )
        else:
            df = pd.read_parquet(path)

        df = df.rename(columns={
            "item_code": "product_code",
            "quantity": "qty",
            "rate": "unit_price",
            "type": "line_type",
            "txn_time": "ts"
        })

        df["store_id"] = store
        df["business_date"] = pd.to_datetime(date).date()

        frames.append(df[
            ["store_id","business_date","bill_no","line_no",
             "product_code","qty","unit_price","line_type","ts"]
        ])

data = pd.concat(frames, ignore_index=True)

# Critical: deduplicate at line level
data = data.drop_duplicates(
    subset=["bill_no", "line_no"]
).sort_values(["bill_no", "line_no"])

print("ROWS:", len(data))

canonical = data.to_csv(index=False).encode("utf-8")
checksum = hashlib.sha256(canonical).hexdigest()

print("CHECKSUM:", checksum)