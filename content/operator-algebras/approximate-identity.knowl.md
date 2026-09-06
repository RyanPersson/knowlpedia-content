+++
id = "operator-algebras/approximate-identity"
title = "Approximate identity in a C*-algebra"
kind = "definition"
summary = "A net of positive contractions that converges to an identity through multiplication on every algebra element."
aliases = ["approximate unit", "contractive approximate identity", "approximate identity", "two-sided approximate identity"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-element"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. An
**approximate identity** is a net \((e_\lambda)\) in \(A\) such that, for
every \(a\in A\),
\[
\lim_\lambda e_\lambda a=a
\quad\text{and}\quad
\lim_\lambda a e_\lambda=a
\]
in norm. A **contractive approximate identity** additionally satisfies
\(\lVert e_\lambda\rVert\leq 1\); a **positive contractive approximate
identity** has [[operator-algebras/positive-element|positive]] terms with
\(0\leq e_\lambda\leq 1\). Every \(C^*\)-algebra has a positive contractive
approximate identity, so that form is usually meant by “approximate unit” in
\(C^*\)-algebra theory.

## Existence and construction

One construction directs the positive contractions of \(A\) by how well they
act as identities on finite subsets. Functional calculus applied to finite
sums of elements \(a^*a\) then produces a net that works simultaneously on
both sides.
For a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]
\(I\), the same theorem supplies an approximate identity lying inside \(I\).
In a unital algebra the constant net \(e_\lambda=1_A\) is the simplest
example.

## Sequential and strictly positive cases

An approximate identity need not be a sequence. A \(C^*\)-algebra admits a
[[operator-algebras/sigma-unital-cstar-algebra|countable approximate identity]] precisely when it is \(\sigma\)-unital. If
\(h\in A\) is strictly positive, suitable continuous functions of \(h\), such
as \(h(h+1/n)^{-1}\) in the
[[operator-algebras/unitization|unitization]], form a sequential approximate
identity. Separability implies \(\sigma\)-unitality, but many nonseparable
\(C^*\)-algebras require genuinely nonsequential nets.

## Multipliers and nondegeneracy

Inside the [[operator-algebras/multiplier-algebra|multiplier algebra]]
\(M(A)\), every approximate identity converges strictly to the multiplier
unit: \(e_\lambda a\to a\) and \(ae_\lambda\to a\) for all \(a\in A\).
Likewise, a representation \(\rho:A\to B(\mathcal H)\) is nondegenerate
exactly when \(\rho(e_\lambda)\xi\to\xi\) for every \(\xi\in\mathcal H\).
These facts make approximate identities the correct replacement for an
absent unit, while not asserting norm convergence to a unit outside \(A\).

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.1 on ideals and approximate identities.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.4 on approximate units.
