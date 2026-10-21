import pandas as pd
import numpy as np

def validate_input(data):
    invalid_rows = data[
        data.isna().any(axis=1)
        | (data["reads"] < 0)
        | (data["mean_depth"] < 0)
        | (~data["status"].isin(["PASS", "FAIL"]))
        | (data["sample"].duplicated(keep=False))
    ]

    return invalid_rows
def build_report(data):
    data = data.copy()

    conditions = [
        (data["reads"] >= 2000) & (data["mean_depth"] >= 40),
        (data["reads"] >= 1000) & (data["mean_depth"] >= 25)
    ]
    choices = ["HIGH", "MEDIUM"]

    data["qc_categories"] = np.select(
        conditions, choices, default="LOW"
    )

    batch_summary = pd.pivot_table(
        data,
        values="reads",
        index="batch",
        columns="qc_categories",
        aggfunc="count",
        fill_value=0
    )

    batch_matrix = data.groupby("batch").agg(
        average_reads=("reads", "mean"),
        average_depth=("mean_depth", "mean")
    )

    batch_summary = batch_summary.reset_index()
    batch_matrix = batch_matrix.reset_index()

    final_matrix = pd.merge(
        batch_summary, batch_matrix, on="batch"
    )

    pass_count = (
        data[data["status"] == "PASS"]
        .groupby("batch")["sample"]
        .count()
    )
    total_count = data.groupby("batch")["sample"].count()
    pass_rate = (pass_count / total_count) * 100

    pass_rate_df = pass_rate.reset_index()
    pass_rate_df.columns = ["batch", "pass_percent"]

    final_matrix = pd.merge(
        final_matrix, pass_rate_df, on="batch"
    )

    final_matrix["average_reads"] = (
        final_matrix["average_reads"].round(2)
    )
    final_matrix["average_depth"] = (
        final_matrix["average_depth"].round(2)
    )
    final_matrix["pass_percent"] = (
        final_matrix["pass_percent"].round(2)
    )

    return final_matrix

def save_report(report, output_path):
    report.to_csv(output_path, index=False)

def main():
    df = pd.read_csv("ngs_qc.csv")

    invalid_val = validate_input(df)

    if not invalid_val.empty:
        print("Input validation failed!")
        print(invalid_val)
        raise SystemExit("Stopping QC report generation.")

    print("Input validation passed!")

    final_matrix = build_report(df)

    output_path = "ngs_final_qc_report.csv"
    save_report(final_matrix, output_path)

    print("\nFinal batch QC report:")
    print(final_matrix.to_string(index=False))
    print(f"\nReport saved to {output_path}")


if __name__ == "__main__":
    main()

#df=pd.read_csv("ngs_qc.csv")

#print(df)
#print(df.shape)
#df.info()
#print(df.isna().sum())
#print(df[df["reads"] < 0])
#print(df[df["mean_depth"] < 0])
#print(df[~df["status"].isin(["PASS","FAIL"])])
#print(df["sample"].duplicated().sum())
#print(df[df["sample"].duplicated(keep=False)])

#invalid_val = validate_input(df)

#invalid_val=df[df.isna().any(axis=1) | (df["reads"] < 0) | (df["mean_depth"] < 0)| (~df["status"].isin(["PASS", "FAIL"]))| (df["sample"].duplicated(keep=False))]
#if not invalid_val.empty:
#    print("Input validation failed!")
#    print(invalid_val)
#    raise SystemExit("Stopping QC report generation.")
#
#print("Input validation passed!")

#final_matrix = build_report(df)

#conditions = [(df["reads"] >= 2000) & (df["mean_depth"] >= 40), (df["reads"] >= 1000) & (df["mean_depth"] >= 25)]
#choices = ("HIGH", "MEDIUM")
#df["qc_categories"] = np.select(conditions, choices, default="LOW")
##print(df)
#batch_summary = pd.pivot_table(df, values="reads", index="batch", columns="qc_categories", aggfunc="count", fill_value=0)
##print(batch_summary)
#batch_matrix = df.groupby("batch").agg(average_reads=("reads", "mean"), average_depth=("mean_depth", "mean"))
##print(batch_matrix)
#batch_summary = batch_summary.reset_index()
#batch_matrix = batch_matrix.reset_index()
#final_matrix = pd.merge(batch_summary,batch_matrix, on="batch")
##print(final_matrix)
#pass_count = df[df["status"] == "PASS"].groupby("batch")["sample"].count()
#total_count = df.groupby("batch")["sample"].count()
#pass_rate = (pass_count / total_count) * 100
##print(pass_count)
##print(total_count)
##print(pass_rate)
#pass_rate_df = pass_rate.reset_index()
#pass_rate_df.columns = ["batch", "pass_percent"]
#final_matrix = pd.merge(final_matrix, pass_rate_df, on="batch")
##print(final_matrix)
#final_matrix["average_reads"] = final_matrix["average_reads"].round(2)
#final_matrix["average_depth"] = final_matrix["average_depth"].round(2)
#final_matrix["pass_percent"] = final_matrix["pass_percent"].round(2)
##print(final_matrix)

#save_report(final_matrix, "ngs_final_qc_report.csv")

#final_matrix.to_csv("ngs_final_qc_report.csv", index=False)

#print("\nFinal batch QC report:")
#print(final_matrix.to_string(index=False))
#print("\nReport saved to ngs_final_qc_report.csv")
