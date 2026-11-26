+++
id = "proofs/grh/upper-elementary-divisors/least-height-term-at-a-flag"
title = "A term of least height occurs at a flag and has nonpositive defects"
kind = "lemma"
summary = "In characteristic p, for a Levi subgroup L and representatives R of the cosets of its lower Iwahori subgroup, some translate of a nonzero polynomial by an element of R has a term of defect at most 0 along all simple roots inside the blocks."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_coeff_ne_zero_weight_defectWeight_nonpos", "New.FrobeniusCycle.coeff_polyAction_of_mem_parahoric", "New.FrobeniusCycle.polyAction_X_sub_mem_gaussFiltration"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,K)\), \(N\ge1\), with \(K\) a field of characteristic \(p\). Let \(\tau\) be a labelling of \(\{0..k-1\}\), \(L=L_\tau(W)\) its Levi subgroup, \(\mathrm{Iw}^{-}\subseteq\mathrm{GL}_k(W)\) the lower Iwahori subgroup (matrices with \(g_{ij}\) in the maximal ideal for \(i<j\)), and \(R\subseteq L\) a set such that every \(g\in L\) is uniquely \(g=yx\) with \(y\in\mathrm{Iw}^{-}\cap L\), \(x\in R\). For every nonzero \(f\in K[x_{b,s}]\) there are \(x\in R\) and an exponent \(\alpha\) such that \(x^{\alpha}\) occurs in \(x\cdot f\) and
\[
\operatorname{def}_{i,b,b+1}(\alpha)\le0\quad\text{for all letters }i\text{ and all }b\text{ with }\tau(b)=\tau(b+1).
\]

## Proof

Let the **height** of \(x_{b,s}\) be \(b\) for even and \(-b\) for odd \(s\), and the height of a monomial the sum over its variables.

*Triangularity.* Let \(y\in\mathrm{Iw}^{-}\). Then \(y\cdot x_{b,s}=d\,x_{b,s}+(\text{a combination of variables of height}\ge\operatorname{height}(x_{b,s})+1)\), with \(d=(y_s)_{bb}\): the coefficient of \(x_{c,s}\) is \((y_s)_{c,b}\), which is divisible by \(p=0\) in \(K\) when \(c<b\) (even \(s\)) or \(c>b\) (odd \(s\)), by [[proofs/grh/upper-elementary-divisors/maps-of-cycle-kill-maximal-ideal|the lemma on parahoric elements]]. Consequently, if all monomials of \(f'\) have height at least that of \(x^{\alpha}\), the coefficient of \(x^{\alpha}\) in \(y\cdot f'\) is \(\prod_ud_u^{\alpha(u)}\) times its coefficient in \(f'\) (apply [[proofs/grh/upper-elementary-divisors/substitution-respects-gauss-filtration|the substitution lemma]] with \(w=0\), comparing \(y\) with its diagonal part).

*Choice.* The exponents occurring in translates \(g\cdot f\), \(g\in L\), form a finite nonempty set (degrees are bounded by \(\deg f\)); choose \(\alpha\) of least height in it, occurring in \(g\cdot f\), and write \(g=yx\). All monomials of \(x\cdot f\) have height \(\ge\) that of \(\alpha\), so by triangularity the coefficient of \(x^{\alpha}\) in \(g\cdot f=y\cdot(x\cdot f)\) is a multiple of its coefficient in \(x\cdot f\); hence \(x^{\alpha}\) occurs in \(x\cdot f\).

*Defects.* Let \(\tau(b)=\tau(b+1)\). The heights rise by exactly \(1\) from \(X_s\) to \(Y_s\) for the root \((b,b+1)\), in every letter. The \(\mathrm{SL}_2\) of this root lies in \(L\), so all its translates of \(x\cdot f\) are translates of \(f\) by \(L\) and have only monomials of height \(\ge\) that of \(\alpha\). The characteristic-\(p\) form of the [[proofs/grh/upper-elementary-divisors/root-lemma|root lemma]] gives \(\operatorname{def}_{i,b,b+1}(\alpha)\le0\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_coeff_ne_zero_weight_defectWeight_nonpos`, `New.FrobeniusCycle.coeff_polyAction_of_mem_parahoric`, `New.FrobeniusCycle.polyAction_X_sub_mem_gaussFiltration` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
2. Related work named in the head of the Lean file: Forrester–Zhang, Corank-1 projections and the randomised Horn problem, 2021 (after Dixon, 1905; Anderson, 1991); E. Bombieri, Counting points on curves over finite fields, Séminaire Bourbaki 430, 1973; A. Okounkov, Brunn–Minkowski inequality for multiplicities, 1996.
