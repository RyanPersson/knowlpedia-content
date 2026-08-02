+++
id = "differential-geometry/neat-embedding"
title = "Neat embedding"
kind = "definition"
summary = "A smooth embedding between manifolds with boundary that is exactly boundary preserving and transverse to the target boundary."
aliases = ["boundary-compatible embedding"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(N\) and \(M\) be smooth [[differential-geometry/manifold-with-boundary|manifolds with boundary]]. A **neat embedding** is a [[fiber-bundles/smooth-embedding|smooth embedding]] \(e:N\to M\) such that
\[
e^{-1}(\partial M)=\partial N
\]
and \(e\) is transverse to \(\partial M\). Equivalently, for every \(p\in\partial N\),
\[
d e_p(T_pN)+T_{e(p)}\partial M=T_{e(p)}M.
\]
Thus interior points map to the interior, boundary points map to the boundary, and the embedded image meets the ambient boundary without tangency. Properness or closedness of \(e\) is not part of this core convention unless stated separately.

## Image characterization

The image of a neat embedding is a [[differential-geometry/neat-submanifold|neat submanifold]], and the embedding identifies \(N\) diffeomorphically with that image. Conversely, the inclusion of a neat submanifold is a neat embedding. Boundary-adapted coordinates put the map locally into the standard linear inclusion of one half-space into another.

## Examples and non-examples

The inclusion of a diameter \([-1,1]\hookrightarrow D^2\) is neat: its two boundary points land on \(\partial D^2\) and the diameter meets the circle transversely. An embedded arc that is tangent to the circle at an endpoint is not neat, because the displayed transversality condition fails there. An embedding that sends an [[differential-geometry/boundary-and-interior-of-a-manifold|interior point]] to \(\partial M\) also fails the boundary-preimage condition.

## Conventions and scope

Some treatments add properness, closed image, or a prescribed product form in collars to the term “neat embedding.” Those global additions are useful in relative embedding and tubular-neighborhood theorems, but they are stronger than the local boundary compatibility stated here. The convention should therefore be checked when compactness is absent.

## References

1. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, neat submanifolds and boundary-compatible embeddings.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 5, embedded submanifolds with boundary.
