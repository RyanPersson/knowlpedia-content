+++
id = "algebraic-geometry-foundations/formal-spectrum"
title = "Formal spectrum"
kind = "definition"
summary = "The affine formal scheme Spf(A) associated to a complete adic ring A."
aliases = ["Spf", "affine formal scheme", "formal affine spectrum"]
domains = ["algebraic-geometry-foundations", "formal-groups"]
section_mode = "progressive"
prerequisites = ["algebra-topological/adic-ring", "algebra-topological/ideal-of-definition", "algebraic-geometry-foundations/structure-sheaf"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a complete and separated
[[algebra-topological/adic-ring|adic ring]], and choose a finitely generated
[[algebra-topological/ideal-of-definition|ideal of definition]] \(I\). The
**formal spectrum** \(\operatorname{Spf}(A)\) is the locally topologically
ringed space whose underlying topological space is
\[
\{\mathfrak p\in\operatorname{Spec}(A):\mathfrak p\text{ is open}\}
=V(I)\cong\operatorname{Spec}(A/I),
\]
and whose [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] retains the compatible structure sheaves of all
quotients \(A/I^n\). It may be viewed as the system of infinitesimal
thickenings
\[
\operatorname{Spec}(A/I)
\hookrightarrow
\operatorname{Spec}(A/I^2)
\hookrightarrow\cdots .
\]

## Functions and morphisms

Global functions recover the topological ring:
\[
\Gamma(\operatorname{Spf}(A),\mathcal O)=A.
\]
For complete adic rings \(A\) and \(B\) in this convention, continuous ring
homomorphisms give morphisms in the opposite direction:
\[
\operatorname{Hom}\bigl(\operatorname{Spf}(B),\operatorname{Spf}(A)\bigr)
\cong
\operatorname{Hom}_{\mathrm{cont}}(A,B).
\]
Continuity is essential because the sheaves remember the [[algebra-commutative/i-adic-topology|adic topologies]].

## Relation to ordinary spectra

If \(A\) has the discrete topology, so that \(0\) may be chosen as an ideal
of definition, then
\(\operatorname{Spf}(A)\) is the ordinary
[[algebraic-geometry-foundations/affine-scheme|\(\operatorname{Spec}(A)\)]].
For a general ideal of definition, \(\operatorname{Spf}(A)\) has the
topological space of the scheme of definition
\(\operatorname{Spec}(A/I)\), while its structure sheaf retains functions to
every infinitesimal order. The scheme of definition need not be reduced.

For example,
\[
\operatorname{Spf}(k[[X_1,\ldots,X_n]])
\]
has one underlying point when \(k\) is a field, yet its structure sheaf
contains all formal directions around that point.

## Convention

Several related notions of formal spectrum occur in the literature. This
knowl uses the classical adic/EGA convention with complete separated adic
rings and finitely generated ideals of definition, which is sufficient for
the finite-dimensional formal discs used in formal Lie theory.

## References

1. The Stacks Project Authors, “Formal schemes à la EGA.” [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY). Relevant: the construction of \(\operatorname{Spf}(A)\) and continuous morphisms.
2. Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique I: Le langage des schémas*, Publications Mathématiques de l’IHÉS 4 (1960). Relevant: Chapter 0, §7, formal schemes.
