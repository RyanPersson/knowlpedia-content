+++
id = "proofs/grh/upper-elementary-divisors/conjugated-frobenius-factors-level"
title = "Gauss level of the conjugated Frobenius factors"
kind = "lemma"
summary = "For small variable weights, each entry of a conjugated Frobenius factor has the same Gauss level as the corresponding power of a variable, the difference being a multiple of p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.conjFrobGenericMatrix_mem_gaussFiltration", "New.FrobeniusCycle.p_dvd_letterConj_pow_sub", "New.FrobeniusCycle.letterConj_mem_gaussFiltration", "New.mem_gaussFiltration_adicFiltration_iff", "New.le_weight_of_mem_gaussFiltration_zero", "New.FrobeniusCycle.X_mem_gaussFiltration"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(h\in\mathrm{GL}_k(W)\), \(s\) a letter, \(d\ge0\), and \(\Psi^{h}_{s,d}\) the [[proofs/grh/upper-elementary-divisors/substitution-operator|conjugated Frobenius factor]].

1. For every \(Y\in M_k(O)\) (or over any commutative \(O\)-algebra with the base-changed cycle) and all \(b,c\): \(p\) divides \(\bigl[\operatorname{conj}_{h,s}\bigl((\operatorname{conj}_{h^{-1},s-d}Y)^{(P^{d})}\bigr)\bigr]_{b,c}-Y_{b,c}^{P^{d}}\).
2. Let \(\omega\) be real weights on the variables \(X_{j,b,c}\) with \(\lvert\omega\rvert\le P^{-d}\). Then \((\Psi^{h}_{s,d})_{b,c}\) lies in the [[proofs/grh/upper-elementary-divisors/gauss-filtration|Gauss level]] \(t=P^{d}\omega(X_{s-d,b,c})\) for \((F^{w},\omega)\): its coefficient at \(X^{\mu}\) is divisible by \(w^{\lceil t-\omega\cdot\mu\rceil_+}\).

## Proof

(1) Work in \(Q=O/pO\). There \(f\colon x\mapsto x^{P^{d}}\) is a ring homomorphism \(O\to Q\) (\(P^{d}\) is a power of \(p\)), and \(f\circ\iota_{s-d}=\pi\circ\iota_s\) by the iterated Frobenius congruence. Let \(A,B\) be the images in \(Q\) of \(\iota_s(h),\iota_s(h^{-1})\); \(AB=BA=1\). Then the image of \((\operatorname{conj}_{h^{-1},s-d}Y)^{(P^{d})}\) is \(B\,f(Y)\,A\), and conjugating by \(h\) through \(\iota_s\) gives \(A(Bf(Y)A)B=f(Y)\), the image of \(Y^{(P^{d})}\).

(2) Let \(M=(\Psi^{h}_{s,d})_{b,c}\). Conjugation by constant matrices preserves Gauss levels, and \(X_v\) has level \(-P^{-d}\) for the weights \(\omega\) over the \(0\)-adic filtration; so every monomial \(X^{\mu}\) occurring in \(M\) has \(\omega\cdot\mu\ge P^{d}\cdot(-P^{-d})=-1\). Also \(t\le1\). Hence for such \(\mu\), \(\lceil t-\omega\cdot\mu\rceil_+\le2\). By (1), \(w^{2}=p\) divides \(M-X_{s-d,b,c}^{P^{d}}\) coefficientwise, and \(X_{s-d,b,c}^{P^{d}}\) lies in level \(t\). So the coefficient of \(M\) at \(\mu\) is divisible by \(w^{\lceil t-\omega\cdot\mu\rceil_+}\); for \(\mu\) not occurring in \(M\) there is nothing to prove. \(\square\)

## References

1. Lean: `New.FrobeniusCycle.conjFrobGenericMatrix_mem_gaussFiltration`, `New.FrobeniusCycle.p_dvd_letterConj_pow_sub`, `New.FrobeniusCycle.letterConj_mem_gaussFiltration`, `New.mem_gaussFiltration_adicFiltration_iff`, `New.le_weight_of_mem_gaussFiltration_zero`, `New.FrobeniusCycle.X_mem_gaussFiltration` in `src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean`.
