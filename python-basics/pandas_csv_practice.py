import pandas as pd
import numpy as np
df = pd.read_csv("qc_results.csv")
new_df = df[df["status"] == "PASS"]
new_df.to_csv("passed_samples.csv", index=False)
print(new_df)
conditions= [df["reads"] >= 2000, df["reads"] >= 1000]
choice = ["HIGH", "MEDIUM"]
df["qc_category"] = np.select(conditions, choice, default = "LOW")
print(df)
