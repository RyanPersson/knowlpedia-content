+++
id = "grh-lean/main-inequality"
title = "Comparing the upper and lower covolume bounds"
kind = "theorem"
summary = "The common main amount cancels and leaves a signed prime remainder."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/short-forms", "grh-lean/enough-forms", "grh-lean/long-forms", "linear-algebra/hadamard-gram-bound"]
+++

For [[grh-lean/arithmetic-data|admissible data]], the chain length \(m\), total remainder \(R\), number \(f\) of infinite places and scale \(a=xb\) satisfy \(mR\le fa(\log b)^5\).

## Proof

Let \(d_T\) be the target dimension, \(H\ge0\) the main amount, and \(\ell=fa(\log b)^4\). By [[grh-lean/enough-forms|Theorem B]], choose translates meeting at least \((1-4/b^2)d_T\) dimensions. By [[grh-lean/short-forms|Theorem A]], take an independent family of \(n\) short images there. [[linear-algebra/hadamard-gram-bound|Hadamard’s inequality]] bounds its logarithmic squared covolume by \(V=n(H-mR+\ell)\). Its index admits a bound \(\Delta\le d_T I\), where \(I=10\log(1+2b^2)\,fa(\log b)^3\).

Apply [[grh-lean/long-forms|Theorem C]] to the same family. It gives \(d_T(H-3\ell)\le V+2\Delta\). Substituting \(V\) leaves
\[
 nmR\le(n-d_T)H+(n+3d_T)\ell+2d_T I
       \le d_T(4\ell+2I).
\]
Here \(n\le d_T\), and \(H\ge0\) allows the first term to be dropped. Since \(n\ge d_T/2>0\), the scale bounds absorb \(2(4\ell+2I)\) into \(fa(\log b)^5\).

## References

- [New/Reduction/MainInequality.lean, star_inequality](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L87)
