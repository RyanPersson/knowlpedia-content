+++
id = "algebraic-geometry-foundations/algebraically-closed-field"
title = "Algebraically closed field"
kind = "definition"
summary = "A field in which every nonconstant one-variable polynomial has a root."
aliases = ["algebraically closed field", "algebraically closed"]
domains = ["algebraic-geometry-foundations"]
+++

A [[algebra-rings/field|field]] $k$ is **algebraically closed** if every nonconstant polynomial $f(x)\in k[x]$ has a root in $k$. Equivalently, every nonconstant polynomial factors completely into linear factors:

$$
f(x)=c\prod_{i=1}^n(x-a_i),
\qquad c,a_i\in k,
$$

or, equivalently, $k$ has no proper finite algebraic field extension. An [[algebra-fields-galois/algebraic-closure|algebraic closure]] of a field $F$ is an algebraic extension $\overline F/F$ whose field $\overline F$ is algebraically closed.

Standard examples include $\mathbb C$ and $\overline{\mathbb F}_p$; neither $\mathbb R$ nor a finite field is algebraically closed.

## Remarks

Algebraic closedness concerns polynomial equations, not topological closedness or metric completeness.
