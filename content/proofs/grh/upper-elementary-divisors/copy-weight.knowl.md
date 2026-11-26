+++
id = "proofs/grh/upper-elementary-divisors/copy-weight"
title = "Weight of a monomial in the copies at a copy"
kind = "definition"
summary = "Real weights on the entries of the N generic matrices, built from the vector e_{a'} - e_a, whose weighted degree matches the defect of the rows of the substitution operator."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.rootVector", "New.FrobeniusCycle.indexWeight", "New.FrobeniusCycle.scaledIndexWeight", "New.FrobeniusCycle.entryWeight", "New.FrobeniusCycle.copyWeight", "New.FrobeniusCycle.weight_entryWeight", "New.FrobeniusCycle.abs_entryWeight_le", "New.FrobeniusCycle.abs_scaledIndexWeight_le", "New.FrobeniusCycle.abs_indexWeight_le"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\), let \(a,a'\) be indices below \(k\), \(\ell\ge0\), and \(i\in\mathbb{Z}/N\) (a copy). Let \(\varrho=e_{a'}-e_a\in\mathbb{Z}^{k}\) (for \(a\ne a'\): \(\varrho_{a'}=1\), \(\varrho_a=-1\), other entries \(0\)).

- The **index weight** of \(b\) is \(\varrho_b/P^{\ell}\); the **scaled index weight** at an exponent \(m\) is \(\varsigma_m(b)=\varrho_bP^{m}/(P^{\ell}q)\). For \(m\le N\), \(\lvert\varsigma_m(b)\rvert\le P^{-\ell}\), and \(\varsigma_N(b)=\varrho_b/P^{\ell}\).
- The **entry weight at the copy \(i\)** of the variable \(X_{j,b,c}\) is
\[
\epsilon_i(X_{j,b,c})=\begin{cases}\varrho_b/P^{\ell}&j=i,\\ \varsigma_{[j-i]}(b)-\varsigma_{[j-i]}(c)&j\ne i,\end{cases}
\]
with \([j-i]\in\{0,\dots,N-1\}\). It satisfies \(\lvert\epsilon_i\rvert\le2/P^{\ell}\).
- The **copy weight** of a monomial \(X^{\nu}\) in the entries of all copies is its weighted degree \(\operatorname{cw}_i(\nu)=\sum_{j,b,c}\nu(j,b,c)\,\epsilon_i(X_{j,b,c})\). Writing \(\operatorname{row}_j(\nu)=\sum_{b,c}\nu(j,b,c)\varrho_b\) and \(\operatorname{col}_j(\nu)=\sum_{b,c}\nu(j,b,c)\varrho_c\),
\[
\operatorname{cw}_i(\nu)=\frac1{P^{\ell}}\Bigl(\operatorname{row}_i(\nu)+\sum_{j\ne i}\frac{P^{[j-i]}}{q}\bigl(\operatorname{row}_j(\nu)-\operatorname{col}_j(\nu)\bigr)\Bigr).
\]
(The formal source defines the copy weight by the second formula and proves the equality with the weighted degree.)

## References

1. Lean: `New.rootVector`, `New.FrobeniusCycle.indexWeight`, `New.FrobeniusCycle.scaledIndexWeight`, `New.FrobeniusCycle.entryWeight`, `New.FrobeniusCycle.copyWeight`, `New.FrobeniusCycle.weight_entryWeight`, `New.FrobeniusCycle.abs_entryWeight_le`, `New.FrobeniusCycle.abs_scaledIndexWeight_le`, `New.FrobeniusCycle.abs_indexWeight_le` in `src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean`.
