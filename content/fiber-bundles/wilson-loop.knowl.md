+++
id = "fiber-bundles/wilson-loop"
title = "Wilson loop"
kind = "definition"
summary = "The trace of connection holonomy around a closed loop in a chosen representation."
aliases = ["Wilson observable", "trace of holonomy"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] with [[fiber-bundles/principal-connection|connection]] \(A\), let \(\rho:G\to\operatorname{GL}(V)\) be a finite-dimensional [[lie-groups/representation-of-a-lie-group|representation]], and let \(\gamma\) be a piecewise smooth closed loop based at \(x\). Choosing \(p\in P_x\), [[fiber-bundles/parallel-transport|parallel transport]] around \(\gamma\) gives a holonomy element \(h_{A,\gamma,p}\in G\). The **Wilson loop in the representation \(\rho\)** is
\[
W_{\rho,\gamma}(A)
:=
\operatorname{tr}\!\bigl(\rho(h_{A,\gamma,p})\bigr).
\]
Changing \(p\) conjugates the holonomy element, so invariance of the [[linear-algebra/trace|trace]] under conjugation makes \(W_{\rho,\gamma}(A)\) independent of this choice.

## Gauge invariance

Under a [[fiber-bundles/gauge-transformation|gauge transformation]], based holonomy is conjugated by the value of the transformation at the basepoint. Therefore
\[
W_{\rho,\gamma}(u\cdot A)=W_{\rho,\gamma}(A).
\]
Thus the Wilson loop is a function on gauge-equivalence classes of connections, even though the holonomy element itself depends on a point in the fiber. This is the basic mechanism by which a geometric transport operator produces a gauge-invariant observable.

## Geometric meaning

The Wilson loop packages the [[algebra-groups/conjugacy-class|conjugacy class]] of the [[fiber-bundles/holonomy-group|holonomy]] along \(\gamma\) through the character of \(\rho\). For a flat connection, it depends only on the based homotopy class of \(\gamma\). For a curved connection, smoothly homotopic loops can have different Wilson values; infinitesimal loops detect the [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]] to leading order.

If \(\gamma^{-1}\) is the oppositely oriented loop, then
\[
W_{\rho,\gamma^{-1}}(A)
=
\operatorname{tr}\!\bigl(\rho(h_{A,\gamma,p}^{-1})\bigr),
\]
which need not equal \(W_{\rho,\gamma}(A)\) for an arbitrary representation.

## Conventions

Some authors normalize the trace by \(\dim V\), insert a sign or coupling constant in the exponential convention for holonomy, or reserve “Wilson loop” for its expectation value in a quantum [[fiber-bundles/gauge-theory|gauge theory]]. The representation and normalization must therefore be specified. Before taking the trace, the parallel-transport operator is often called a Wilson line; along an open path it transforms at both endpoints and is not by itself gauge invariant.

## References

1. Kenneth G. Wilson, “Confinement of quarks,” *Physical Review D* 10 (1974), 2445–2459. [DOI record](https://doi.org/10.1103/PhysRevD.10.2445). Relevant: the original lattice-gauge Wilson observable.
2. John C. Baez and Javier P. Muniain, *Gauge Fields, Knots and Gravity*, World Scientific, 1994. [DOI record](https://doi.org/10.1142/2324). Relevant: holonomy and gauge-invariant loop observables.
