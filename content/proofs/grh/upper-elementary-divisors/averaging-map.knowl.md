+++
id = "proofs/grh/upper-elementary-divisors/averaging-map"
title = "The averaging map"
kind = "theorem"
summary = "There is a matrix Av whose values have no term of defect above 9kc modulo w^c in any block diagonal translate, and which preserves the edge pairing with forms in all halfway lattices up to the factor p^(N c_0), modulo w^c."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_average_mem_defectConditions_and_dvd_sub", "New.FrobeniusCycle.partialAverage_univ_mulVec_mem_defectConditions", "New.FrobeniusCycle.pow_dvd_pairing_partialAverage_insert_sub", "New.dvd_map_of_forall_monomial"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/AveragingMap.lean"]
proof_status = "full"
+++

**Theorem.** Let \(O\) be a valuation ring that is a domain of characteristic \(0\), and \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\) with \(p\) not a unit of \(O\). Let \(r=a+1<k\), \(N=2\ell\), and \(n\ge0\) with
\[
N\,k\,(\ell+2)\,n+n+k<P^{\ell}.
\]
Let \((b,b')\) be an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]], \(c_0=k^{2}fN\), and \(c\in\mathbb{N}\), \(c^{*}=3kc\). Then there is a matrix \(\mathrm{Av}\in M_{\mathcal{E}(N,k,n)}(O)\) such that

1. for every \(h\), \(\mathrm{Av}\,h\) satisfies the [[proofs/grh/upper-elementary-divisors/translate-conditions|defect conditions]] for the root \((a,r)\), the ideal \((w^{c})\) and the threshold \(3c^{*}\): for every block diagonal \(g\) and every \(\beta\) with \(\operatorname{def}_{i,a,r}(\beta)>3c^{*}\) for some \(i\), \(w^{c}\mid(\rho_n(g)\mathrm{Av}\,h)_\beta\);
2. for every \(h\) and every \(h'\in\mathcal{A}(k,n,r)\) ([[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|forms in all halfway lattices]]): \(\langle\mathrm{Av}\,h,h'\rangle_b\equiv p^{Nc_0}\langle h,h'\rangle_b\pmod{w^{c}}\).

## Proof

The hypotheses give \(Nnk(\ell+2)\le P^{\ell}\), \(\ell\le N\), and with \(D=Nnk(\ell+2)P^{\ell}\): \(D+k<(Nk(\ell+2)n+1)P^{\ell}\le P^{2\ell}=q\). By the [[proofs/grh/upper-elementary-divisors/existence-of-average|existence of averages]] (with exponent \(fN\), so \(p^{k^{2}fN}=p^{c_0}\), and \(D<p^{fN}\), \(D+k\le q\)), for each \(j\) there is an average \(I_j\) for the block diagonal Levi subgroup, the map \(\iota_j\), the weights \(\varrho=e_r-e_a\), the threshold \(2c^{*}P^{\ell}\), the constant \(p^{c_0}\) and the degree \(D\). Let \(\mathrm{Av}=\mathrm{Av}_{\mathbb{Z}/N}\) be the [[proofs/grh/upper-elementary-divisors/partial-average|partial average]] for all copies.

(1) Let \(g\) be block diagonal and \(\operatorname{def}_{i,a,r}(\beta)>3c^{*}\); write \(i=j+\ell\). By the [[proofs/grh/upper-elementary-divisors/contraction-change-of-frame|change of frame]] (part 2 with \(l=I\), \(m=I_j\), all invariant), \((\rho_n(g)\mathrm{Av}\,h)_\beta=I_j\bigl(\mathcal{C}_j(I;g,h)_\beta\bigr)\). For every monomial \(X^{\alpha}\) of \(\mathcal{C}_j(I;g,h)_\beta\), either its coefficient is divisible by \(w^{c}\), or, by [[proofs/grh/upper-elementary-divisors/weight-and-defect-in-one-copy|weight and defect in one copy]], \(\operatorname{rw}(\alpha)>2c^{*}P^{\ell}\), so \(\alpha\) is bad and \(I_j(X^{\alpha})=0\). Hence \(w^{c}\) divides the value.

(2) We show by induction on \(J\) that \(\langle\mathrm{Av}_Jh,h'\rangle_b\equiv p^{Nc_0}\langle h,h'\rangle_b\) modulo \(w^{c}\); for \(J=\emptyset\) it is an equality. Let \(j\notin J\), let \(l\) be the family defining \(\mathrm{Av}_J\) (all members invariant: evaluation at \(1\) is invariant), and
\[
\psi=\sum_\beta h'_\beta b_\beta\,\mathcal{C}_j(l;1,h)_\beta\in O[X],\qquad\deg\psi\le D .
\]
By the change of frame at \(g=1\), \(m(\psi)=\langle\mathcal{F}(l\text{ with }l_j:=m)h,h'\rangle_b\); so \(I_j(\psi)-\mathrm{ev}(\psi)=\langle\mathrm{Av}_{J\cup\{j\}}h,h'\rangle_b-\langle\mathrm{Av}_Jh,h'\rangle_b\). By the third property of an average with the ideal \((w^{c})\), it suffices that for every block diagonal \(g\) and every bad \(\alpha\), \(w^{c}\) divides the coefficient of \(X^{\alpha}\) in \(c^{(j)}_g\psi\). By part 3 of the change of frame, that coefficient is
\[
\sum_\beta[X^{\alpha}]\,\mathcal{C}_j(l;g,h)_\beta\cdot\bigl\langle\rho_n(g^{-1})e_\beta,h'\bigr\rangle_b .
\]
For each \(\beta\): either \(w^{c}\) divides the first factor, or by weight and defect in one copy (second implication, \(\alpha\) bad) \(\operatorname{def}_{j+\ell,a,r}(\beta)>c^{*}\), and then \(w^{c}\) divides the second factor by [[proofs/grh/upper-elementary-divisors/halfway-forms-divisible-at-large-defect|the divisibility of the pairing at large defect]] (part 3; \(g^{-1}\) is block diagonal and \(a<r\)). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_average_mem_defectConditions_and_dvd_sub`, `New.FrobeniusCycle.partialAverage_univ_mulVec_mem_defectConditions`, `New.FrobeniusCycle.pow_dvd_pairing_partialAverage_insert_sub`, `New.dvd_map_of_forall_monomial` in `src/New/UpperBound/ElementaryDivisors/AveragingMap.lean`.
2. Related work named in the head of the Lean file: Benson–Doty, Schur–Weyl duality over finite fields, 2009; J. A. Green, Polynomial representations of GL_n, 1980; S. Donkin, On Schur algebras and related algebras I, 1986.
