"""
Deep Dive - Part 2: Hypothesis Testing
Topic: Common Pitfalls — Seeing p-hacking Happen, Not Just Reading About It

This simulates the "p-hacking" pitfall directly: if you run enough
tests on pure random noise (no real effect at all), roughly alpha
(e.g. 5%) of them will come back "significant" just by chance.

Run this file with:  python 08_pitfalls_multiple_testing_demo.py
"""

import numpy as np
from scipy import stats

np.random.seed(42)

# ---------------------------------------------------------
# 1. Run ONE test on pure random noise
# ---------------------------------------------------------
print("--- A single test on random noise (no real effect exists) ---")
group_a = np.random.normal(loc=50, scale=10, size=30)
group_b = np.random.normal(loc=50, scale=10, size=30)   # same true mean as group_a!

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"p-value: {p_value:.4f}")
print("Both groups were drawn from the SAME distribution -- any 'significant'")
print("result here would be a false positive (Type I error).")

# ---------------------------------------------------------
# 2. Now run MANY tests on random noise and count false positives
# ---------------------------------------------------------
print("\n--- Running 100 tests on random noise ---")
alpha = 0.05
num_tests = 100
significant_count = 0

for i in range(num_tests):
    sample_a = np.random.normal(loc=50, scale=10, size=30)
    sample_b = np.random.normal(loc=50, scale=10, size=30)
    _, p = stats.ttest_ind(sample_a, sample_b)
    if p < alpha:
        significant_count += 1

print(f"Out of {num_tests} tests where NO real effect exists,")
print(f"{significant_count} came back 'statistically significant' at alpha={alpha}.")
print(f"That's a {significant_count / num_tests * 100:.1f}% false positive rate --")
print(f"close to the {alpha * 100:.0f}% we'd expect by definition of alpha.")
print("\nThis is exactly why p-hacking (testing many things until one 'works')")
print("is dangerous: with enough tries, false positives are guaranteed to appear.")

# ---------------------------------------------------------
# 3. The fix: correct for multiple comparisons
# ---------------------------------------------------------
print("\n--- One fix: Bonferroni correction ---")
bonferroni_alpha = alpha / num_tests
print(f"Instead of alpha={alpha}, require p < {bonferroni_alpha:.5f} when running {num_tests} tests.")
print("This keeps the OVERALL false-positive rate across all tests near the original alpha.")

# demonstrate with the same simulated tests
np.random.seed(42)
significant_count_corrected = 0
for i in range(num_tests):
    sample_a = np.random.normal(loc=50, scale=10, size=30)
    sample_b = np.random.normal(loc=50, scale=10, size=30)
    _, p = stats.ttest_ind(sample_a, sample_b)
    if p < bonferroni_alpha:
        significant_count_corrected += 1

print(f"\nWith Bonferroni correction: {significant_count_corrected} out of {num_tests} 'significant'")
print("(much closer to the 0 we'd hope for, since no real effect exists anywhere here)")
