"""
Introduction to Machine Learning & AI
Companion demo: "Teaching a Model to Learn"

This is the exact example from the slide deck, runnable on its own.
No external libraries needed — pure Python.

Run with:  python ml_concept_demo.py

The idea: the true relationship is y = 2x + 1, but the "model" below
is never told that formula. It only sees example (x, y) pairs and
nudges its own guess a little closer after each one. That repeated
nudging process is what "training" means in machine learning.
"""

# The model starts with a random (here, zero) guess for the pattern.
weight, bias = 0.0, 0.0

# Training examples: pairs of (x, y) where the true rule is y = 2x + 1
examples = [(1, 3), (2, 5), (3, 7), (4, 9)]

LEARNING_RATE = 0.01
EPOCHS = 1000

print("--- Training ---")
print(f"Starting guess: y = {weight:.2f}x + {bias:.2f}\n")

for epoch in range(EPOCHS):
    for x, y_actual in examples:
        y_predicted = weight * x + bias
        error = y_actual - y_predicted

        # Nudge the guess a little closer to correct.
        # This is a tiny, from-scratch version of gradient descent.
        weight += LEARNING_RATE * error * x
        bias += LEARNING_RATE * error

    # Print progress every 200 epochs so you can watch it converge
    if (epoch + 1) % 200 == 0:
        print(f"After {epoch + 1:>4} epochs: y = {weight:.3f}x + {bias:.3f}")

print(f"\nFinal learned rule: y = {weight:.2f}x + {bias:.2f}")
print("The true rule was:  y = 2.00x + 1.00")
print("\nThe model was never given the formula — it only ever saw")
print("(x, y) example pairs and adjusted itself after each one.")

# ---------------------------------------------------------
# Try it on a new, unseen input — this is a "prediction"
# ---------------------------------------------------------
print("\n--- Using the trained model ---")
new_x = 10
prediction = weight * new_x + bias
print(f"For x = {new_x}, the model predicts y = {prediction:.2f}")
print(f"(the true rule would give y = {2 * new_x + 1})")
