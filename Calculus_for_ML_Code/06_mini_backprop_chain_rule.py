"""
Calculus for ML - Part 5: Chain Rule -> Backpropagation
Topic: A Tiny 2-Layer Network, Trained by Hand With the Chain Rule

This builds the smallest possible "neural network" -- two layers,
one input, one weight per layer -- and trains it using nothing but
plain Python and the chain rule. No frameworks, no autograd: this
IS what those frameworks are doing under the hood.

Run this file with:  python 06_mini_backprop_chain_rule.py
"""


def sigmoid(z):
    return 1 / (1 + 2.718281828 ** (-z))


def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)


# ---------------------------------------------------------
# The tiny network:
#   input x -> [* w1] -> a -> [sigmoid] -> h -> [* w2] -> y_hat
#   loss = (y_true - y_hat)^2
# ---------------------------------------------------------
def forward(x, w1, w2):
    a = x * w1                 # layer 1: linear
    h = sigmoid(a)              # layer 1: activation
    y_hat = h * w2               # layer 2: linear (output)
    return a, h, y_hat


def compute_loss(y_hat, y_true):
    return (y_true - y_hat) ** 2


def backward(x, w1, w2, a, h, y_hat, y_true):
    """Compute d(loss)/d(w1) and d(loss)/d(w2) via the chain rule,
    walking backward through the exact same steps forward() took."""

    # d(loss)/d(y_hat) -- loss = (y_true - y_hat)^2
    d_loss_d_yhat = -2 * (y_true - y_hat)

    # d(y_hat)/d(w2) -- y_hat = h * w2
    d_yhat_d_w2 = h
    # chain rule: d(loss)/d(w2) = d(loss)/d(y_hat) * d(y_hat)/d(w2)
    d_loss_d_w2 = d_loss_d_yhat * d_yhat_d_w2

    # d(y_hat)/d(h) -- y_hat = h * w2
    d_yhat_d_h = w2
    # d(h)/d(a) -- h = sigmoid(a)
    d_h_d_a = sigmoid_derivative(a)
    # d(a)/d(w1) -- a = x * w1
    d_a_d_w1 = x
    # chain rule, chained through THREE steps this time:
    # d(loss)/d(w1) = d(loss)/d(y_hat) * d(y_hat)/d(h) * d(h)/d(a) * d(a)/d(w1)
    d_loss_d_w1 = d_loss_d_yhat * d_yhat_d_h * d_h_d_a * d_a_d_w1

    return d_loss_d_w1, d_loss_d_w2


# ---------------------------------------------------------
# Train the tiny network on a single example
# ---------------------------------------------------------
print("--- Training a 2-layer network by hand with the chain rule ---")
x = 1.5
y_true = 0.8

w1, w2 = 0.5, 0.5    # initial weights
learning_rate = 0.5

for epoch in range(10):
    a, h, y_hat = forward(x, w1, w2)
    loss = compute_loss(y_hat, y_true)

    d_loss_d_w1, d_loss_d_w2 = backward(x, w1, w2, a, h, y_hat, y_true)

    w1 = w1 - learning_rate * d_loss_d_w1
    w2 = w2 - learning_rate * d_loss_d_w2

    print(f"epoch {epoch}: loss={loss:.5f}, y_hat={y_hat:.4f}, "
          f"w1={w1:.4f}, w2={w2:.4f}")

print(f"\nTarget was y_true={y_true}. Final prediction: {forward(x, w1, w2)[2]:.4f}")
print("\nEvery weight update above came from chaining local derivatives")
print("together -- exactly the chain rule from the earlier examples,")
print("just applied through more steps. This IS backpropagation.")
