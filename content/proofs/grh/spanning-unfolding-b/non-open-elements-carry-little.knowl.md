+++
id = "proofs/grh/spanning-unfolding-b/non-open-elements-carry-little"
title = "Elements that are not open carry a small part of a positive type sum"
kind = "lemma"
summary = "For a nonnegative function of positive type on the residue group and a subgroup in which stabilisers of frame vectors at one place carry at most a proportion b^(-6k), the elements that are not open carry at most a proportion b^(-4)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.sum_not_isOpenElement_le", "New.Filling.sum_leadingMinor_eq_zero_le", "New.Filling.levelPrime_pow_mul_sqrt_le"]
lean_files = ["src/New/Spanning/Unfolding/MomentBounds.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. Let \(\beta\colon\bar G\to\mathbb{R}_{\ge0}\) be of [[?c:Positive-definite function on a group|positive type]]: \(\beta(a^{-1}b)=\langle u_a,u_b\rangle\) for vectors \(u_a\) of a complex inner product space. Let \(\Gamma\subset\bar G\) be a subgroup, \(w\in C_0\) a chosen place above \(p_0\), and suppose that for every frame vector \(d\) at \(w\) (a nonzero vector of the span of the frame modulo \(w\) or its conjugate) the [[?lean:New.Filling.vectorFixer|stabiliser]] of \(d\) satisfies
\[
\sum_{s\in\Gamma,\ s\text{ fixes }d}\beta(s)\le b^{-6k}\sum_{s\in\Gamma}\beta(s).
\]
Then:

1. for every \(0\le l<n\), with \(\delta_l(s)\) the leading minor of order \(l\) of the frame products of \(s_w\) for the form in the lattice basis modulo \(w\),
\[
\sum_{s\in\Gamma,\ \delta_l(s)=0}\beta(s)\le3\,b^{-10}\sum_{s\in\Gamma}\beta(s);
\]
2. \(\displaystyle\sum_{s\in\Gamma,\ s\text{ not open}}\beta(s)\le b^{-4}\sum_{s\in\Gamma}\beta(s)\).

## Proof

Let \(\mathbb{F}=\mathbb{F}_w\), of cardinality \(q=p_0\), \(J\) the Gram matrix in the lattice basis over \(\mathbb{F}\) (symmetric, by [[proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular|unimodularity]]), and \(e\) the \(r\times l\) matrix whose columns are the first \(l\) frame vectors. Then \(\delta_l(s)=\det\bigl((Je)^{\mathsf T}s_we\bigr)\). Put \(\Sigma=\sum_{s\in\Gamma}\beta(s)\).

(1) Apply the [[?lean:New.card_mul_sum_det_eq_zero_le|determinant sieve for functions of positive type]] to the representation \(s\mapsto s_w\) of \(\Gamma\) on \(\mathbb{F}^r\), with \(A_0=e\), \(A_1=Je\) and \(Y=b^{-6k}\Sigma\): if, for every \(v\ne0\) in \(\mathbb{F}^l\), the \(s\) with \(s_w(ev)=ev\) and the \(s\) with \(s_w^{-\mathsf T}(Jev)=Jev\) each carry at most \(Y\), then
\[
q\sum_{\delta_l(s)=0}\beta(s)\le2\Sigma+q^{\,l}\sqrt{q^{\,r}}\;Y .
\]
The hypotheses hold: \(ev\) is a nonzero vector of the span of the frame, so the first set is the stabiliser of the frame vector \((\text{modulo }w,v)\); and \(s_w^{-\mathsf T}Jev=Jev\) says that the inverse adjoint \(J^{-1}s_w^{-\mathsf T}J\), which is the action of \(s\) modulo the conjugate of \(w\), fixes \(ev\), so the second set is the stabiliser of the frame vector \((\text{modulo }\bar w,v)\). Next, \(q^l\sqrt{q^r}\le b^{6k}\): squaring, \(p_0^{2l+r}\le b^{11(2l+r)}\) and \(11(2l+r)=11(2l+2\varrho+k+1)\le12k\) because \(l\le\varrho\) and \(1000(2\varrho+2)\le k\). Hence \(q\sum_{\delta_l=0}\beta\le3\Sigma\), and \(q=p_0\ge b^{10}\).

(2) If \(s\) is not open, then at every place of \(C_0\), in particular at \(w\), some \(\delta_l(s)\) with \(l<n\) vanishes. So the sum over non-open elements is at most \(\sum_{l<n}\sum_{\delta_l(s)=0}\beta(s)\le3n\,b^{-10}\Sigma\le3b\cdot b^{-10}\Sigma\le b^{-4}\Sigma\), using \(n\le b\) and \(3\le b^5\).

## References

1. Lean: `New.Filling.sum_not_isOpenElement_le`, `New.Filling.sum_leadingMinor_eq_zero_le`, `New.Filling.levelPrime_pow_mul_sqrt_le` in `src/New/Spanning/Unfolding/MomentBounds.lean`; `New.card_mul_sum_det_eq_zero_le` in `src/New/Spanning/SecondMoment/PositiveType.lean`.
