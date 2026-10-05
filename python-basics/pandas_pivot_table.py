import pandas as pd
df = pd.DataFrame({
    "sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "batch": ["B1", "B1", "B2", "B2", "B3", "B3"],
    "reads": [800, 1500, 2200, 500, 3000, 1200],
    "status": ["FAIL", "PASS", "PASS", "FAIL", "PASS", "PASS"]
})

pivot_table1 = pd.pivot_table(df, values="reads", index="batch", columns="status", aggfunc="mean")
pivot_table2 = pd.pivot_table(df, values="reads", index="batch", columns="status", aggfunc=["mean", "sum"])
pivot_table3 = pd.pivot_table(df, values="reads", index="batch", columns="status", aggfunc=["mean", "sum", "count"])
print(pivot_table1)
print(pivot_table2)
print(pivot_table3)

