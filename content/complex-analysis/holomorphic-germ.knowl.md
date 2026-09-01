+++
id = "complex-analysis/holomorphic-germ"
title = "Holomorphic germ"
kind = "definition"
summary = "The local behavior of a holomorphic function near one point, modulo restriction to smaller neighborhoods."
aliases = ["germ of a holomorphic function", "analytic germ"]
domains = ["complex-analysis", "sheaf-theory"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a complex manifold and \(a\in X\). Two holomorphic functions \(f:U\to\mathbb C\) and \(g:V\to\mathbb C\), defined on neighborhoods of \(a\), determine the same **holomorphic germ at \(a\)** if they agree on some neighborhood \(W\subseteq U\cap V\) of \(a\). The equivalence class is denoted \([f]_a\) or \(f_a\).

## Local ring

Holomorphic germs at \(a\) form a [[algebra-commutative/local-ring|local ring]] \(\mathcal O_{X,a}\) under pointwise addition and multiplication of representatives. Its unique [[algebra-rings/maximal-ideal|maximal ideal]] consists of germs vanishing at \(a\); a germ is a unit exactly when its value at \(a\) is nonzero.

## One complex variable

For a plane domain, a germ is completely determined by its convergent Taylor series at \(a\). The [[complex-analysis/order-of-zero-or-pole|order of vanishing]] and the local inverse of a nonvanishing germ depend only on the germ, not on a representative.

## Continuation

[[complex-analysis/analytic-continuation|Analytic continuation]] transports a germ through chains of overlapping neighborhoods. The [[complex-analysis/monodromy-theorem|monodromy theorem]] gives conditions under which the transported germ is independent of the chosen path.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§5–7.
