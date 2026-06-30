import pandas as pd
def generate_report(data):

    report = {

        "Total Students":
        len(data),

        "Passed Students":
        len(data[data["Result"]=="Pass"]),

        "Failed Students":
        len(data[data["Result"]=="Fail"]),

        "Highest Marks":
        data["Marks"].max(),

        "Lowest Marks":
        data["Marks"].min(),

        "Average Marks":
        data["Marks"].mean(),

        "Average Attendance":
        data["Attendance"].mean()

    }

    report_df = pd.DataFrame(
        report.items(),
        columns=["Parameter","Value"]
    )

    report_df.to_csv(
        "output/report.csv",
        index=False
    )

    toppers = data.sort_values(
        by="Performance Score",
        ascending=False
    ).head(10)

    toppers.to_csv(
        "output/toppers.csv",
        index=False
    )

    failed = data[
        data["Result"]=="Fail"
    ]

    failed.to_csv(
        "output/failed_students.csv",
        index=False
    )
    print("\nReport Generated Successfully")