+++
id = "proofs/grh/spanning-core/link-of-an-isometry"
title = "Link of an isometry"
kind = "definition"
summary = "The module of pairs (class of t, class of gamma^-1 t) in two copies of X-perp/X, for t orthogonal to X and to gamma X."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.linkMatrix", "New.link"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(R\) be a commutative ring with involution, \(T\) a hermitian matrix on the middle indices (\(x_i\), \(i\in\kappa\), and \(z\)), \(h\) the form with \(\varrho\) hyperbolic pairs \((e_a,e_a^*)\) and middle block \(T\) on the free module \(L\) with basis \(e_a;x_i,z;e_a^*\), and \(\gamma\) an isometry of \(h\). Let \(X=\langle e_1,\dots,e_\varrho\rangle\). A vector \(t\in L\) is orthogonal to \(X\) exactly when its coordinates at the \(e_a^*\) vanish, and then its **middle coordinates** \([t]\in R^{\kappa\sqcup\{z\}}\) represent its class in \(X^\perp/X\).

The **link** of \(\gamma\) is the submodule of \(R^{\kappa\sqcup\{z\}}\oplus R^{\kappa\sqcup\{z\}}\)
\[
\operatorname{link}(\gamma)=\bigl\{\,([t],[\gamma^{-1}t])\ :\ t\in L,\ h(e_a,t)=0=h(\gamma e_a,t)\ \text{for }a=1,\dots,\varrho\,\bigr\},
\]
where \([\cdot]\) takes the middle coordinates. (For such \(t\), also \(\gamma^{-1}t\perp X\).)

## References

1. Lean: `New.link`, `New.linkMatrix` in `src/New/Spanning/Bessel/Basic.lean`.
