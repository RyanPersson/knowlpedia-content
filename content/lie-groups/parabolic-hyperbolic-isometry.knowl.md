+++
id = "lie-groups/parabolic-hyperbolic-isometry"
title = "Parabolic isometry of hyperbolic three-space"
kind = "definition"
summary = "A nonidentity orientation-preserving isometry with exactly one ideal fixed point and no interior fixed point."
aliases = ["parabolic element of PSL2C"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/psl2c-action-on-hyperbolic-three-space", "complex-analysis/riemann-sphere"]
+++

A **parabolic isometry** of hyperbolic three-space is a nonidentity orientation-preserving isometry that fixes exactly one point of the ideal boundary [[complex-analysis/riemann-sphere|sphere]] and no point in the interior.

## Normal form

Under the [[lie-groups/psl2c-action-on-hyperbolic-three-space|PSL₂(ℂ) action]], it is conjugate to
\[
z\longmapsto z+1,
\qquad (z,r)\longmapsto(z+1,r).
\]
The corresponding matrix is \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\), considered modulo sign. It fixes \(\infty\) and preserves every horizontal horosphere.

## Matrix test

For a lift \(A\in\operatorname{SL}_2(\mathbb C)\), the test is \((\operatorname{tr} A)^2=4\) and \(A\ne\pm I\). The scalar exclusion prevents misclassifying the identity.

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §2, classification of elements.
