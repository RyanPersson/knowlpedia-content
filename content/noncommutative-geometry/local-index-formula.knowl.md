+++
id = "noncommutative-geometry/local-index-formula"
title = "Local index formula in noncommutative geometry"
kind = "theorem"
summary = "A residue formula representing the cyclic Chern character of suitable regular finitely summable spectral triples."
aliases = ["Connes–Moscovici index formula", "Connes–Moscovici local index formula"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/regular-spectral-triple", "noncommutative-geometry/dimension-spectrum", "convex-analysis/linear-combination"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((\mathcal A,H,D)\) be a finitely summable [[noncommutative-geometry/regular-spectral-triple|regular spectral triple]] with discrete [[noncommutative-geometry/dimension-spectrum|dimension spectrum]] and the meromorphic-continuation hypotheses of Connes and Moscovici. The **local index formula** states that the periodic cyclic Chern character of the bounded transform of \(D\) is represented by a finite \((b,B)\)-cocycle whose components are [[convex-analysis/linear-combination|linear combinations]] of residues at specified poles of
\[
\operatorname{Tr}_{s}\!\left(
a_0[D,a_1]^{(k_1)}\cdots[D,a_n]^{(k_n)}
|D|^{-n-2|k|-z}\right).
\]
Here \(T^{(k)}\) denotes the \(k\)-fold commutator with \(D^2\), and \(\operatorname{Tr}_{s}\) is the parity-appropriate trace.

## Hypotheses and notation

[[noncommutative-geometry/finitely-summable-spectral-triple|Finite summability]]
controls which cochain degrees and multi-indices can
contribute. Regularity supplies the abstract pseudodifferential calculus
needed to expand products and resolvents. The dimension-spectrum hypothesis
provides meromorphic continuation of the weighted zeta functions whose
residues occur in the formula. None of these three hypotheses alone implies
the other two.

The displayed expression suppresses universal coefficients involving
factorials and gamma functions. Their exact form depends on whether one uses
the even or odd cocycle, how \(D\)'s kernel is removed, and the normalization
of the \((b,B)\)-complex.

## Meaning of locality

The bounded-transform character is global: it involves the phase of \(D\)
and ordinary operator traces. The residue cocycle instead uses finitely many
iterated commutators and coefficients extracted from spectral asymptotics.
For classical [[noncommutative-geometry/dirac-operator|Dirac operators]] these
residues are integrals of local
symbolic expressions, recovering the local character of the
Atiyah–Singer index density.

In the abstract setting, “local” means residue-local relative to the
pseudodifferential calculus of the triple. It does not assert that an
underlying point-set space or coordinate neighborhood exists.

## Consequences and use

Because the residue cocycle represents the
[[noncommutative-geometry/chern-character-fredholm-module|Chern character of the Fredholm module]],
pairing it with \(K\)-theory computes the same Fredholm index. The theorem
therefore turns an index defined by a compressed operator into a finite sum
of residues that can often be calculated from heat-kernel or symbol
asymptotics.

## Conventions and scope

**Warning.** A regular finitely summable triple need not satisfy the
meromorphic-continuation and pole-order assumptions required by the formula.
“Simple dimension spectrum” gives the cleanest residue presentation; multiple
poles require higher residue functionals. Semifinite, twisted, and nonunital
local index formulas are genuine extensions with modified hypotheses.

The theorem is an equality of cyclic-cohomology classes, not generally an
identity between one chosen residue cochain and one chosen bounded character
cochain. They can differ by a \((b,B)\)-coboundary.

## References

1. A. Connes and H. Moscovici, “The Local Index Formula in Noncommutative Geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243. [DOI record](https://doi.org/10.1007/BF01895667). Relevant: §§II–III, especially Theorems II.1 and II.2 and the residue cocycle.
2. N. Higson, “The Local Index Formula in Noncommutative Geometry,” in *Contemporary Developments in Algebraic K-Theory*, ICTP Lecture Notes 15, 2004. [Author-hosted manuscript](https://nigel.higson.ca/uploads/1/2/1/4/121496570/higson_-_2004_-_the_local_index_formula_in_noncommutative_geometry.pdf). Relevant: §§5–7 on the residue formula and its identification with the Chern character.
