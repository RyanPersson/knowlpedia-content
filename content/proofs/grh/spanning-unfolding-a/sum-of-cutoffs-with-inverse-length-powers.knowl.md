+++
id = "proofs/grh/spanning-unfolding-a/sum-of-cutoffs-with-inverse-length-powers"
title = "Sums of class cutoffs over terms, weighted by inverse powers of the length"
kind = "proposition"
summary = "Over all classes d and all terms gamma over (c, s, d), the cutoffs beta_d(gamma^-1 y) times P(gamma^-1 y)^(-r^3 f) add up to at most 2 b^(12 n^3 r f), uniformly in y."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_classCutoff_mul_inv_pow_le", "New.Filling.tsum_classCutoff_mul_const_mul_inv_pow_le"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity with \(f\) [[?c:Infinite place of a number field|infinite places]], and \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]]; \(b\) its parameter, \(n=\varrho+1\), \(r\) the rank of \(V\). Let \(T\) be any set of rational [[?c:Isometry of a hermitian space|isometries]], \(c\) a class, \(s\) an element of the [[?lean:New.Filling.ResidueGL|residue group]], and \(y\in G_\infty\). Then
\[
\sum_{d}\ \sum_{\gamma\in T\cap\mathcal T(c,s,d)}\beta_d(\gamma^{-1}y)\;P(\gamma^{-1}y)^{-r^{3}f}\ \le\ 2\,b^{12n^{3}rf},
\]
where \(d\) runs over the classes, \(\mathcal T(c,s,d)\) is the set of [[?lean:New.Filling.termsOver|terms]] over \((c,s,d)\), \(\beta_d\) is the [[?lean:New.Filling.classCutoff|class cutoff]] and \(P\) the [[proofs/grh/spanning-unfolding-a/scaled-bessel-length-product|product of the scaled Bessel lengths]]. The same holds with both sides multiplied by a constant \(A\in[0,\infty]\).

## Proof

Index the sum by pairs \(p=(d,\gamma)\), with weight \(w_p=\beta_d(\gamma^{-1}y)\) and \(u(p)=P(\gamma^{-1}y)\ge1\).

*Counting in layers.* Fix \(R\ge1\) and consider the pairs with \(u(p)\le R\) and \(w_p\ne0\). For these, each component of \(\gamma^{-1}y\) has Bessel length at most \(b^{6n}R\le b^{6n+2}R\). Apply the lemma on [[proofs/grh/spanning-unfolding-a/packing-of-weights|packing of weights]] with \(x=1\) and \(\mathcal V\) the whole space of families of \(n\) vectors of \(\mathbb C^{r}\) at each of the \(f\) places, of real dimension \(2nrf\): the pairs \((d,\gamma)\) are distinct, \(\gamma\) is a term over \((c,s,d)\), and \(w_p\le\beta_d(\gamma^{-1}y)\cdot1\). Hence
\[
\sum_{p:\ u(p)\le R}w_p\le\bigl(b^{6n^2}R^2\bigr)^{2nrf}.
\]

*Summation.* By [[proofs/grh/spanning-unfolding-a/summation-by-layers|summation by layers]] with \(K=b^{6n^2}\), \(e=2\), \(d=2nrf\) and \(i=r^{3}f\), the sum is at most \(2K^{d}=2b^{12n^3rf}\), provided \(2\cdot2\cdot2nrf<r^3f\), i.e. \(8n<r^2\). This holds since \(r\ge2\varrho+1\) and \(\varrho\ge10^5\).

## References

1. Lean: `New.Filling.tsum_classCutoff_mul_inv_pow_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.tsum_classCutoff_mul_const_mul_inv_pow_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
