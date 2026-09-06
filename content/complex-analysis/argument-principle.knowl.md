+++
id = "complex-analysis/argument-principle"
title = "Argument principle"
kind = "theorem"
summary = "The logarithmic derivative counts zeros minus poles inside a contour."
aliases = ["principle of the argument"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/meromorphic-function", "complex-analysis/complex-contour-integral", "complex-analysis/winding-number", "complex-analysis/logarithmic-derivative", "complex-analysis/residue-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(f\) be meromorphic on a domain containing a positively oriented simple closed contour \(\gamma\) and its interior, with no zeros or poles on \(\gamma\). If \(N\) and \(P\) are the numbers of zeros and poles inside \(\gamma\), counted with multiplicity, then
\[
\frac{1}{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\,dz=N-P.
\]

## Winding interpretation

The integral equals the [[complex-analysis/winding-number|winding number]] of the image contour \(f\circ\gamma\) about \(0\). As \(\gamma\) is traversed, the net change in a continuous choice of \(\arg f\) is \(2\pi(N-P)\).

## Residue proof

At a zero or pole \(a\), the [[complex-analysis/logarithmic-derivative|logarithmic derivative]] and local factorization give
\[
\operatorname{Res}\!\left(\frac{f'}f,a\right)
=\operatorname{ord}_a(f).
\]
The result follows directly from the [[complex-analysis/residue-theorem|residue theorem]]. [[complex-analysis/rouche-theorem|Rouché's theorem]] and many root-counting methods are refinements of this mechanism.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 5, §2.
