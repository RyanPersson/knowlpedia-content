+++
id = "operator-algebras/normal-completely-positive-map"
title = "Normal completely positive map"
kind = "definition"
summary = "A completely positive map between von Neumann algebras that is ultraweakly continuous."
aliases = ["normal CP map", "ultraweakly continuous completely positive map"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "linear-algebra/linear-map", "operator-algebras/completely-positive-map", "operator-algebras/normal-linear-map"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[operator-algebras/von-neumann-algebra|von Neumann
algebras]]. A [[linear-algebra/linear-map|linear map]] \(\Phi:M\to N\) is a **normal completely positive
map** if it is both [[operator-algebras/completely-positive-map|completely
positive]] and [[operator-algebras/normal-linear-map|normal]]. Equivalently,
every matrix amplification of \(\Phi\) is positive and \(\Phi\) is ultraweakly
continuous. Since \(\Phi\) is positive, normality may also be tested on
increasing bounded nets:
\[
x_i\uparrow x\quad\Longrightarrow\quad
\Phi(x_i)\uparrow\Phi(x).
\]
Neither unitality nor multiplicativity is included in this definition.

## Preduals and normality

Normality is equivalent to the existence of a bounded preadjoint
\(\Phi_*:N_*\to M_*\) satisfying
\[
\omega(\Phi(x))=\Phi_*(\omega)(x)
\qquad(\omega\in N_*,\ x\in M).
\]
This makes normal CP maps compatible with the intrinsic preduals of von
Neumann algebras.

## Examples and closure properties

Every normal [[operator-algebras/star-homomorphism|\(*\)-homomorphism]] is
normal and completely positive. For a bounded operator \(V:K\to H\), the map
\(B(H)\to B(K)\), \(x\mapsto V^*xV\), is normal CP. Compositions and finite
sums of normal CP maps remain normal CP. [[operator-algebras/normal-conditional-expectation|Normal conditional expectations]] are
important idempotent examples.

## Distinctions

**Warning.** Complete positivity alone does not imply normality: a CP map
between [[operator-algebras/von-neumann-algebra|von Neumann algebras]] can fail to be ultraweakly continuous. Likewise,
normality does not imply complete positivity. A
[[operator-algebras/positive-linear-map|positive map]] need not be completely
positive. A normal CP map need not preserve the identity; imposing
\(\Phi(1_M)=1_N\) gives a
[[operator-algebras/normal-unital-completely-positive-map|normal unital
completely positive map]].

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapters III–IV on normal maps and complete positivity.
2. Vern Paulsen, *Completely Bounded Maps and Operator Algebras*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511546631). Relevant: Chapter 4 on completely positive maps and their representations.
