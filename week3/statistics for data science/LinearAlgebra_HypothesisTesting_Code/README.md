# Deep Dive — Linear Algebra & Hypothesis Testing

Companion code for the slide deck `LinearAlgebra_HypothesisTesting_DeepDive.pptx`.
Part of the 3-Month Machine Learning Mentorship Program (supplements Week 3).

## Files

### Part 1: Linear Algebra

| File | Topic |
|---|---|
| `01_vectors.py` | Creating vectors, addition, scalar multiplication, magnitude, unit vectors |
| `02_matrices.py` | Matrix types (identity, zero, diagonal), transpose, matrix multiplication |
| `03_dot_product_deep_dive.py` | Algebraic vs. geometric dot product, orthogonality, ML connections (neurons, cosine similarity) |
| `04_eigenvalues_eigenvectors.py` | Solving the characteristic equation symbolically (sympy) and numerically (NumPy), verifying Av = λv |
| `05_pca_with_eigenvectors.py` | PCA built from scratch using eigen-decomposition, checked against scikit-learn |

### Part 2: Hypothesis Testing

| File | Topic |
|---|---|
| `06_hypothesis_testing_basics.py` | One-sample t-test, interpreting the p-value, one-sided vs. two-sided tests |
| `07_ab_test_two_sample_ttest.py` | Two-sample t-test A/B test, effect size (Cohen's d), checking test assumptions |
| `08_pitfalls_multiple_testing_demo.py` | A live simulation showing false positives accumulate when p-hacking, plus the Bonferroni fix |

## Setup

```bash
pip install numpy scipy sympy scikit-learn
pip freeze > requirements.txt
```

## Running the examples

Each file is self-contained and runnable on its own:

```bash
python 01_vectors.py
python 02_matrices.py
python 03_dot_product_deep_dive.py
python 04_eigenvalues_eigenvectors.py
python 05_pca_with_eigenvectors.py
python 06_hypothesis_testing_basics.py
python 07_ab_test_two_sample_ttest.py
python 08_pitfalls_multiple_testing_demo.py
```

## Why these two topics are paired

Linear algebra gives you the language to represent and compute with
data (vectors, matrices, transformations). Hypothesis testing gives
you a disciplined way to decide whether a pattern in that data is
real or just noise. Every later week in the program leans on both:
neural networks are built from matrix multiplication and dot
products; comparing model versions or A/B testing a deployed feature
uses exactly the hypothesis-testing framework in `07` and `08`.

## Suggested extension

Try applying `07_ab_test_two_sample_ttest.py`'s pattern to real data:
swap in scores from two different study techniques, two model
versions' accuracy across cross-validation folds, or before/after
results from a real intervention.
