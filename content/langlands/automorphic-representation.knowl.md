+++
id = "langlands/automorphic-representation"
title = "Automorphic representation"
kind = "knowl"
summary = "An irreducible representation occurring as a subquotient of a space of automorphic forms."
aliases = ["automorphic representations"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
+++

Let \(F\) be a global field and \(G\) a connected reductive \(F\)-group. An
**automorphic representation** of \(G(\mathbb A_F)\) is an irreducible
subquotient of the right-regular representation on an appropriate space
\(\mathcal A(G)\) of [[langlands/automorphic-form|automorphic forms]], usually
with a fixed central character.

## Representation category

At finite places one works with smooth admissible representations. At the
archimedean places one ordinarily records the underlying
\((\mathfrak g_\infty,K_\infty)\)-module. Consequently, the displayed adelic
representation is shorthand for a compatible archimedean Harish-Chandra
module and a smooth representation of \(G(\mathbb A_F^\infty)\).

An automorphic representation need not occur as a closed irreducible
subrepresentation of an \(L^2\)-space. Constituents of Eisenstein series can
appear naturally as subquotients. By contrast, a representation in the
[[langlands/discrete-automorphic-spectrum|discrete spectrum]] occurs
unitarily, with a multiplicity, in the automorphic \(L^2\)-space.

## Local components

An irreducible admissible automorphic representation factors as a
[[langlands/restricted-tensor-product-automorphic-representation|restricted
tensor product]]

\[
\pi \simeq \bigotimes_v' \pi_v .
\]

Almost every finite-place component \(\pi_v\) is unramified. These local
components carry [[langlands/satake-parameter|Satake parameters]] or [[langlands/local-l-parameter|local Langlands parameters]] and are the
inputs to Euler products.

## Nearly equivalent representations

Two automorphic representations are **nearly equivalent** if their local
components are isomorphic at all but finitely many places. Strong
multiplicity one makes near equivalence very rigid for
\(\operatorname{GL}_n\), but it need not identify representations for a
general [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]. Global packets and multiplicity formulas account for
this distinction.

## Terminology warning

An automorphic form is a vector-valued analytic object; an automorphic
representation is an [[algebra-representation-theory/irreducible-representation|irreducible representation]] generated or detected by
such vectors. The two terms should not be used interchangeably.

## References

1. A. Borel and H. Jacquet, “Automorphic forms and automorphic
   representations,” in *Automorphic Forms, Representations and
   \(L\)-Functions*, Proc. Sympos. Pure Math. 33, part 1, 1979, pp. 189–207.
2. James Arthur, “An introduction to the trace formula,” in *Harmonic
   Analysis, the Trace Formula, and Shimura Varieties*, 2005.
   [Clay Mathematics Proceedings](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
