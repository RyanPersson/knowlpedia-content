+++
id = "proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms"
title = "Few forms have only deep translates"
kind = "theorem"
summary = "Over a field of characteristic p, the dimensions of the spaces of forms all of whose translates have depth at least 1, 2, ..., M add up to at most N n (P^(-2r) + r^2/(kP)) times the number of exponents."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.sum_finrank_deepForms_le", "New.FrobeniusCycle.divisorConstant", "New.FrobeniusCycle.divisorConstant_map", "New.FrobeniusCycle.sum_deepIndicator_div_le", "New.mul_sum_exponentOf", "New.finrank_le_card_of_forall_exists_ne_zero"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Depth.lean"]
proof_status = "full"
+++

For a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] \(T\) and natural numbers \(k>0\), \(n\), \(r\), the **divisor constant** is the real number
\[
\Delta_T(k,n,r)=N\,n\Bigl(\frac1{P^{2r}}+\frac{r^{2}}{k\,P}\Bigr).
\]
It depends on \(T\) only through \(P\) (and \(N\)), so it is unchanged by base change of the cycle. (For \(k=0\) the formal source reads the second summand as \(0\); this case is not used.)

**Theorem.** Let \(T\) be a Frobenius cycle for \((N,W,K)\), \(N\ge1\), with \(K\) a field of characteristic \(p\), and let \(0<2r\le k\), \(n\ge0\). For every \(M\ge0\),
\[
\sum_{d=1}^{M}\dim_K\mathcal{D}_n(r,d)\ \le\ \Delta_T(k,n,r)\cdot\#\mathcal{E}(N,k,n),
\]
where \(\mathcal{D}_n(r,d)\) is the space of [[proofs/grh/upper-elementary-divisors/translate-conditions|deep forms]] and \(\#\mathcal{E}(N,k,n)=\binom{n+k-1}{k-1}^{N}\) is the number of exponents.

## Proof

Let \(c(v)=1/\kappa(v)\) for deep \(v\) and \(c(v)=0\) otherwise, and \(\operatorname{cost}(\beta)=\sum_v\beta(v)c(v)\ge0\). By the theorem on [[proofs/grh/upper-elementary-divisors/deep-forms-have-heavy-monomial|heavy monomials]], every nonzero \(F\in\mathcal{D}_n(r,d)\) is nonzero at some \(\beta\) with \(\operatorname{cost}(\beta)\ge d\). Hence restriction to the set \(\{\beta:\lfloor\operatorname{cost}\beta\rfloor\ge d\}\) is injective on \(\mathcal{D}_n(r,d)\), and \(\dim\mathcal{D}_n(r,d)\le\#\{\beta:\lfloor\operatorname{cost}\beta\rfloor\ge d\}\). Summing over \(1\le d\le M\) and exchanging the sums, each \(\beta\) is counted at most \(\lfloor\operatorname{cost}\beta\rfloor\le\operatorname{cost}(\beta)\) times:
\[
\sum_{d=1}^{M}\dim\mathcal{D}_n(r,d)\le\sum_\beta\operatorname{cost}(\beta)=\sum_vc(v)\sum_\beta\beta(v).
\]
By symmetry under permuting the indices \(b\) within a letter, \(\sum_\beta\beta(b,s)\) does not depend on \(b\), and \(\sum_b\beta(b,s)=n\); so \(\sum_\beta\beta(v)=\#\mathcal{E}\cdot n/k\) (here \(k>0\)). Finally each index \(b\) is deep in \(\lfloor N/2\rfloor\) letters, at most \(k\) indices have \(b\ge2r\) and exactly \(2r\) have \(b<2r\), so
\[
\sum_vc(v)\le k\cdot\frac{N/2}{P^{2r}}+2r\cdot\frac{N/2}{P}\le N\Bigl(\frac{k}{P^{2r}}+\frac{r^{2}}{P}\Bigr),
\]
using \(r\le r^{2}\). Multiplying by \(\#\mathcal{E}\,n/k\) gives \(\Delta_T(k,n,r)\cdot\#\mathcal{E}\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.sum_finrank_deepForms_le`, `New.FrobeniusCycle.divisorConstant`, `New.FrobeniusCycle.divisorConstant_map`, `New.FrobeniusCycle.sum_deepIndicator_div_le`, `New.mul_sum_exponentOf`, `New.finrank_le_card_of_forall_exists_ne_zero` in `src/New/UpperBound/ElementaryDivisors/Depth.lean`.
