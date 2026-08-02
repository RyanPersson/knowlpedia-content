+++
id = "differential-geometry/clean-intersection"
title = "Clean intersection"
kind = "definition"
summary = "An intersection of submanifolds whose set and tangent spaces fit together without a tangent-space jump."
aliases = ["cleanly intersecting submanifolds"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(S\) and \(T\) be [[differential-geometry/embedded-submanifold|embedded submanifolds]] of a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\). They **intersect cleanly** if \(C=S\cap T\) is an embedded submanifold of \(M\) and, at every \(p\in C\),
\[
T_pC=T_pS\cap T_pT.
\]
The first condition controls the set-theoretic intersection, while the second requires its smooth structure to have exactly the tangent directions common to \(S\) and \(T\). The definition permits \(C\) to be empty and does not require the [[differential-geometry/tangent-space|tangent spaces]] of \(S\) and \(T\) to span \(T_pM\).

## Relation to transversality

Every pair of [[differential-geometry/transverse-submanifolds|transverse submanifolds]] intersects cleanly by the [[differential-geometry/transverse-intersection-theorem|transverse intersection theorem]]. Clean intersection is weaker: along a [[topology/connected-component|connected component]] of \(C\), the integer
\[
e=\operatorname{codim}_M S+\operatorname{codim}_M T-\operatorname{codim}_M C
\]
equals the codimension of \(T_pS+T_pT\) in \(T_pM\). Thus \(e=0\) precisely in the transverse case.

## Examples and non-examples

Any embedded submanifold \(S\subseteq M\) intersects itself cleanly: the intersection is \(S\), and both sides of the tangent equality are \(T_pS\). Unless \(S\) is open in \(M\), this self-intersection is not transverse.

The \(x\)-axis and the parabola \(y=x^2\) in \(\mathbb R^2\) meet only at the origin, but they do not intersect cleanly. Their set-theoretic intersection has zero tangent space, whereas the two curve tangent spaces intersect in the entire \(x\)-axis.

## Conventions and scope

**Warning.** Merely having a smooth intersection of the expected set-theoretic dimension is not enough: the tangent-space equality is part of the definition. Some treatments formulate clean intersection for maps or for several submanifolds; this knowl concerns two embedded submanifolds.

## References

1. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea Publishing, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: Chapter 3, clean and transverse intersection conditions.
2. Victor Guillemin and Shlomo Sternberg, *Geometric Asymptotics*, American Mathematical Society, 1977. [DOI record](https://doi.org/10.1090/surv/014). Relevant: Chapter I, clean intersections.
