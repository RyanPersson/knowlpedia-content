+++
id = "complex-analysis/winding-number"
title = "Winding number"
kind = "definition"
summary = "The integer measuring how a closed contour winds around a point."
aliases = ["index of a curve", "contour index"]
domains = ["complex-analysis", "topology"]
section_mode = "progressive"
+++

Let \(\gamma\) be a closed piecewise \(C^1\) contour in \(\mathbb C\), and let \(a\notin\gamma\). Its **winding number** or **index about \(a\)** is
\[
\operatorname{Ind}(\gamma,a)
=\frac{1}{2\pi i}\int_\gamma\frac{dz}{z-a}.
\]
This number is an integer and is constant as \(a\) varies within a [[topology/connected-component|connected component]] of \(\mathbb C\setminus\gamma\).

## Interpretation

Choose a continuous argument of \(\gamma(t)-a\) locally along the contour. Its total change after one circuit is \(2\pi\operatorname{Ind}(\gamma,a)\). Positive counterclockwise circuits contribute \(+1\); reversing orientation negates the index.

## Homotopy behavior

The winding number is unchanged under a homotopy of closed contours that avoids \(a\). It therefore records the class of the contour in the punctured plane and supplies the coefficients in the general [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]] and [[complex-analysis/residue-theorem|residue theorem]].

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter IV, §§2–4.
