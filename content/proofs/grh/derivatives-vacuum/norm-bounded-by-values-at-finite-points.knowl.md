+++
id = "proofs/grh/derivatives-vacuum/norm-bounded-by-values-at-finite-points"
title = "A bound at finite points bounds the norm"
kind = "lemma"
summary = "If a vector of a standard space, read as a function of adelic vectors, has absolute value at most M at all points with zero archimedean part, then its squared norm is at most M^2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_dataInner_self_le"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
proof_status = "full"
+++

Let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E\) with index set \(n\). A vector \(f\in\mathcal{S}(V)\) is read as the function \(f(y)=\theta(\varrho(y)f)\) of adelic vectors \(y\in\mathbb{A}_E^{\,n}\), and \(\langle f,f\rangle\) denotes the [[?lean:New.Space.dataInner|inner product]] of \(V\), which is the mean of \(\lvert f(y)\rvert^2\) over adelic vectors modulo rational ones (Lean `New.Space.dataInner_eq_quotMean`).

**Lemma.** If \(\lvert f(x_f)\rvert\le M\) for all finite adelic vectors \(x\), then \(\lvert\langle f,f\rangle\rvert\le M^2\).

## Proof

A mean of a function bounded by \(M^2\) is bounded by \(M^2\), so it suffices to show \(\lvert f(y)\rvert^2\le M^2\) for all adelic \(y\). The function \(y\mapsto\lvert f(y)\rvert^2\) is continuous, and the vectors whose archimedean part is the image of a rational vector are dense (the image of \(E\) is dense in \(\prod_{w}\mathbb{C}\) by [[?c:Weak approximation theorem|weak approximation]]); so it suffices to treat \(y\) with archimedean part the image of \(\rho\in E^n\) and arbitrary finite part. For \(\gamma=-\rho\), automorphy of the theta functional gives \(\lvert f(\gamma+y)\rvert=\lvert f(y)\rvert\) (translation by a rational vector changes \(f\) by a factor of absolute value one; Lean `New.Space.apply_vecAtPoint_add`, using that the point of \(V\) is the identity), and \(\gamma+y\) has archimedean part \(0\), i.e. is of the form \(x_f\). Hence \(\lvert f(y)\rvert\le M\).

## References

1. Lean: `New.Parameters.norm_dataInner_self_le` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
