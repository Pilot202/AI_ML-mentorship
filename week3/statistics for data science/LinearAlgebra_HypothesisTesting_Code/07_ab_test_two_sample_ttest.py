"""
Deep Dive - Part 2: Hypothesis Testing
Topic: Worked Example — A/B Test with a Two-Sample t-test

Run this file with:  python 07_ab_test_two_sample_ttest.py
"""

import numpy as np
from scipy import stats

# ---------------------------------------------------------
# Scenario: does Teaching Method B produce higher scores
# than Teaching Method A?
# ---------------------------------------------------------
print("--- A/B Test: Method A vs. Method B ---")
group_a = np.array([65, 70, 68, 72, 66, 71, 69, 67])   # Method A scores
group_b = np.array([75, 78, 80, 74, 77, 82, 76, 79])   # Method B scores

print(f"Method A scores: {group_a}")
print(f"Method B scores: {group_b}")
print(f"\nMean A: {group_a.mean():.2f}")
print(f"Mean B: {group_b.mean():.2f}")
print(f"Difference: {group_b.mean() - group_a.mean():.2f}")

# H0: no difference in mean scores between methods
# H1: there IS a difference in mean scores
t_statistic, p_value = stats.ttest_ind(group_a, group_b)

print(f"\nt-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.6f}")

alpha = 0.05
print(f"\nSignificance level (alpha): {alpha}")
if p_value < alpha:
    print("Reject H0 -- Method B likely performs differently from Method A")
else:
    print("Fail to reject H0 -- not enough evidence of a real difference")

# ---------------------------------------------------------
# Effect size: statistical significance isn't the whole story
# ---------------------------------------------------------
print("\n--- Effect size (Cohen's d) ---")


def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    pooled_std = np.sqrt(
        ((n1 - 1) * group1.var(ddof=1) + (n2 - 1) * group2.var(ddof=1)) / (n1 + n2 - 2)
    )
    return (group2.mean() - group1.mean()) / pooled_std


d = cohens_d(group_a, group_b)
print(f"Cohen's d: {d:.3f}")
print("Rule of thumb: 0.2 = small, 0.5 = medium, 0.8+ = large effect")
print("A statistically significant result with a tiny effect size may not be practically meaningful.")

# ---------------------------------------------------------
# Checking the assumption of equal variances (optional detail)
# ---------------------------------------------------------
print("\n--- Checking equal-variance assumption (Levene's test) ---")
levene_stat, levene_p = stats.levene(group_a, group_b)
print(f"Levene's test p-value: {levene_p:.4f}")
if levene_p < 0.05:
    print("Variances are significantly different -- consider Welch's t-test instead:")
    t_stat_welch, p_welch = stats.ttest_ind(group_a, group_b, equal_var=False)
    print(f"Welch's t-test p-value: {p_welch:.6f}")
else:
    print("Variances look similar enough -- the standard t-test above is appropriate.")
