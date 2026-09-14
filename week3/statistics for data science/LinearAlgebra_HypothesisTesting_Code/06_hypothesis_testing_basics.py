"""
Deep Dive - Part 2: Hypothesis Testing
Topic: The Basics — one-sample t-test

Run this file with:  python 06_hypothesis_testing_basics.py
"""

import numpy as np
from scipy import stats

# ---------------------------------------------------------
# Scenario: a class average is claimed to be 70. Is a sample
# of actual scores significantly different from that claim?
# ---------------------------------------------------------
print("--- One-sample t-test ---")
scores = np.array([72, 68, 75, 65, 71, 69, 74, 77, 66, 73])
claimed_mean = 70

print(f"Sample scores: {scores}")
print(f"Sample mean: {scores.mean():.2f}")
print(f"Claimed population mean: {claimed_mean}")

# H0: the true mean score is 70 (no difference from the claim)
# H1: the true mean score is NOT 70
t_statistic, p_value = stats.ttest_1samp(scores, claimed_mean)

print(f"\nt-statistic: {t_statistic:.4f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05
print(f"\nSignificance level (alpha): {alpha}")
if p_value < alpha:
    print("Reject H0 -- the sample mean is significantly different from 70")
else:
    print("Fail to reject H0 -- not enough evidence the mean differs from 70")

# ---------------------------------------------------------
# What the p-value actually means here
# ---------------------------------------------------------
print("\n--- Interpreting the p-value ---")
print(
    f"A p-value of {p_value:.4f} means: if the true mean really were {claimed_mean},\n"
    f"there'd be about a {p_value * 100:.1f}% chance of seeing a sample mean at least\n"
    f"this far from {claimed_mean} just by random sampling variation."
)

# ---------------------------------------------------------
# One-sided vs. two-sided testing (a common source of confusion)
# ---------------------------------------------------------
print("\n--- One-sided test example ---")
# Sometimes you only care whether scores are HIGHER than claimed,
# not just "different". scipy's ttest_1samp is two-sided by default;
# halve the p-value for a one-sided test in the direction you expect
# (only valid when the result is in that direction).
if scores.mean() > claimed_mean:
    one_sided_p = p_value / 2
    print(f"One-sided p-value (testing if mean > {claimed_mean}): {one_sided_p:.4f}")
else:
    print("Sample mean is not above the claimed mean, so a one-sided 'greater than' test doesn't apply here.")
