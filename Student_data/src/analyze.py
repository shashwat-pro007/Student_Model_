def analyze_data(data):

    print("\nAverage Marks:",
          data["Marks"].mean())

    print("\nHighest Marks:",
          data["Marks"].max())

    print("\nLowest Marks:",
          data["Marks"].min())

    print("\nAverage Attendance:",
          data["Attendance"].mean())

    print("\nAverage Study Hours:",
          data["StudyHours"].mean())

    total = len(data)

    passed = len(
        data[data["Result"]=="Pass"]
    )

    failed = len(
        data[data["Result"]=="Fail"]
    )

    print("\nPass Percentage:",
          (passed/total)*100)

    print("\nFail Percentage:",
          (failed/total)*100)

    print("\nGrade Distribution")

    print(
        data["Grade"].value_counts()
    )

    print("\nStatistics")

    print(data.describe())


    print("\nCorrelation")

    print(
        data.corr(numeric_only=True)
    )