import pandas as pd


def clean_data(data):

    print("\nMissing Values:")
    print(data.isnull().sum())

    print("\nDuplicate Records:")
    print(data.duplicated().sum())

    data = data.drop_duplicates()


    data["StudyHours"] = data["StudyHours"].fillna(
        data["StudyHours"].mean()
    )
    data["Attendance"] = data["Attendance"].fillna(
        data["Attendance"].mean()
    )

    data["Marks"] = data["Marks"].fillna(
        data["Marks"].mean()
    )

    data = data[
        (data["Attendance"] >= 0) &
        (data["Attendance"] <= 100)
    ]


    data = data[
        (data["Marks"] >= 0) &
        (data["Marks"] <= 100)
    ]


    data = data[
        data["StudyHours"] >= 0
    ]


    data.to_csv(
        "output/cleaned_data.csv",
        index=False
    )


    return data