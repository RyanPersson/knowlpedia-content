+++
id = "partial-differential-equations/heat-equation"
title = "Heat equation"
kind = "definition"
summary = "Evolution whose time derivative is a positive constant times the spatial Laplacian."
aliases = ["diffusion equation"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/partial-differential-equation", "partial-differential-equations/classical-solution", "real-analysis/laplacian", "real-analysis/partial-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **heat equation** with diffusivity \(\nu>0\) is
\[
\partial_tu=\nu\Delta u.
\]
Here \(u=u(x,t)\), and the [[real-analysis/laplacian|Laplacian]] acts on the spatial variables. A classical solution has the derivatives required by this pointwise equality. A prescribed source gives the inhomogeneous equation \(\partial_tu-\nu\Delta u=f\).

## Data and interpretation

An evolution problem also specifies initial data and, on a domain with boundary, boundary conditions. The positive sign of \(\nu\) makes Fourier modes decay forward in time. A component of a vector field expressed in a moving coordinate basis need not satisfy the scalar heat equation: differentiating the basis can introduce additional terms.

## References

- [Hunter, The Heat and Schrödinger Equations, §§5.1–5.3](https://www.math.ucdavis.edu/~hunter/pdes/ch5.pdf).

## Uniqueness from terminal data

[[partial-differential-equations/backward-uniqueness|Backward uniqueness]] holds for the L2 heat evolution even though arbitrary terminal data do not yield a well-posed backward problem.
