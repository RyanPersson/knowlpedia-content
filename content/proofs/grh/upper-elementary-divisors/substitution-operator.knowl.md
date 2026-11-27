+++
id = "proofs/grh/upper-elementary-divisors/substitution-operator"
title = "Substitution operator of Frobenius powers of generic matrices"
kind = "construction"
summary = "The operator on forms obtained by letting, on each letter s, the product of given k x k factors (or its cofactor matrix on odd letters) act, with one more factor on the deep rows; used with entrywise P^d-th powers of generic matrices."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.frobGenericMatrix", "New.FrobeniusCycle.parityCofactor", "New.FrobeniusCycle.substitutionLetterMatrix", "New.FrobeniusCycle.substitutionOperator", "New.FrobeniusCycle.letterConj", "New.FrobeniusCycle.conjFrobGenericMatrix", "New.FrobeniusCycle.conjFrobGenericMatrix_one", "New.FrobeniusCycle.substitutionOperator_one", "New.FrobeniusCycle.substitutionOperator_frobeniusCycle_map"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\) with \(N\ge1\), let \(R\) be a commutative ring and \(k,r,\ell,n\ge0\).

- **Parity cofactor.** For a letter \(s\) and \(M\in M_k(R)\): \(\operatorname{pc}_s(M)=M\) if \(s\) is even, and \(\operatorname{pc}_s(M)={}^{t}\!\operatorname{adj}(M)\) (the cofactor matrix) if \(s\) is odd.
- **Letter matrix.** For a family of **factors** \(\psi_{s,d}\in M_k(R)\) (\(s\in\mathbb{Z}/N\), \(d\in\mathbb{N}\)), \(\Sigma_s=\Sigma_s(r,\ell,\psi)\in M_k(R)\) is the matrix whose row \(b\) is row \(b\) of
\[
\operatorname{pc}_s\bigl(\psi_{s,m-1}\,\psi_{s,m-2}\cdots\psi_{s,0}\bigr),\qquad m=\ell+\delta_r(b,s),
\]
i.e. \(m=\ell+1\) if the variable \(x_{b,s}\) is [[proofs/grh/upper-elementary-divisors/depth-of-monomial|deep for \(r\)]] and \(m=\ell\) otherwise.
- **Substitution operator.** \(\mathcal{S}(r,\ell,n;\psi)=\bigotimes_{s}\operatorname{Sym}^n(\Sigma_s)\in M_{\mathcal{E}(N,k,n)}(R)\). It depends on \(T\) only through the parities. If all \(\psi_{s,d}=1\), it is the identity.
- **Generic factors.** Let \(R=O[X_{j,b,c}:j\in\mathbb{Z}/N,\ 0\le b,c<k]\), the polynomial ring in the entries of \(N\) generic matrices \(X_j=(X_{j,b,c})_{b,c}\) (the **copies**). The Frobenius factors are \(\Psi_{s,d}=\bigl(X_{s-d,b,c}^{P^{d}}\bigr)_{b,c}\): the copy \(s-d\) with entries raised to the power \(P^{d}\).
- **Change of frame.** For \(h\in\mathrm{GL}_k(W)\) and a letter \(s\), \(\operatorname{conj}_{h,s}(M)=\iota_s(h)\,M\,\iota_s(h)^{-1}\) (also for matrices of polynomials over \(O\)). The conjugated Frobenius factors are
\[
\Psi^{h}_{s,d}=\operatorname{conj}_{h,s}\Bigl(\bigl(\operatorname{conj}_{h^{-1},s-d}(X_{s-d})\bigr)^{(P^{d})}\Bigr),
\]
where \((\cdot)^{(P^{d})}\) raises every entry to the power \(P^{d}\). For \(h=1\), \(\Psi^{1}=\Psi\).

## Remarks

For a general cycle the twists \(\iota_s(g)\) need not be polynomial in \(g\); the relation that is guaranteed is that modulo \(p\) they are entrywise powers of one another. So one takes one generic matrix per letter and lets the copy \(s-d\), \(0\le d\le\ell\), act on the letter \(s\) through its entrywise \(P^{d}\)-th power, the last factor (\(d=\ell\)) acting on the deep variables only. Matrices act on coefficient vectors, so they are the transposes of the matrices substituted in the variables.

## References

1. Lean: `New.FrobeniusCycle.frobGenericMatrix`, `New.FrobeniusCycle.parityCofactor`, `New.FrobeniusCycle.substitutionLetterMatrix`, `New.FrobeniusCycle.substitutionOperator`, `New.FrobeniusCycle.letterConj`, `New.FrobeniusCycle.conjFrobGenericMatrix`, `New.FrobeniusCycle.conjFrobGenericMatrix_one`, `New.FrobeniusCycle.substitutionOperator_one`, `New.FrobeniusCycle.substitutionOperator_frobeniusCycle_map` in `src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean`.
