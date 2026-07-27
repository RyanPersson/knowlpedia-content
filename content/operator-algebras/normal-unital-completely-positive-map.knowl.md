+++
id = "operator-algebras/normal-unital-completely-positive-map"
title = "Normal unital completely positive map"
kind = "definition"
summary = "An ultraweakly continuous completely positive map that preserves the identity."
aliases = ["normal UCP map"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) and \(N\) be unital [[operator-algebras/von-neumann-algebra|von
Neumann algebras]]. A linear map \(\Phi:M\to N\) is a **normal unital
completely positive map**, or **normal UCP map**, if it is a
[[operator-algebras/normal-completely-positive-map|normal completely positive
map]] and is also a
[[operator-algebras/unital-completely-positive-map|unital completely positive
map]]; explicitly,
\[
\Phi(1_M)=1_N.
\]
Equivalently, \(\Phi\) is ultraweakly continuous, all its matrix
amplifications are positive, and it preserves the identity. These three
requirements are independent pieces of the definition. In particular, a
normal UCP map is not required to be multiplicative or invertible.

## Basic properties

A normal UCP map is contractive and satisfies the Kadison–Schwarz inequality
\[
\Phi(x)^*\Phi(x)\leq\Phi(x^*x).
\]
Compositions of normal UCP maps are again normal UCP. These properties follow
from unital complete positivity, while normality ensures compatibility with
increasing limits and preduals
[Paulsen, Chapters 2–4](https://doi.org/10.1017/CBO9780511546631).

## Examples

Normal unital [[operator-algebras/star-homomorphism|\(*\)-homomorphisms]] and
normal conditional expectations are normal UCP. On \(M_n(\mathbb C)\), the map
\[
\Phi(x)=t x+(1-t)\operatorname{tr}_n(x)1
\qquad(0\leq t\leq1)
\]
is normal UCP, where \(\operatorname{tr}_n\) is the normalized trace; for
generic \(0<t<1\), it is not multiplicative. A
[[operator-algebras/normal-state|normal state]] is exactly a normal UCP map
\(M\to\mathbb C\).

## Predual interpretation

The preadjoint of a normal UCP map acts in the opposite direction on normal
functionals. In quantum-information terminology, the normal UCP map is the
Heisenberg-picture evolution; its preadjoint preserves the normalization of
normal states. This duality uses normality essentially—without it, a
preadjoint on the canonical preduals need not exist.

## References

1. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapters 2–4 on UCP maps, Schwarz inequalities, and dilations.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapters III–IV on normal maps and completely positive maps.
