import os
import re
import shutil

SOURCE = "sales"
DEST = "sales_landed"

pattern = re.compile(
    r"SALES_(S\d{2})_(\d{8})(?:__R\d+)?\.(csv|parquet)$",
    re.IGNORECASE
)

count = 0

for root, dirs, files in os.walk(SOURCE):
    for filename in files:
        m = pattern.match(filename)

        if not m:
            continue

        store = m.group(1)
        date = m.group(2)

        month = f"{date[:4]}-{date[4:6]}"

        target = os.path.join(
            DEST,
            f"store={store}",
            f"month={month}"
        )

        os.makedirs(target, exist_ok=True)

        shutil.copy2(
            os.path.join(root, filename),
            os.path.join(target, filename)
        )

        count += 1

print("FILES LANDED:", count)
print("DESTINATION:", DEST)
print("DONE")