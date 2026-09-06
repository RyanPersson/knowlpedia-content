+++
id = "differential-geometry/collar-neighborhood-theorem"
title = "Collar neighborhood theorem"
kind = "theorem"
summary = "Every smooth manifold with boundary has a neighborhood of its boundary diffeomorphic to a product with a half-open interval."
aliases = ["collar theorem", "boundary collar"]
domains = ["differential-geometry", "topology"]
prerequisites = ["differential-geometry/manifold-with-boundary", "fiber-bundles/smooth-embedding", "differential-geometry/product-manifold", "differential-geometry/smooth-map-of-manifolds-with-boundary"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]]. There exists a [[fiber-bundles/smooth-embedding|smooth embedding]]
\[
c:\partial M\times[0,1)\longrightarrow M
\]
such that \(c(x,0)=x\) for every \(x\in\partial M\), and whose image is an open neighborhood of \(\partial M\) in \(M\). Such an embedding is called a **collar** of the boundary. Equivalently, \(c\) is a diffeomorphism from the [[differential-geometry/product-manifold|product manifold]] \(\partial M\times[0,1)\) onto its image.
Here smoothness is understood in the
[[differential-geometry/smooth-map-of-manifolds-with-boundary|manifold-with-boundary
sense]], including extension across the endpoint.

## Construction idea

Choose a smooth [[fiber-bundles/vector-field|vector field]] along the boundary that points inward and extend it to a neighborhood. Its local flow carries each [[differential-geometry/boundary-and-interior-of-a-manifold|boundary point]] into the interior. Flow existence gives a product map for a point-dependent time; a positive rescaling of the vector field and a locally finite construction make the interval uniform. Injectivity after shrinking produces the collar.

## Consequences

A collar gives a [[differential-geometry/boundary-defining-function|boundary defining function]] by taking the interval coordinate near \(\partial M\) and extending it positively over the rest of \(M\). It also provides room for gluing manifolds along diffeomorphic boundary components: product coordinates identify smooth structures on the two sides. In cobordism, collars ensure that composition by boundary gluing is independent of accidental coordinate behavior at the seam.

The inclusion \(\partial M\hookrightarrow c(\partial M\times[0,1))\) is a deformation retract, with homotopy \(c(x,t)\mapsto c(x,(1-s)t)\). This conclusion concerns the collar neighborhood, not generally the whole manifold.

## Examples and nonuniqueness

For \(M=N\times[0,1)\), the identity map is the standard collar. A closed interval has a collar consisting of two disjoint short half-intervals, one at each endpoint. On the [[topology/closed-ball|closed ball]], radial motion inward gives a collar of the sphere.

Collars are not canonical: different inward vector fields give different embeddings. The map \(c(x,t)=c_0(x,t^2)\) built from a collar \(c_0\) is not another collar, because its differential loses the normal direction at \(t=0\).

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 9, boundary flowouts and the collar neighborhood theorem.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, collars and tubular-neighborhood methods.
