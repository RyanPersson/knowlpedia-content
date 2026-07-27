+++
id = "fiber-bundles/zero-section"
title = "Zero section"
kind = "definition"
summary = "The canonical smooth section assigning the zero vector to every fiber of a vector bundle."
aliases = ["canonical zero section", "zero section of a vector bundle"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(\pi:E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]]. Its **zero section** is the map
\[
0_E:M\longrightarrow E,
\qquad
0_E(x)=0_x\in E_x.
\]
It is a smooth [[fiber-bundles/section-of-a-vector-bundle|section]] because every vector-bundle trivialization identifies it with \(x\mapsto(x,0)\). The identity \(\pi\circ0_E=\operatorname{id}_M\) makes \(0_E\) injective, and it is a [[fiber-bundles/smooth-embedding|smooth embedding]]. Its image, also called the zero section, is the embedded copy \(\{0_x:x\in M\}\subseteq E\). No trivialization, connection, or metric is required for this construction.

## Canonical properties

Every [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] \(\Phi:E\to F\) covering \(f:M\to N\) preserves zero vectors:
\[
\Phi\circ0_E=0_F\circ f.
\]
Thus the zero section is natural with respect to vector bundle morphisms. It is also the additive identity in the [[fiber-bundles/module-of-smooth-sections|module of smooth sections]].

## Tangent and normal geometry

Along \(0_E(M)\), the differential of the projection splits the [[fiber-bundles/tangent-bundle|tangent bundle]]:
\[
TE|_{0_E(M)}
\cong
T M\oplus E.
\]
The first summand is tangent to the embedded zero section, and the second consists of vertical tangent vectors in the fibers. Consequently the [[differential-geometry/normal-bundle|normal bundle]] of \(0_E(M)\subseteq E\) is canonically isomorphic to \(E\). This canonical identification is frequently used in tubular-neighborhood constructions and in definitions of the [[fiber-bundles/thom-class|Thom class]].

## Examples and warning

For the tangent bundle \(TM\to M\), the zero section sends \(x\) to the zero tangent vector \(0\in T_xM\). For a trivial bundle \(M\times\mathbb F^r\), it is \(x\mapsto(x,0)\).

**Warning.** A vector bundle always has this [[fiber-bundles/section-of-a-fiber-bundle|global section]], regardless of whether it is trivial. A [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]] is a different notion: the zero section is zero at every point and therefore supplies no member of a global frame.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 10, vector bundles, sections, and embedded zero sections.
2. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 3, vector-bundle constructions.
