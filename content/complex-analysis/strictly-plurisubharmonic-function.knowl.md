+++
id = "complex-analysis/strictly-plurisubharmonic-function"
title = "Strictly plurisubharmonic function"
kind = "definition"
summary = "A plurisubharmonic function whose Levi form has a locally positive lower bound."
aliases = ["strict plurisubharmonicity", "strictly PSH function"]
domains = ["complex-analysis", "several-complex-variables"]
prerequisites = ["complex-analysis/levi-form"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A \(C^2\) function \(\phi\) on \(U\subseteq\mathbb C^d\) is **strictly
plurisubharmonic** if its [[complex-analysis/levi-form|Levi form]] is positive
definite at every point. Quantitatively, one often assumes
\[
\mathcal L_\phi(z;v)\ge\kappa(z)|v|^2
\]
for a positive function \(\kappa\).

## Nonsmooth convention

For an [[complex-analysis/upper-semicontinuous-function|upper-semicontinuous function]], strict plurisubharmonicity may be defined
locally by requiring \(\phi-\varepsilon|z|^2\) to be
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]] for some
\(\varepsilon>0\). Distributional inequalities permit measurable lower bounds
\(\kappa\).

## Role in the d-bar equation

The positive lower bound supplies coercivity in the
[[complex-analysis/hormander-l2-dbar-theorem|Hörmander \(L^2\)
\(\bar\partial\)-existence theorem]], controlling a solution by the data divided
by \(\kappa\).

## References

1. Lars Hörmander, *An Introduction to Complex Analysis in Several Variables*, 3rd ed., North-Holland, 1990.
