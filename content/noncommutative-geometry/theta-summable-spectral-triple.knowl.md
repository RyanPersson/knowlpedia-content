+++
id = "noncommutative-geometry/theta-summable-spectral-triple"
title = "Theta-summable spectral triple"
kind = "definition"
summary = "A spectral triple whose Dirac heat operator has finite trace at every positive time."
aliases = ["heat-kernel summable triple", "theta summability"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

A [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\) is **theta-summable** if
\[
e^{-tD^2}
\]
is trace class for every \(t>0\), equivalently if
\(\operatorname{Tr}(e^{-tD^2})<\infty\) for every \(t>0\), where
\(\operatorname{Tr}\) is the [[operator-algebras/operator-trace|canonical operator trace]]. The exponential is defined by functional calculus for the self-adjoint operator \(D\). This condition controls the multiplicity and growth of the spectrum without requiring any fixed power of \((1+D^2)^{-1/2}\) to be trace class. Consequently, theta summability is weaker than finite \(p\)-summability but strong enough to make heat-kernel cochains, notably the Jaffe–Leśniewski–Osterwalder cochain, analytically meaningful.

## Comparison with finite summability

If \((1+D^2)^{-p/2}\) is trace class for some \(p>0\), then the triple is
theta-summable: exponential decay dominates every negative power. The converse
fails. For example, an eigenvalue counting function may grow faster than every
polynomial while remaining subexponential in the sense required for
\(\operatorname{Tr}(e^{-tD^2})\) to converge at every positive time.

## Role in entire cyclic cohomology

Products containing heat factors \(e^{-t_jD^2}\) regularize the unbounded
commutators that occur in the JLO formula. Integration over a simplex and
trace-norm estimates then give the factorial growth bounds required of an
entire cyclic cochain. This is the original analytic setting of
[Jaffe–Leśniewski–Osterwalder, §§2–4](https://doi.org/10.1007/BF01218474).

## Conventions and scope

**Warning.** Requiring the heat operator to be trace class for one specified
time gives convergence automatically only for larger times. Theta summability
requires every \(t>0\). In semifinite spectral geometry, the ordinary operator
trace is replaced by a chosen [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]]; that is a
different ambient definition.

## References

1. A. Jaffe, A. Leśniewski, and K. Osterwalder, “Quantum K-Theory. I. The Chern Character,” *Communications in Mathematical Physics* 118 (1988), 1–14. [DOI record](https://doi.org/10.1007/BF01218474). Relevant: theta-summability and the entire Chern character.
2. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapter IV on theta-summable Fredholm modules and entire cyclic cohomology.
