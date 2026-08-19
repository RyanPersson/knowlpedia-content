+++
id = "complex-analysis/plurisubharmonic-function"
title = "Plurisubharmonic function"
kind = "definition"
summary = "An upper-semicontinuous function whose restriction to every affine complex line is subharmonic."
aliases = ["PSH function", "plurisubharmonicity"]
domains = ["complex-analysis", "several-complex-variables", "potential-theory"]
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb C^d\) be open. A function
\(u:U\to[-\infty,\infty\)) is **plurisubharmonic** if it is
[[complex-analysis/upper-semicontinuous-function|upper-semicontinuous]] and,
for every affine complex line \(L\\), the restriction \(u|_{U\cap L}\) is
[[complex-analysis/subharmonic-function|subharmonic]] or identically
\(-\infty\) on each component.

## Smooth criterion

For \(u\in C^2(U)\), plurisubharmonicity is equivalent to positive
semidefiniteness of its [[complex-analysis/levi-form|Levi form]]:
\[
\sum_{j,k=1}^d
\frac{\partial^2u}{\partial z_j\partial\bar z_k}(z)
v_j\overline{v_k}\ge0
\]
for all \(z\in U\) and \(v\in\mathbb C^d\).

## Holomorphic logarithms

If \(F:U\to\mathbb C\) is holomorphic and not identically zero, then
\(\log|F|\) is plurisubharmonic. This makes plurisubharmonic functions the
natural potential-theoretic models for magnitudes of
[[complex-analysis/entire-function-several-variables|entire functions of
several variables]].

## References

1. Lars Hörmander, *Notions of Convexity*, Birkhäuser, 2007. [DOI record](https://doi.org/10.1007/978-0-8176-4585-4).
