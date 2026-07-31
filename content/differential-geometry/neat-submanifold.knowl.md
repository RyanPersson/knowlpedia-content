+++
id = "differential-geometry/neat-submanifold"
title = "Neat submanifold"
kind = "definition"
summary = "A boundary-compatible embedded submanifold that meets the ambient boundary transversely and has no other boundary."
aliases = ["neat embedded submanifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]], and let \(S\subseteq M\) be an embedded [[differential-geometry/embedded-submanifold|smooth submanifold]] with boundary. The submanifold \(S\) is **neat** if
\[
\partial S=S\cap\partial M
\]
and \(S\) is [[differential-geometry/transverse-submanifolds|transverse]] to \(\partial M\) at every point of \(\partial S\); explicitly,
\[
T_pS+T_p(\partial M)=T_pM\qquad(p\in\partial S).
\]
Thus every [[differential-geometry/boundary-and-interior-of-a-manifold|boundary point]] of \(S\) lies on the ambient boundary, every intersection with the ambient boundary is a boundary point of \(S\), and the meeting is non-tangential.

## Local form

Around each boundary point, neatness gives boundary-adapted coordinates in which
\[
M=\{x^n\geq0\},\qquad
S=\{x^k=\cdots=x^{n-1}=0,\ x^n\geq0\}
\]
after a suitable reordering of coordinates, with \(x^n\) serving as the inward boundary coordinate on \(S\). This local normal form is the reason neat submanifolds admit boundary-compatible [[differential-geometry/tubular-neighborhood|tubular neighborhoods]] [Hirsch, Chapter 4].

## Examples and non-examples

A properly embedded diameter of the closed disk is neat: its endpoints lie on the circle and it meets the circle transversely. An arc tangent to the boundary at an endpoint is not neat, even if that endpoint is its only intersection with the ambient boundary.

## Conventions and scope

Some authors build closedness or properness of the inclusion into “neat,” while others impose it separately. The core definition here records the local boundary and transversality conditions; global closedness must be stated when a theorem, such as a global tubular-neighborhood result, requires it.

## References

1. M. W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, neat submanifolds and tubular neighborhoods.
2. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 5, submanifolds with boundary.
