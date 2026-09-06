+++
id = "noncommutative-geometry/chern-character-fredholm-module"
title = "Chern character of a Fredholm module"
kind = "definition"
summary = "The periodic cyclic-cohomology class represented by trace cocycles constructed from a summable Fredholm module."
aliases = ["Connes-Chern character", "cyclic Chern character"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/p-summable-fredholm-module", "noncommutative-geometry/periodic-cyclic-cohomology"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((H,\pi,F)\) be a
[[noncommutative-geometry/p-summable-fredholm-module|\(p\)-summable Fredholm
module]] over a complex algebra \(\mathcal A\). Its **Chern character** is the
class
\[
\operatorname{Ch}(H,\pi,F)\in HP^\varepsilon(\mathcal A)
\]
in [[noncommutative-geometry/periodic-cyclic-cohomology|periodic cyclic
cohomology]], where \(\varepsilon\) is the module's parity. For every integer
\(n>p-1\) of parity \(\varepsilon\), the class has a representative obtained,
up to the standard degree-dependent normalization, by tracing
\[
\pi(a_0)[F,\pi(a_1)]\cdots[F,\pi(a_n)],
\]
with the grading operator inserted in the even case. Summability makes this product trace class. Representatives in successive admissible degrees correspond under cyclic periodicity.

## Why the construction is cohomological

The trace property and \(F^2=1\) imply the cyclic symmetry and cocycle
identity for the displayed cochain. If one starts with an unnormalized
[[noncommutative-geometry/fredholm-module|Fredholm module]], compact perturbation and normalization produce the same
periodic class. Operator homotopies, unitary equivalence, and addition of
degenerate modules also leave the class unchanged. Consequently the
construction factors through [[noncommutative-geometry/analytic-k-homology|analytic K-homology]]
rather than depending on a chosen cycle representative.

The constants in the trace formula are chosen so that representatives in
degrees \(n,n+2,\ldots\) match under Connes's periodicity operator. Omitting
them can preserve the cocycle equation but changes the normalization of the
index pairing.

## Index pairing

Pairing the Chern character with a \(K\)-theory class reproduces the
Fredholm-module index pairing. In even parity, a projection is paired with
the index of the compressed off-diagonal part of \(F\); in odd parity, a
unitary is compressed by the positive spectral projection of \(F\). Thus the
cohomological expression is integral on \(K\)-theory classes.

This equality is the bridge used by local index formulas: a trace cocycle
defined from the bounded phase \(F\) may be replaced, in the same cyclic
cohomology class, by a residue cocycle built from an unbounded operator \(D\).

## Conventions and scope

**Warning.** “Chern character” also names maps from \(K\)-theory to cyclic
homology and classical [[fiber-bundles/characteristic-class|characteristic classes]]
of [[fiber-bundles/vector-bundle|vector bundles]]. The object
defined here is the cohomological character of a Fredholm module. Periodic,
entire, and local cyclic representatives require different summability
hypotheses and should not be identified term by term.

Formulas vary by powers of \(2\), signs, factors of \(i\), and whether a
modified trace is used in low degree. These choices are harmless only when
the cyclic periodicity and \(K\)-theory pairing conventions are changed
consistently.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §1, especially the character formula and Propositions 1–2.
2. A. Connes, “Non-Commutative Differential Geometry,” *Publications Mathématiques de l'IHÉS* 62 (1985), 41–144. [DOI record](https://doi.org/10.1007/BF02698807). Relevant: §§II.1–II.3 on cyclic cohomology and the Chern character of summable Fredholm modules.
