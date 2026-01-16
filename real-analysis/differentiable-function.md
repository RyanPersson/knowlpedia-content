---
title: "Differentiable function"
description: "A function that has a derivative at every point of its domain."
---

A function \(f: U \to \mathbb{R}\) on an open set \(U \subseteq \mathbb{R}\) is **differentiable** if it is {{< knowl id="differentiability-one-variable" text="differentiable at every point" >}} of \(U\).

## Single variable
A function \(f: (a,b) \to \mathbb{R}\) is differentiable at \(x_0\) if the limit
$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$
exists. The function \(f': (a,b) \to \mathbb{R}\) is the {{< knowl id="derivative" text="derivative" >}} of \(f\).

## Multivariable
A function \(f: U \to \mathbb{R}^m\) on open \(U \subseteq \mathbb{R}^n\) is differentiable at \(a \in U\) if there exists a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} \(Df(a): \mathbb{R}^n \to \mathbb{R}^m\) such that
$$
\lim_{h \to 0} \frac{\|f(a + h) - f(a) - Df(a)h\|}{\|h\|} = 0.
$$

## Properties
- Differentiability implies {{< knowl id="continuous-function" text="continuity" >}} (but not conversely).
- Sums, products, and compositions of differentiable functions are differentiable (chain rule).
- {{< knowl id="mean-value-theorem" text="Mean value theorem" >}} relates the derivative to finite differences.
