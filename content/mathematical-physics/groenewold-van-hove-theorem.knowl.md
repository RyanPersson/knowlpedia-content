+++
id = "mathematical-physics/groenewold-van-hove-theorem"
title = "Groenewold–Van Hove theorem"
kind = "theorem"
summary = "The obstruction to extending canonical quantization consistently to every polynomial observable on a finite-dimensional linear phase space."
aliases = ["Groenewold-Van Hove theorem", "Groenewold-Van Hove obstruction", "no-go theorem for canonical quantization"]
domains = ["mathematical-physics", "differential-geometry", "functional-analysis"]
prerequisites = ["mathematical-physics/quantization-map"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For the standard symplectic space \(\mathbb R^{2n}\), there is no [[mathematical-physics/quantization-map|quantization map]] on the full Poisson algebra of polynomial observables that simultaneously extends the Schrödinger quantization of the canonical affine observables, sends \(1\) to the identity, satisfies the exact Dirac rule
\[
[Q(f),Q(g)]=i\hbar Q(\{f,g\}),
\]
and obeys the standard domain and irreducibility requirements. This impossibility is the **Groenewold–Van Hove theorem**.

## Quantizable polynomial subalgebras

The obstruction does not prevent every useful exact quantization. The polynomials of degree at most two form a Lie algebra under the [[differential-geometry/poisson-bracket-symplectic|Poisson bracket]] and admit the extended metaplectic quantization. The theorem says that this construction cannot be extended consistently to all higher-degree polynomials under the same axioms. Thus the failure is not a contradiction inside quantum mechanics; it is a limit on a particular exact classical-to-quantum correspondence.

## Source of the contradiction

Classically, a polynomial may admit distinct expressions as Poisson brackets. Applying the exact Dirac rule to those expressions can force incompatible operator identities once the canonical position and momentum operators are fixed. Ordering corrections cannot make all such identities agree at once.

## Scope

Precise formulations differ in the chosen basic algebra, operator domain, irreducibility hypothesis, and meaning of functional calculus. Weaker schemes evade the theorem: one may quantize a smaller Poisson subalgebra, require only an asymptotic commutator formula, or replace operator multiplication by a star product. The theorem should therefore not be paraphrased as saying that “quantization is impossible.”

## References

1. H. J. Groenewold, “On the Principles of Elementary Quantum Mechanics,” *Physica* 12 (1946), 405–460. [DOI record](https://doi.org/10.1016/S0031-8914(46)80059-4). Relevant: the original polynomial obstruction.
2. M. J. Gotay, “On the Groenewold–Van Hove Problem for \(\mathbb R^{2n}\),” *Journal of Mathematical Physics* 40 (1999), 2107–2116. [arXiv record](https://arxiv.org/abs/math-ph/9809015). Relevant: rigorous formulation and the maximal quantizable polynomial subalgebras.
