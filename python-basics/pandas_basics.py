import pandas as pd

data = {
    "sample": ["sample1", "sample2", "sample3"],
    "reads": [1000, 500, 2500],
    "status": ["PASS", "FAIL", "PASS"]
}

df = pd.DataFrame(data)

print(df)
print("Shape:")
print(df.shape)

print("\nFirst rows:")
print(df.head())

print("\nInformation:")
df.info()

print("\nStatistics:")
print(df.describe())

df = pd.DataFrame({
    "sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "batch": ["B1", "B1", "B2", "B2", "B3", "B3"],
    "reads": [800, 1500, 2200, 500, 3000, 1200],
    "status": ["FAIL", "PASS", "PASS", "FAIL", "PASS", "PASS"]
})

print(df)
qc_summary = df[df["status"] == "PASS"].groupby("batch").agg(average_reads =("reads", "mean"), maximum_reads=("reads", "max"), pass_samples=("reads", "count")).sort_values("average_reads", ascending=False)
#To add a column as index at the end 
#qc_summary["index"] = range(1, len(qc_summary) + 1)
#to add the column with sr_num in the 1st column
qc_summary.insert(0, "sr_num", range(1, len(qc_summary) + 1))
print(qc_summary)
