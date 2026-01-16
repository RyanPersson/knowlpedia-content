---
title: "Fundamental Theorem of Calculus"
description: "The theorem connecting differentiation and integration as inverse operations."
---

The **Fundamental Theorem of Calculus** establishes the relationship between {{< knowl id="derivative" text="differentiation" >}} and integration.

## First part
If \(f: [a,b] \to \mathbb{R}\) is {{< knowl id="continuous-function" text="continuous" >}}, then the function
$$
F(x) = \int_a^x f(t)\, dt
$$
is an {{< knowl id="antiderivative" text="antiderivative" >}} of \(f\). That is, \(F\) is differentiable on \((a,b)\) and
$$
F'(x) = f(x).
$$

## Second part
If \(f: [a,b] \to \mathbb{R}\) is continuous and \(F\) is any antiderivative of \(f\), then
$$
\int_a^b f(x)\, dx = F(b) - F(a).
$$

## Significance
This theorem shows that differentiation and integration are inverse operations (up to constants), unifying the two main branches of calculus. It provides a practical method for computing definite integrals by finding antiderivatives.

## Extensions
- **Lebesgue's version**: If \(f\) is Lebesgue integrable and \(F(x) = \int_a^x f\, d\mu\), then \(F' = f\) almost everywhere.
- **Multivariable**: Generalizes to {{< knowl id="stokes-theorem" section="differential-geometry" text="Stokes' theorem" >}}.
