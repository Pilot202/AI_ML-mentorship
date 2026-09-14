"""
Week 2 - Thursday Session
Practice Project: Dataset Explorer

This mini project ties together everything from Week 2:
  - NumPy         (summary statistics)
  - Pandas        (loading, cleaning, grouping)
  - Visualization (saving a summary chart)

Run this file with:  python 07_mini_project_dataset_explorer.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_sample_dataset(filename="scores_raw.csv"):
    """Create a small, deliberately messy CSV to practice on."""
    data = {
        "name": ["Ada", "Chidi", "Ngozi", "Tunde", "Bisi", "Femi", "Ada", "Kemi"],
        "subject": ["Math", "Math", "Science", "Science", "Math", "Science", "Math", "English"],
        "grade": [85, 60, 95, None, 78, 88, 85, 72],  # includes a missing value
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return filename


def load_data(filename):
    """Step 1: Load the CSV."""
    print(f"--- Step 1: Loading {filename} ---")
    df = pd.read_csv(filename)
    print(df)
    return df


def clean_data(df):
    """Step 2: Clean missing values and duplicate rows."""
    print("\n--- Step 2: Cleaning data ---")
    print("Missing values per column:")
    print(df.isnull().sum())

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"\nRemoved {before - after} duplicate row(s)")

    # Fill missing grades with the subject's average rather than dropping
    df["grade"] = df.groupby("subject")["grade"].transform(
        lambda g: g.fillna(g.mean())
    )
    print("\nCleaned data:")
    print(df)
    return df


def compute_stats(df):
    """Step 3: Compute summary statistics with NumPy/Pandas."""
    print("\n--- Step 3: Summary statistics ---")
    grades = df["grade"].to_numpy()
    print(f"Mean:   {np.mean(grades):.1f}")
    print(f"Median: {np.median(grades):.1f}")
    print(f"Min:    {np.min(grades):.1f}")
    print(f"Max:    {np.max(grades):.1f}")
    print(f"Std dev: {np.std(grades):.1f}")


def group_and_aggregate(df):
    """Step 4: Group and aggregate by subject."""
    print("\n--- Step 4: Group by subject ---")
    summary = df.groupby("subject")["grade"].agg(["mean", "min", "max", "count"])
    print(summary)
    return summary


def visualize(summary, output="subject_summary.png"):
    """Step 5: Visualize and save a chart of the findings."""
    print(f"\n--- Step 5: Saving chart to {output} ---")
    plt.figure(figsize=(6, 4))
    summary["mean"].plot(kind="bar", color="#2E86AB")
    plt.title("Average Grade by Subject")
    plt.ylabel("Average Grade")
    plt.xlabel("Subject")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()
    print(f"Saved {output}")


def main():
    filename = create_sample_dataset()
    df = load_data(filename)
    df = clean_data(df)
    compute_stats(df)
    summary = group_and_aggregate(df)
    visualize(summary)
    print("\nDone! Open subject_summary.png to see the final chart.")


if __name__ == "__main__":
    main()
