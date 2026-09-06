+++
id = "shale-paper/gaussian-measure-hilbert-space"
title = "Gaussian Measure on a Hilbert Space (Segal)"
kind = "definition"
summary = "An isonormal Gaussian process indexed by a real Hilbert space, realized on an auxiliary probability space."
aliases = ["gaussian-measure-hilbert-space", "Gaussian Measure on a Hilbert Space (Segal)"]
domains = ["shale-paper"]
prerequisites = ["linear-algebra/hilbert-space"]
dependency_review_count = 1
legacy_source_path = "shale-paper/gaussian-measure-hilbert-space.md"
+++

Let \(M\) be a real [[linear-algebra/hilbert-space|Hilbert space]]. A **normal
distribution over \(M\)** in Segal's sense is a probability space
\((N,\mathfrak R,n)\) carrying a real-linear map
\[
W:M\longrightarrow L^2(N,n)
\]
such that the random variables \(W(x)\) are jointly centered Gaussian and
\[
\int_N W(x)W(y)\,dn=\langle x,y\rangle_M
\qquad(x,y\in M).
\]
Thus \(W\) is an isometric embedding of \(M\) into the real Gaussian subspace
of \(L^2(N,n)\).

## Finite-dimensional distributions

If \(e_1,\ldots,e_m\) are orthonormal and
\[
F=\bar F\bigl(W(e_1),\ldots,W(e_m)\bigr)
\]
is integrable, then
\[
\int_N F\,dn
=(2\pi)^{-m/2}\int_{\mathbb R^m}
 \bar F(t_1,\ldots,t_m)e^{-\lVert t\rVert^2/2}\,dt.
\]
This compatibility of all finite-dimensional Gaussian marginals is the
integration rule for [[shale-paper/tame-function|tame functions]]. A covariance
\(cI\) convention is obtained by replacing the right-hand covariance above by
\(c\langle x,y\rangle_M\).

## Why the sample space is not \(M\)

If \(M\) is infinite-dimensional, there is no countably additive Gaussian
Borel probability measure on \(M\) having covariance \(I\): the covariance
operator of a Gaussian Borel measure on a Hilbert space must be trace class,
whereas \(I\) is not. The notation \(L^p(M,n)\) used in this context therefore
refers to the Gaussian probability-space realization, not literally to a
standard Gaussian measure supported on \(M\).

## Shale's setting

These Gaussian \(L^p\)-spaces are used in §3 of Shale's paper. The relevant
Gaussian measure class is quasi-invariant under the
[[shale-paper/restricted-general-linear-group-rgl|restricted general linear
group]].
