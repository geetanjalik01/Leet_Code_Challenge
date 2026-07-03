import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    result = students.merge(subjects, how="cross")
    counts = (
        examinations.groupby(["student_id", "subject_name"])
        .size()
        .reset_index(name="attended_exams")
    )
    result = result.merge(
        counts,
        on=["student_id", "subject_name"],
        how="left"
    )

    # Fill missing counts with 0
    result["attended_exams"] = result["attended_exams"].fillna(0).astype(int)

    # Return in the required order
    return result.sort_values(
        ["student_id", "subject_name"]
    )[["student_id", "student_name", "subject_name", "attended_exams"]]