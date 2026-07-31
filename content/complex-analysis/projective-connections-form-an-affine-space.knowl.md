+++
id = "complex-analysis/projective-connections-form-an-affine-space"
title = "Projective connections form an affine space"
kind = "theorem"
summary = "Holomorphic projective connections, when they exist, form an affine space over holomorphic quadratic differentials."
aliases = ["affine space of projective connections"]
domains = ["complex-analysis", "differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a Riemann surface. If the set of [[complex-analysis/projective-connection|holomorphic projective connections]] on \(X\) is nonempty, it is an affine space modeled on the vector space
\[
H^0(X,K_X^{\otimes2})
\]
of holomorphic quadratic differentials.

## Difference of two connections

If \(R\) and \(\widetilde R\) are projective connections, their Schwarzian terms cancel under a coordinate change \(w=w(z)\):
\[
(R_z-\widetilde R_z)(z)
=
(R_w-\widetilde R_w)(w(z))\bigl(w'(z)\bigr)^2.
\]
This is exactly the transformation law for a holomorphic quadratic differential.

## Translation by a quadratic differential

Conversely, if \(q\) is a holomorphic quadratic differential and \(R\) is a projective connection, then the local coefficients \(R_z+q_z\) satisfy the projective-connection transformation law. Therefore quadratic differentials act freely and transitively on the set of projective connections.

## References

1. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective structures and projective connections.
