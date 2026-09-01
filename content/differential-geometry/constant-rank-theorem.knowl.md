+++
id = "differential-geometry/constant-rank-theorem"
title = "Constant rank theorem"
kind = "theorem"
summary = "A smooth map of locally constant rank has coordinates in which it is a coordinate projection followed by a coordinate inclusion."
aliases = ["rank theorem for smooth maps", "constant-rank normal form"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-map", "differential-geometry/rank-of-a-smooth-map"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(f:M^m\to N^n\) be a [[fiber-bundles/smooth-map|smooth map]], and suppose its [[differential-geometry/rank-of-a-smooth-map|rank]] is constantly \(r\) on a neighborhood of \(p\in M\). The **constant rank theorem** states that there are smooth coordinate charts \(\varphi\) about \(p\) and \(\psi\) about \(f(p)\), both centered at the origin, such that
\[
(\psi\circ f\circ\varphi^{-1})(x^1,\ldots,x^m)
=(x^1,\ldots,x^r,0,\ldots,0).
\]
Thus, locally and up to diffeomorphisms of source and target, \(f\) is the projection onto \(r\) coordinates followed by the inclusion into \(n\) coordinates. Local constancy of rank near \(p\), not merely rank \(r\) at \(p\), is the essential hypothesis.

## Geometric consequences

After shrinking the charts, each nonempty local fiber of \(f\) is an [[differential-geometry/embedded-submanifold|embedded submanifold]] of dimension \(m-r\), described by fixing the first \(r\) coordinates. The local image is an embedded \(r\)-dimensional submanifold of \(N\). Moreover,
\[
T_x(f^{-1}(f(x)))=\ker df_x
\]
throughout the constant-rank neighborhood. These conclusions are immediate from the displayed normal form.

## Full-rank special cases

When \(r=m\), the normal form is a coordinate inclusion, giving the local model for a [[fiber-bundles/smooth-immersion|smooth immersion]]. When \(r=n\), it is a coordinate projection, giving the local model for a [[fiber-bundles/smooth-submersion|smooth submersion]]. If \(m=n=r\), it reduces to the [[shared-foundations/inverse-function|inverse function]] theorem and \(f\) is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]].

## Conventions and scope

Some texts call this result simply the “rank theorem.” A related local form remains available when the rank is only known to be \(r\) at \(p\), provided a suitable \(r\times r\) minor stays nonzero and additional target components are retained; the clean zero-component form above requires constant rank.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 4, the rank theorem and its immersion and submersion corollaries.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 1, local forms of smooth maps.
