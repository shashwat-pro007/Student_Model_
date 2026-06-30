def transform_data(data):

    def assign_grade(marks):

        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    data["Grade"] = data["Marks"].apply(assign_grade)

    data["Result"] = data["Marks"].apply(
        lambda x: "Pass" if x >= 40 else "Fail"
    )

    data["Performance Score"] = (
        data["Marks"]*0.5 +
        data["Attendance"]*0.3 +
        data["StudyHours"]*2
    )

    return data