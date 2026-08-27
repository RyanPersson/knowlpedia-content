+++
id = "complex-analysis/octonionic-plurisubharmonic-function"
title = "Octonionic plurisubharmonic function"
kind = "definition"
summary = "An upper-semicontinuous function on the octonionic plane whose restriction to every affine octonionic line is subharmonic."
aliases = ["octonionic PSH function", "octonionic plurisubharmonicity", "oPSH function"]
domains = ["complex-analysis", "octonionic-analysis", "potential-theory"]
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb O^2\) be open. A function
\(u:\Omega\to[-\infty,\infty)\) is **octonionic plurisubharmonic** if it is
[[complex-analysis/upper-semicontinuous-function|upper-semicontinuous]] and
its restriction to every
[[complex-analysis/octonionic-affine-line|affine octonionic line]] is
[[complex-analysis/subharmonic-function|subharmonic]] on that underlying
eight-dimensional real affine space.

## Smooth criterion

For \(u\in C^2(\Omega)\), octonionic plurisubharmonicity is equivalent to
positive semidefiniteness of the
[[complex-analysis/octonionic-hessian|octonionic Hessian]].

## Relations and closure properties

Every convex function on \(\mathbb O^2\cong\mathbb R^{16}\) is octonionic
PSH, and every octonionic PSH function is ordinary subharmonic. Nonnegative
linear combinations and finite maxima remain octonionic PSH. The class is
invariant under translations and
[[lie-groups/octonionic-special-linear-group|
\(SL_2(\mathbb O)\cong\operatorname{Spin}(9,1)\)]].

## Scope

The definition belongs to the octonionic plane. Although one can write
linewise conditions in other dimensions, the determinant theory needed for
the established Monge–Ampère measure does not extend routinely beyond
\(\mathbb O^2\).

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: §3.1.
