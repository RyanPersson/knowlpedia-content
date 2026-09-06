+++
id = "differential-geometry/lorentzian-manifold"
title = "Lorentzian manifold"
kind = "definition"
summary = "A pseudo-Riemannian manifold with one timelike direction at every point."
aliases = ["Lorentz manifold", "Lorentzian metric manifold"]
domains = ["differential-geometry", "mathematical-physics"]
prerequisites = ["differential-geometry/pseudo-riemannian-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An \(n\)-dimensional **Lorentzian manifold** is a [[differential-geometry/pseudo-riemannian-manifold|pseudo-Riemannian manifold]] \((M,g)\) whose metric has signature \((1,n-1)\). In the convention used here, a nonzero tangent vector \(v\) is **timelike**, **null**, or **spacelike** according as
\[
g(v,v)<0,\qquad g(v,v)=0,\qquad\text{or}\qquad g(v,v)>0.
\]
The timelike and null directions determine the causal cones of \(M\).

## Time orientation

At each point the timelike cone has two connected components. A [[differential-geometry/time-orientation|time orientation]] is a continuous choice of one component as future-pointing; equivalently, it is represented by a continuous timelike vector field. A Lorentzian manifold need not be time-orientable, and the Lorentzian metric alone does not choose a time orientation. In relativity, a **spacetime** commonly means a connected, time-oriented four-dimensional Lorentzian manifold, sometimes with additional causality hypotheses.

## Geometry and morphisms

The metric determines a [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]], geodesics, curvature, and a volume density. A Lorentzian isometry \(F:(M,g)\to(N,h)\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]] satisfying \(F^*h=g\). If time orientations or space orientations are part of the objects, their morphisms are normally required to preserve that extra structure.

## Examples

[[mathematical-physics/minkowski-spacetime|Minkowski spacetime]] is flat and has a canonical time orientation once the coordinate vector \(\partial_t\) is declared future-pointing. The product metric
\[
g=-dt^2+h_t
\]
on \(I\times\Sigma\), where each \(h_t\) is Riemannian, is Lorentzian and time-oriented by \(\partial_t\). Curved examples include de Sitter and anti-de Sitter spacetimes.

## Sign warning

Sources that list positive directions first call the same \((-+\cdots+)\) metric's signature \((n-1,1)\), while its timelike vectors still have negative squared length. Other sources reverse the metric to \((+-\cdots-)\) and call vectors with positive squared length timelike; in this collection's negative-first ordering, that opposite metric also has signature \((n-1,1)\). Formulas for the [[mathematical-physics/dalembert-operator|wave operator]] and [[differential-geometry/clifford-module|Clifford multiplication]] must be translated consistently when the overall sign changes.

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983. [Publisher record](https://doi.org/10.1016/C2009-0-03118-3). Relevant: Chapters 5 and 14.
2. John K. Beem, Paul E. Ehrlich, and Kevin L. Easley, *Global Lorentzian Geometry*, 2nd ed., Marcel Dekker, 1996. [Publisher record](https://doi.org/10.1201/9780203753125). Relevant: Chapters 1–3.
