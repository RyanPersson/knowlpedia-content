+++
id = "proofs/grh/spanning-mainterm/coset-labels-for-bounded-denominator"
title = "Numbers with denominator dividing an ideal lie in norm-many cosets of the integers"
kind = "lemma"
summary = "The elements of a number field whose denominator ideal contains a nonzero ideal b can be given N(b) labels so that equal labels differ by an algebraic integer."
aliases = ["exists_coset_label"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_coset_label", "New.exists_mem_algebraMap_eq_mul"]
lean_files = ["src/New/Spanning/MainTerm/Frequencies.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a number field and \(\mathfrak b\) a nonzero ideal of \(\mathcal O_E\)
with [[algebra-fields-galois/ideal-norm|absolute norm]] \(N\mathfrak b\). There is a map
\(\lambda\colon E\to\{1,\dots,N\mathfrak b\}\) such that for all \(\nu,\nu'\in E\) with
\(\mathfrak b\subseteq\mathfrak d(\nu)\) and \(\mathfrak b\subseteq\mathfrak d(\nu')\)
([[proofs/grh/spanning-mainterm/denominator-ideal|denominator ideals]]): if
\(\lambda(\nu)=\lambda(\nu')\) then \(\nu-\nu'\in\mathcal O_E\).

## Proof

Choose \(0\ne a\in\mathfrak b\). Since \(\mathcal O_E\) is a
[[algebra-commutative/dedekind-domain|Dedekind domain]], \(\mathfrak b\) divides \((a)\):
\((a)=\mathfrak b\mathfrak c\) with \(\mathfrak c\ne0\).

*Step 1: if \(\mathfrak b\subseteq\mathfrak d(\nu)\) then \(a\nu\in\mathfrak c\).* Put
\(x=a\nu\in\mathcal O_E\) (as \(a\in\mathfrak b\)). For \(r\in\mathfrak b\) the number
\(y=r\nu\) is an integer and \(ya=xr\), so \(xr\in(a)\). Hence
\(\mathfrak b\cdot(x)\subseteq(a)=\mathfrak b\mathfrak c\), that is
\(\mathfrak b\mathfrak c\mid\mathfrak b\,(x)\); cancelling the nonzero ideal \(\mathfrak b\),
\(\mathfrak c\mid(x)\), i.e. \(x\in\mathfrak c\).

*Step 2: counting.* The additive group \(\mathfrak c/(a)\) has
\([\mathcal O_E:(a)]/[\mathcal O_E:\mathfrak c]=N(\mathfrak b\mathfrak c)/N\mathfrak c=N\mathfrak b\)
elements, by multiplicativity of the norm and \(N\mathfrak c\ne0\). Fix a bijection
\(e\colon\mathfrak c/(a)\to\{1,\dots,N\mathfrak b\}\) and define
\(\lambda(\nu)=e(a\nu\bmod(a))\) when \(\mathfrak b\subseteq\mathfrak d(\nu)\) (and arbitrarily
otherwise).

*Step 3.* If \(\lambda(\nu)=\lambda(\nu')\), then \(a\nu-a\nu'=ta\) for some \(t\in\mathcal O_E\),
and \(a\ne0\) gives \(\nu-\nu'=t\in\mathcal O_E\). \(\blacksquare\)

## References

1. Lean: `New.exists_coset_label`, `New.exists_mem_algebraMap_eq_mul` in
   `src/New/Spanning/MainTerm/Frequencies.lean`.
