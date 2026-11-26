+++
id = "proofs/grh/upper-divisibility/mean-degree-in-one-variable"
title = "Mean degree of the weight basis in one variable"
kind = "lemma"
summary = "The total degree in a given variable of X_0, over all classes and basis vectors of the weight space, is the same for every variable and at most f a / k times the dimension of the source forms."
aliases = ["summed degree in a variable"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.sumDegreeOf", "New.Data.sumDegreeOf_eq", "New.Data.mul_sumDegreeOf_le", "New.colengthDvd_span_pow_monomials", "New.mul_sum_monomials_apply"]
lean_files = ["src/New/UpperBound/Divisibility/ColengthAtLevel.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. A basis vector of the weight space of \(X_0\) is a family of tableaux, one for each infinite place \(\tau\); its degree in a variable \(u\) (a basis vector of \(X_0\)) at \(\tau\) is the number of entries equal to \(u\). The **summed degree** in \(u\) is
\[
l(u)=\sum_{(c,i)}\sum_{\tau\in\Phi}\deg_{u,\tau}(i),
\]
the sum over all pairs of a class \(c\in\Gamma\backslash G_f(X_0)/K_0\) and a basis vector \(i\).

**Lemma.** \(l(u)=l(u')\) for all variables \(u,u'\), and \(k\cdot l(u)\le\dim_{\mathbb{C}}\mathcal S\cdot fa\).

## Proof

*Symmetry.* The Schur matrix of the diagonal matrix \(\operatorname{diag}(1,\dots,2,\dots,1)\) with \(2\) at \(u\) is diagonal with entries \(2^{\sum_\tau\deg_{u,\tau}(i)}\) ([[?lean:New.schur_diagonal|`schur_diagonal`]], quoted). Let \(A\) be this diagonal matrix with columns permuted by the transposition \((u\,u')\) and \(B\) the permutation matrix; then \(AB\) is the diagonal matrix with \(2\) at \(u\) and \(BA\) that with \(2\) at \(u'\). Since \(\det(\mathrm{Schur}(A)\mathrm{Schur}(B))=\det(\mathrm{Schur}(B)\mathrm{Schur}(A))\) and the Schur matrix is multiplicative, the exponents of \(2\) agree: \(\sum_i\sum_\tau\deg_{u,\tau}(i)=\sum_i\sum_\tau\deg_{u',\tau}(i)\). Multiply by the number of classes.

*Mean.* \(X_0\) has \(k\) variables, so \(k\,l(u)=\sum_{u'}l(u')=\sum_{(c,i)}\sum_\tau\sum_{u'}\deg_{u',\tau}(i)\). The total degree of a basis vector at \(\tau\) in all variables is the number of boxes of the diagram in columns of height below \(k\), at most \(a\) ([[proofs/grh/upper-divisibility/short-ramified-source-forms-span|as in the proof that short forms span]]). The number of pairs \((c,i)\) is \(\dim\mathcal S\) because the level of stage \(0\) is free. \(\blacksquare\)

*Status.* The Schur matrix of a diagonal matrix and the total degree of a tableau are quoted.

## Remarks

The source file first treats, as a model not used later, the free module on the monomials \(z^{\alpha}\) of degree \(a\) in \(k\) variables: the span of the \(N^{\alpha_i}z^{\alpha}\) has colength dividing \(N^{\sum_\alpha\alpha_i}\), and \(k\sum_\alpha\alpha_i=a\cdot\#\{\alpha\}\) by symmetry.

## References

1. Lean: `New.Data.sumDegreeOf_eq`, `New.Data.mul_sumDegreeOf_le` in `src/New/UpperBound/Divisibility/ColengthAtLevel.lean`.
