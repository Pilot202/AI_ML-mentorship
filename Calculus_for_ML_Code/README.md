# Calculus for Machine Learning — Code

Companion code for `Calculus_for_ML_DeepDive.pptx` and
`Calculus_for_ML_Explained.pdf`.
Part of the 3-Month Machine Learning Mentorship Program (Week 3, Tuesday).

## Files

| File | Topic |
|---|---|
| `01_derivatives_basics.py` | Core derivative rules, symbolic vs. numerical (finite difference) derivatives |
| `02_derivative_loss_function_example.py` | Worked ML example: the derivative of a squared-error loss |
| `03_gradients_partial_derivatives.py` | Partial derivatives, the gradient vector, using it in an update step |
| `04_chain_rule.py` | Chain rule on nested functions, plus a manual multi-step chain |
| `05_gradient_descent_from_scratch.py` | 1D and 2D gradient descent, and what happens with a bad learning rate |
| `06_mini_backprop_chain_rule.py` | A tiny 2-layer network trained by hand using nothing but the chain rule |

## Setup

```bash
pip install numpy sympy
pip freeze > requirements.txt
```

## Running the examples

```bash
python 01_derivatives_basics.py
python 02_derivative_loss_function_example.py
python 03_gradients_partial_derivatives.py
python 04_chain_rule.py
python 05_gradient_descent_from_scratch.py
python 06_mini_backprop_chain_rule.py
```

## Suggested order

Work through them in numeric order — each one builds on the last:
derivatives → gradients → chain rule → optimization → and finally
`06`, which ties everything together into a working (tiny) neural
network trained entirely by hand.

## The big idea

Every file in this folder is really demonstrating one thing from a
different angle: **a derivative tells you which way to nudge a
number to make some output smaller.** Gradients extend that to many
numbers at once. The chain rule lets that nudge propagate through
layers of nested computation. Put them together and you have exactly
what `06` shows — a trainable model, built from first principles.
