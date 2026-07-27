+++
id = "differential-geometry/degree-of-a-smooth-map"
title = "Degree of a smooth map"
kind = "definition"
summary = "An integer measuring the signed number of preimages of a regular value under a proper map of oriented manifolds."
aliases = ["mapping degree", "topological degree of a smooth map"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[differential-geometry/orientation-of-a-smooth-manifold|oriented]] smooth \(n\)-manifolds without boundary, with \(N\) connected, and let \(f:M\to N\) be a [[differential-geometry/proper-smooth-map|proper smooth map]]. For a [[fiber-bundles/regular-value|regular value]] \(y\in N\), the fiber \(f^{-1}(y)\) is finite. At each \(x\in f^{-1}(y)\), the isomorphism \(d f_x:T_xM\to T_yN\) has sign \(+1\) or \(-1\) according as it preserves or reverses orientation. The **degree of \(f\)** is
\[
\deg(f)=\sum_{x\in f^{-1}(y)}\operatorname{sgn}(d f_x).
\]
This integer is independent of the regular value. The empty sum is zero.

## Integral characterization

For every compactly supported \(n\)-form \(\omega\) on \(N\),
\[
\int_M f^*\omega=\deg(f)\int_N\omega.
\]
This identity both recovers the signed-count definition and extends its computational reach. When \(M\) and \(N\) are compact and connected, degree is the scalar by which \(f\) acts on top-dimensional real cohomology [Guillemin and Pollack, Chapter 3](https://bookstore.ams.org/chel-370-h).

## Homotopy and composition

Degree is invariant under [[differential-geometry/smooth-homotopy|proper smooth homotopies]] for which the combined map to \(N\) is proper. For composable proper maps of oriented \(n\)-manifolds,
\[
\deg(g\circ f)=\deg(g)\deg(f).
\]
An orientation-preserving [[fiber-bundles/diffeomorphism|diffeomorphism]] has degree \(1\), whereas an orientation-reversing one has degree \(-1\).

## Examples and scope

The map \(S^1\to S^1\), \(z\mapsto z^m\), has degree \(m\), including negative \(m\). The constant map between positive-dimensional closed oriented manifolds has degree \(0\). Equal dimensions, orientations, properness, and the absence of boundary are part of the stated convention; relative degree and mod-\(2\) degree are different variants when these hypotheses are changed.

## References

1. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint of the 1974 edition. [AMS record](https://bookstore.ams.org/chel-370-h). Relevant: Chapter 3, mapping degree and integration.
2. John W. Milnor, *Topology from the Differentiable Viewpoint*, Princeton University Press, 1997. [Publisher excerpt](https://assets.press.princeton.edu/about_pup/PUP100/book/5aMilnor.pdf). Relevant: §§5–6, degree and oriented manifolds.
