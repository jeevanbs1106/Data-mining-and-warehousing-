import pandas as pd
import glob
import time
import matplotlib.pyplot as plt
from collections import defaultdict

files = glob.glob("data_2/notices/*.csv")
notices = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
pairs = pd.read_csv("data_2/labelled_pairs.csv")

print("TOTAL NOTICES:", len(notices))
print("LABELLED PAIRS:", len(pairs))

# =====================================================
# BEFORE MITIGATION
# =====================================================

start = time.perf_counter()

blocks = defaultdict(list)

for _, r in notices.iterrows():
    key = (
        str(r["estimated_value"]).strip().lower()
        + "_"
        + str(r["closing_date"]).strip()
    )
    blocks[key].append(r["notice_id"])

candidate_before = set()

for ids in blocks.values():
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            candidate_before.add(tuple(sorted((ids[i], ids[j]))))

runtime_before = time.perf_counter() - start

# work per notice
work = defaultdict(int)

for ids in blocks.values():
    n = len(ids)
    for x in ids:
        work[x] += n - 1

work_df = pd.DataFrame({
    "notice_id": list(work.keys()),
    "work": list(work.values())
})

work_df = work_df.sort_values("work", ascending=False)

total_work = work_df["work"].sum()
top1_n = max(1, int(len(work_df) * 0.01))
top1_work = work_df.head(top1_n)["work"].sum()

# labelled recall
survive_before = 0

for _, r in pairs.iterrows():
    p = tuple(sorted((r["notice_id_a"], r["notice_id_b"])))
    if p in candidate_before:
        survive_before += 1

recall_before = survive_before / len(pairs)

print("\n==============================")
print("BEFORE MITIGATION")
print("==============================")
print("CANDIDATE PAIRS:", len(candidate_before))
print("RUNTIME SECONDS:", runtime_before)
print("RUNTIME MINUTES:", runtime_before / 60)
print("LABELLED PAIRS SURVIVED:", survive_before)
print("LABELLED RETRIEVAL RECALL:", recall_before)
print("TOP 1% NOTICE WORK SHARE:", top1_work / total_work)

print("\nTOP 10 NOTICES BY WORK")
print(work_df.head(10).to_string(index=False))

# =====================================================
# MITIGATION
# Oversized blocks split by title prefix
# =====================================================

MAX_BLOCK = 5

start = time.perf_counter()

new_blocks = defaultdict(list)

for _, r in notices.iterrows():

    value = str(r["estimated_value"]).strip().lower()
    date = str(r["closing_date"]).strip()

    base = value + "_" + date

    title = str(r["title"]).lower()
    prefix = "".join(c for c in title if c.isalnum())[:5]

    if len(blocks[base]) > MAX_BLOCK:
        key = base + "_" + prefix
    else:
        key = base

    new_blocks[key].append(r["notice_id"])

candidate_after = set()

for ids in new_blocks.values():
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            candidate_after.add(tuple(sorted((ids[i], ids[j]))))

runtime_after = time.perf_counter() - start

survive_after = 0

for _, r in pairs.iterrows():
    p = tuple(sorted((r["notice_id_a"], r["notice_id_b"])))
    if p in candidate_after:
        survive_after += 1

recall_after = survive_after / len(pairs)

# =====================================================
# PLOT
# =====================================================

plt.figure(figsize=(8,5))

plt.hist(work_df["work"], bins=50)

plt.xlabel("Candidate comparisons per notice")
plt.ylabel("Number of notices")
plt.title("Retrieval Work Distribution Before Mitigation")

plt.tight_layout()
plt.savefig("B_e_work_distribution_before.png", dpi=200)
plt.close()

# =====================================================
# FINAL RESULTS
# =====================================================

print("\n==============================")
print("AFTER MITIGATION")
print("==============================")
print("MAX BLOCK SIZE:", MAX_BLOCK)
print("CANDIDATE PAIRS:", len(candidate_after))
print("RUNTIME SECONDS:", runtime_after)
print("RUNTIME MINUTES:", runtime_after / 60)
print("LABELLED PAIRS SURVIVED:", survive_after)
print("LABELLED RETRIEVAL RECALL:", recall_after)

print("\n==============================")
print("MITIGATION PRICE")
print("==============================")

print(
    "CANDIDATE PAIR CHANGE:",
    len(candidate_after) - len(candidate_before)
)

print(
    "RUNTIME CHANGE SECONDS:",
    runtime_after - runtime_before
)

print(
    "RECALL CHANGE:",
    recall_after - recall_before
)

print(
    "RECALL LOSS:",
    recall_before - recall_after
)

print(
    "RECALL LOSS PERCENT:",
    (recall_before - recall_after) * 100
)

print("\nPLOT SAVED: B_e_work_distribution_before.png")

print("\nDONE")