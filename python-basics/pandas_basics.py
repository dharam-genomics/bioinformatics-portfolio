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
