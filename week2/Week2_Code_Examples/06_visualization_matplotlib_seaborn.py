"""
Week 2 - Thursday Session
Topic: Data Visualization with Matplotlib & Seaborn

Run this file with:  python 06_visualization_matplotlib_seaborn.py

This saves a few chart images into the same folder so you can open
and inspect them after running the script (useful since these run
without a graphical display in many environments).
"""

import matplotlib
matplotlib.use("Agg")  # renders to a file instead of a pop-up window
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "name": ["Ada", "Chidi", "Ngozi", "Tunde", "Bisi", "Femi"],
    "subject": ["Math", "Math", "Science", "Science", "Math", "Science"],
    "grade": [85, 60, 95, 45, 78, 88],
})

# ---------------------------------------------------------
# 1. A basic bar chart with Matplotlib
# ---------------------------------------------------------
print("--- Creating bar chart (Matplotlib) ---")
avg_by_subject = df.groupby("subject")["grade"].mean()

plt.figure(figsize=(6, 4))
avg_by_subject.plot(kind="bar", color="#2E86AB")
plt.title("Average Grade by Subject")
plt.ylabel("Grade")
plt.xlabel("Subject")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("avg_by_subject.png")
plt.close()
print("Saved avg_by_subject.png")

# ---------------------------------------------------------
# 2. A line chart showing a trend over time
# ---------------------------------------------------------
print("\n--- Creating line chart (Matplotlib) ---")
weeks = [1, 2, 3, 4, 5]
scores = [65, 70, 68, 75, 82]

plt.figure(figsize=(6, 4))
plt.plot(weeks, scores, marker="o", color="#1B4B6B")
plt.title("Ada's Score Trend Over 5 Weeks")
plt.xlabel("Week")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("score_trend.png")
plt.close()
print("Saved score_trend.png")

# ---------------------------------------------------------
# 3. A statistical plot with Seaborn
# ---------------------------------------------------------
print("\n--- Creating box plot (Seaborn) ---")
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="subject", y="grade")
plt.title("Grade Distribution by Subject")
plt.tight_layout()
plt.savefig("grade_boxplot.png")
plt.close()
print("Saved grade_boxplot.png")

# ---------------------------------------------------------
# 4. A scatter plot
# ---------------------------------------------------------
print("\n--- Creating scatter plot (Matplotlib) ---")
study_hours = [2, 5, 1, 6, 3, 4]
plt.figure(figsize=(6, 4))
plt.scatter(study_hours, df["grade"], color="#FFD43B", edgecolor="#1B4B6B", s=100)
plt.title("Study Hours vs. Grade")
plt.xlabel("Study Hours")
plt.ylabel("Grade")
plt.tight_layout()
plt.savefig("study_vs_grade.png")
plt.close()
print("Saved study_vs_grade.png")

print("\nAll charts saved. Open the .png files in this folder to view them.")
