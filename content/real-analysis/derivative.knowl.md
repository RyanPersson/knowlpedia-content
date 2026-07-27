+++
id = "real-analysis/derivative"
title = "Derivative"
kind = "knowl"
summary = "The limit of a function's difference quotient at an interior point."
aliases = ["derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/derivative.md"
+++

A [[shared-foundations/function|function]] $f:I\to\mathbb R$, defined on an open interval $I$, is **differentiable at** $a\in I$ if the finite limit
$$
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}
$$
exists. The number $f'(a)$ is the **derivative of $f$ at $a$**.

## Remarks

This is a special instance of a [[real-analysis/limit-at-a-point|limit at a point]] applied to the difference quotient. Existence of the derivative is the basic notion behind [[real-analysis/differentiability-1d|differentiability in one variable]], and it implies continuity via [[real-analysis/differentiability-implies-continuity|differentiability implies continuity]].
