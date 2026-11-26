+++
id = "proofs/grh/upper-elementary-divisors/contraction-change-of-frame"
title = "Change of frame for contractions of the substitution operator"
kind = "lemma"
summary = "For block diagonal g, conjugating the linear forms by g corresponds to passing to the frame g; in particular the polynomial left in one copy transforms by conjugation of that copy and translation by g."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.letterRep_mul_frobContraction", "New.FrobeniusCycle.map_contractOtherCopies", "New.FrobeniusCycle.map_contractOtherCopies_one", "New.FrobeniusCycle.conjSubst_contractOtherCopies_one", "New.FrobeniusCycle.contractOtherCopies_one_mem_restrictTotalDegree"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/AveragingMap.lean"]
proof_status = "full"
+++

**Lemma.** Notation of [[proofs/grh/upper-elementary-divisors/partial-average|contractions]]. Let \(g\in\mathrm{GL}_k(W)\) be block diagonal for \(\{b<r\},\{b\ge r\}\), and let \(c^{(j)}_g\) be [[proofs/grh/upper-elementary-divisors/conjugation-invariant-average|conjugation]] \(X\mapsto\iota_j(g^{-1})X\iota_j(g)\) on \(O[X]\).

1. If \(m_j=l_j\circ c^{(j)}_g\) for all \(j\), then \(\rho_n(g)\,\mathcal{F}(m)=\bigl(\bigotimes_jl_j\bigr)\bigl(\mathcal{S}(r,\ell,n;\Psi^{g})\bigr)\,\rho_n(g)\).
2. If every \(l_i\) is invariant under \(c^{(i)}_g\), then for every linear form \(m\) on \(O[X]\): \(m\bigl(\mathcal{C}_j(l;g,h)_\beta\bigr)=\bigl(\rho_n(g)\,\mathcal{F}(l')\,h\bigr)_\beta\), where \(l'\) is \(l\) with \(l_j\) replaced by \(m\circ c^{(j)}_g\). For \(g=1\) (no hypothesis on \(l\)): \(m(\mathcal{C}_j(l;1,h)_\beta)=(\mathcal{F}(l\text{ with }l_j:=m)\,h)_\beta\).
3. Under the hypothesis of 2, \(c^{(j)}_g\bigl(\mathcal{C}_j(l;1,h)_\gamma\bigr)=\sum_\beta\rho_n(g^{-1})_{\gamma\beta}\,\mathcal{C}_j(l;g,h)_\beta\).
4. Each \(\mathcal{C}_j(l;1,h)_\beta\) has total degree at most \(N\,n\,k\,(\ell+2)\,P^{\ell}\).

## Proof

(1) Let \(\operatorname{conj}\) be the endomorphism of \(O[X_\bullet]\) applying \(c^{(j)}_g\) in each copy \(j\); then \(\bigotimes m_j=(\bigotimes l_j)\circ\operatorname{conj}\) (check on monomials). Applying \(\operatorname{conj}\) to the entries of the copy \(X_s\) gives \(\iota_s(g^{-1})X_s\iota_s(g)\), so by [[proofs/grh/upper-elementary-divisors/substitution-operator-conjugation|conjugation of the factors]] (with \(\chi=\operatorname{conj}\), \(h=g\)): \(\operatorname{conj}(\mathcal{S}(\Psi))=\rho_n(g^{-1})\mathcal{S}(\Psi')\rho_n(g)\) with \(\Psi'_{s,d}=\operatorname{conj}_{g,s}(\operatorname{conj}(\Psi_{s,d}))=\Psi^{g}_{s,d}\). Apply \(\bigotimes l_j\) entrywise (it commutes with multiplication by constant matrices) and multiply by \(\rho_n(g)\) on the left.

(2) \(m(\mathcal{C}_j(l;g,h)_\beta)=\sum_\gamma\bigl[(\bigotimes l^{m})(\mathcal{S}(\Psi^{g}))\bigr]_{\beta\gamma}(\rho_n(g)h)_\gamma\) with \(l^{m}\) = \(l\) with \(m\) at \(j\). Put \(l'_i=l^{m}_i\circ c^{(i)}_g\) (equal to \(l_i\) for \(i\ne j\) by invariance) and apply (1).

(3) Take coefficients at \(X^{\alpha}\): by (2) with \(m=[X^{\alpha}]\), the coefficient of \(\mathcal{C}_j(l;g,h)_\beta\) is \((\rho_n(g)v)_\beta\) with \(v=\mathcal{F}(l\text{ with }[X^{\alpha}]\circ c^{(j)}_g\text{ at }j)h\), and by (2) for \(g=1\) the coefficient of \(c^{(j)}_g(\mathcal{C}_j(l;1,h)_\gamma)\) is \(v_\gamma=(\rho_n(g^{-1})\rho_n(g)v)_\gamma\).

(4) By the [[proofs/grh/upper-elementary-divisors/levels-of-substitution-operator|degree bound]] for the entries of \(\mathcal{S}(\Psi)\) in each copy. \(\square\)

## References

1. Lean: `New.FrobeniusCycle.letterRep_mul_frobContraction`, `New.FrobeniusCycle.map_contractOtherCopies`, `New.FrobeniusCycle.map_contractOtherCopies_one`, `New.FrobeniusCycle.conjSubst_contractOtherCopies_one`, `New.FrobeniusCycle.contractOtherCopies_one_mem_restrictTotalDegree` in `src/New/UpperBound/ElementaryDivisors/AveragingMap.lean`.
