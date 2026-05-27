import pandas as pd
from typing import Dict, Tuple

FILE_PATH = "dummy_updated_with_values.xlsx"
SHEET_NAME = "Sheet1"

CRITICAL_THRESHOLDS: Dict[str, Tuple[float, float]] = {
    "Potassium": (3.5, 5.0),
    "Glucose": (70, 100),
    "Heart Rate": (60, 100),
    "Lactate": (0.0, 2.0)
}

ADMISSION_PRIORITY = {
    "Emergency": 3,
    "Urgent": 2,
    "Elective": 1
}

def load_data(file_path: str, sheet_name: str) -> pd.DataFrame:
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print("Data loaded successfully.")
        return df

    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()

    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def flag_critical_results(df: pd.DataFrame,
                          thresholds: Dict[str, Tuple[float, float]]) -> pd.DataFrame:
    

    flagged_results = []

    for _, row in df.iterrows():

        for test, (low, high) in thresholds.items():

            if test in df.columns:

                value = row[test]

                if pd.notna(value) and (value < low or value > high):

                    flagged_results.append({
                        "Patient ID": row["Patient ID"],
                        "Name": row.get("Name", "Unknown"),
                        "Test": test,
                        "Value": value,
                        "Normal Range": f"{low}-{high}"
                    })

    flagged_df = pd.DataFrame(flagged_results)

    if flagged_df.empty:
        print("No critical results found.")
    else:
        print(f"{len(flagged_df)} critical results flagged.")

    return flagged_df


def calculate_priority_score(row: pd.Series) -> int:
    

    score = 0

    score += ADMISSION_PRIORITY.get(row.get("Admission Type"), 0) * 10

    
    if row.get("Sepsis") == "Yes":
        score += 15

    
    if row.get("Heart Rate", 0) < 60 or row.get("Heart Rate", 0) > 100:
        score += 5

    if row.get("Glucose", 0) < 70 or row.get("Glucose", 0) > 140:
        score += 5

    if row.get("Potassium", 0) < 3.5 or row.get("Potassium", 0) > 5.2:
        score += 5

    if row.get("Lactate", 0) > 2.0:
        score += 5

    return score


def assign_priority_scores(df: pd.DataFrame) -> pd.DataFrame:
   

    df["Priority Score"] = df.apply(calculate_priority_score, axis=1)

    df_sorted = df.sort_values(
        by="Priority Score",
        ascending=False
    )

    print("Priority scores assigned.")

    return df_sorted



def generate_summary(flagged_df: pd.DataFrame) -> str:
   

    if flagged_df.empty:
        return "All patients are within safe clinical limits."

    summary = "Critical Findings Summary:\n"

    for _, row in flagged_df.iterrows():
        summary += (
            f"Patient {row['Patient ID']} "
            f"has abnormal {row['Test']} value "
            f"({row['Value']} vs normal {row['Normal Range']}).\n"
        )

    return summary



def main():

    df = load_data(FILE_PATH, SHEET_NAME)

    if df.empty:
        return

    
    required_columns = [
        "Patient ID",
        "Name",
        "Medical Condition",
        "Admission Type",
        "Sepsis",
        "Potassium",
        "Glucose",
        "Heart Rate",
        "Lactate"
    ]

    df = df[required_columns].dropna()

    flagged_df = flag_critical_results(df, CRITICAL_THRESHOLDS)

   
    prioritized_df = assign_priority_scores(df)

  
    print("\nTop High Priority Patients:")
    print(prioritized_df.head(10))

   
    summary = generate_summary(flagged_df)

    print("\nSummary Report:")
    print(summary)


# Entry point
if __name__ == "__main__":
    main()
