+++
id = "proofs/grh/upper-elementary-divisors/weight-and-defect-in-one-copy"
title = "Weight and defect in one copy"
kind = "lemma"
summary = "If the forms in the other copies are invariant under the Levi subgroup, a monomial alpha of the polynomial left in copy j whose coefficient is not divisible by w^c has row weight over P^l within 3kc of the defect of the row at the letter j + l."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.abs_weight_div_sub_defect_le", "New.FrobeniusCycle.lt_weight_and_lt_defect_of_not_dvd_coeff_contractOtherCopies", "New.exists_of_not_dvd_coeff_tensorDualExcept"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/AveragingMap.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be an integral domain of characteristic \(0\), \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), with \(p\) not a unit of \(O\). Let \(r=a+1<k\), \(\ell\le N\), \(N\,n\,k\,(\ell+2)\le P^{\ell}\), and let the linear forms \(l_i\) on \(O[X]\) be invariant under conjugation (through \(\iota_i\)) by all block diagonal \(u\) (blocks \(\{b<r\},\{b\ge r\}\)). Let \(j\) be a copy, \(g\in\mathrm{GL}_k(W)\), \(h\in O^{\mathcal{E}}\), and suppose \(w^{c}\) does not divide the coefficient of \(X^{\alpha}\) in \(\mathcal{C}_j(l;g,h)_\beta\) ([[proofs/grh/upper-elementary-divisors/partial-average|notation]]). Let \(\operatorname{rw}(\alpha)=\sum_{b,c}\alpha(b,c)\varrho_b\) be the row weight for \(\varrho=e_r-e_a\), \(\Delta=\operatorname{def}_{j+\ell,a,r}(\beta)\), and \(c^{*}=3kc\). Then

1. \(\bigl\lvert\operatorname{rw}(\alpha)/P^{\ell}-\Delta\bigr\rvert\le c^{*}\);
2. if \(\Delta>3c^{*}\) then \(\operatorname{rw}(\alpha)>2c^{*}P^{\ell}\); and if \(\operatorname{rw}(\alpha)>2c^{*}P^{\ell}\) then \(\Delta>c^{*}\).

## Proof

(1) By the definition of \(\mathcal{C}_j\), there are \(\gamma\) and a monomial \(\prod_iX_i^{\nu_i}\) with \(\nu_j=\alpha\), whose coefficient in \(\mathcal{S}(r,\ell,n;\Psi^{g})_{\beta\gamma}\) is not divisible by \(w^{c}\), and with \(l_i(X^{\nu_i})\ne0\) for all \(i\ne j\) (otherwise every contribution to the coefficient is divisible by \(w^{c}\) or zero). By [[proofs/grh/upper-elementary-divisors/invariant-forms-vanish-on-unbalanced-monomials|the lemma on unbalanced monomials]], for \(i\ne j\) the row and column weights of \(\nu_i\) for \(\varrho\) agree; hence the [[proofs/grh/upper-elementary-divisors/copy-weight|copy weight]] is \(\operatorname{cw}_j(\nu)=\operatorname{rw}(\alpha)/P^{\ell}\). Now apply [[proofs/grh/upper-elementary-divisors/weight-and-defect|weight against defect]].

(2) Immediate from (1). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.abs_weight_div_sub_defect_le`, `New.FrobeniusCycle.lt_weight_and_lt_defect_of_not_dvd_coeff_contractOtherCopies`, `New.exists_of_not_dvd_coeff_tensorDualExcept` in `src/New/UpperBound/ElementaryDivisors/AveragingMap.lean`.
