+++
id = "algebra-fields-galois/dedekind-zeta-function"
title = "Dedekind zeta function"
kind = "definition"
summary = "The Dirichlet series summing inverse powers of nonzero integral-ideal norms."
aliases = []
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ideal-norm"]
+++

For a number field \(K\), the **Dedekind zeta function**, initially on \(\operatorname{Re}(s)>1\), is
\[
\zeta_K(s)=\sum_{0\ne\mathfrak a\subseteq\mathcal O_K}(N\mathfrak a)^{-s}.
\]
The sum runs over all nonzero integral ideals, including the unit ideal, and \(N\mathfrak a\) is the [[algebra-fields-galois/ideal-norm|absolute ideal norm]]. The series converges absolutely in this half-plane.

## How to read the sum

It is a sum over ideals, not over generators or ideal classes. For \(K=\mathbb Q\), the ideals are \(n\mathbb Z\) with \(n\ge1\), giving \(\sum_{n\ge1}n^{-s}\).

At \(s=2\) every summand is positive and the value is finite. This is the value used in the [[differential-geometry/bianchi-orbifold-volume-formula|Bianchi volume formula]]; no analytic continuation is needed to interpret it.

## References

1. F. Paulin, *Regards croisés sur les séries de Poincaré et leurs applications*, Theorem 6, p. 12. [Author’s text](https://www.imo.universite-paris-saclay.fr/~frederic.paulin/preprints/Neuchatel.pdf) Definition immediately before Theorem 6.
