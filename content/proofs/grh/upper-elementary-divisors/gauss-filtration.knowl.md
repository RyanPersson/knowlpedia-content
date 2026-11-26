+++
id = "proofs/grh/upper-elementary-divisors/gauss-filtration"
title = "Real filtrations and the Gauss filtration"
kind = "definition"
summary = "Decreasing multiplicative filtrations of a ring indexed by real numbers, the w-adic filtration, and the Gauss filtration on polynomials with weighted variables."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsRealFiltration", "New.adicFiltration", "New.gaussFiltration", "New.FrobeniusCycle.iteratedGaussFiltration"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/RootLemma.lean"]
+++

Let \(R\) be a commutative ring. A **real filtration** of \(R\) is a family \((F_t)_{t\in\mathbb{R}}\) of additive subgroups of \(R\) with \(1\in F_0\), \(F_s\cdot F_t\subseteq F_{s+t}\), and \(F_t\subseteq F_s\) whenever \(s\le t\).

- **\(w\)-adic filtration.** For \(w\in R\): \(F^{w}_t=\{x\in R: w^{\lceil t\rceil_+}\mid x\}\), where \(\lceil t\rceil_+=\max(\lceil t\rceil,0)\). It is a real filtration because \(\lceil s+t\rceil_+\le\lceil s\rceil_++\lceil t\rceil_+\).
- **Gauss filtration.** For a real filtration \(F\) of \(R\) and real weights \(c=(c_i)_{i\in\sigma}\) of variables: \(\mathrm{G}_t(F,c)\) is the group of polynomials \(f\in R[x_i:i\in\sigma]\) such that for every exponent \(\alpha\), the coefficient of \(x^{\alpha}\) lies in \(F_{t-c\cdot\alpha}\), where \(c\cdot\alpha=\sum_i\alpha_ic_i\). It is a real filtration of the polynomial ring (the coefficient of \(x^{\alpha}\) in \(fg\) is a sum of products of coefficients at \(\beta,\gamma\) with \(\beta+\gamma=\alpha\)).

Informally \(f\in\mathrm{G}_t(F^{w},c)\) says: every term of \(f\) has \(w\)-adic order plus \(c\)-weight at least \(t\). The **iterated Gauss filtration** on \(R[t][x_z]\) with parameters \((c,\rho,v)\) is the Gauss filtration over the Gauss filtration of \(R[t]\) (for \(F^{w}\), with \(t\) of weight \(\rho\)), in which the variable \(x_z\) has weight \(c_z-v_z\rho\).

## Properties

See [[proofs/grh/upper-elementary-divisors/substitution-respects-gauss-filtration|substitution respects weights]].

## References

1. Lean: `New.IsRealFiltration`, `New.adicFiltration`, `New.gaussFiltration`, `New.FrobeniusCycle.iteratedGaussFiltration` in `src/New/UpperBound/ElementaryDivisors/RootLemma.lean`.
