+++
id = "proofs/grh/upper-seesaw/string-lattices-line-by-line"
title = "The string lattices are sums of lines"
kind = "lemma"
summary = "The intersection of the glued lattice with the span of the string and its projection to that span are sums of lines; they differ only by a factor 1/N at the middle vector."
aliases = ["Lambda minus and Lambda plus", "lattice minus", "lattice plus"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.SpansLattice.mem_latticeMinus_iff", "New.Grading.SpansLattice.mem_latticePlus_iff", "New.Grading.SpansLattice.mem_lattice_and_stringProj_eq_zero_iff", "New.Seesaw.IsSplitSquarefree.v_algebraMap", "New.Seesaw.IsSplitSquarefree.algebraMap_mem_Ô"]
lean_files = ["src/New/UpperBound/Seesaw/StandardLines.lean"]
proof_status = "full"
+++

Keep the notation of
[[proofs/grh/upper-seesaw/standard-lattice-membership|membership in the glued standard lattice]]:
\(\Lambda\) is spanned by the glued lattice basis of \((a,\pi,u)\), with line ideles \(\lambda_b\).
Let \(\operatorname{pr}\) be the projection onto the span of the string along \(X\sqcup\{y_0\}\),
\[
\Lambda^{-}=\Lambda\cap\operatorname{span}(z_0,\dots,z_{s-1}),\qquad \Lambda^{+}=\operatorname{pr}(\Lambda)
\]
([[?lean:New.Grading.latticeMinus|\(\Lambda^-\)]], [[?lean:New.Grading.latticePlus|\(\Lambda^+\)]]).

**Lemma.** Let \(y\in\mathbb{A}_{E,f}^{\iota}\), with coordinates \(y_i\) (\(i\in X\)), \(y_e\) at the distinguished vector \(y_0\), and \(y_b\) at the string vector \(z_b\) (the same convention for \(z\)).

1. \(y\in\Lambda^{-}\) iff \(y\) lies in the span of the string and
   \(\lambda_b^{-1}y_b\in\widehat{\mathcal{O}}\) for all \(b\).
2. Suppose \((P,N,\pi)\) is a
   [[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree factorisation]]. Then
   \(y\in\Lambda^{+}\) iff \(y\) lies in the span of the string,
   \(\lambda_b^{-1}y_b\in\widehat{\mathcal{O}}\) for \(b\ne s-1-b\), and
   \(N\lambda_b^{-1}y_b\in\widehat{\mathcal{O}}\) at the middle index.
3. Under the same hypothesis and for odd \(s\): a vector \(y\) with \(\operatorname{pr}(y)=0\) lies
   in \(\Lambda\) iff \(y_i\in\widehat{\mathcal{O}}\) for \(i\in X\) and
   \(\pi^{-1}y_e\in\widehat{\mathcal{O}}\).

## Proof

(1) For \(y\) in the span of the string, \(y_i=0=y_e\), and the membership criterion reduces to
condition 3 without the gluing term.

(2) Under the hypothesis, \(N\) is a [[?c:Uniformizer|uniformiser]] at the places of \(P\cup\bar P\) and a unit
elsewhere; in particular \(N\in\widehat{\mathcal{O}}\) and \(\bar\pi=N\pi^{-1}\).

If \(y=\operatorname{pr}(z)\) with \(z\in\Lambda\), then for \(b\) not the middle index
\(\lambda_b^{-1}y_b=\lambda_b^{-1}z_b\) is integral, and at the middle index
\(N\lambda_b^{-1}z_b=N(\lambda_b^{-1}z_b-\pi^{-1}z_e)+\bar\pi z_e\) is integral by conditions 3 and
2 of the criterion (a middle index exists only for odd \(s\)).

Conversely let \(y\) satisfy the conditions. If \(s\) is even take \(z=y\). If \(s\) is odd with
middle index \(c\), put \(\eta=\lambda_c^{-1}y_c\) and let \(z\) agree with \(y\) except
\(z_e=\pi\eta\). Then \(\bar\pi z_e=N\eta\in\widehat{\mathcal{O}}\) and
\(\lambda_c^{-1}z_c-\pi^{-1}z_e=\eta-\eta=0\), so \(z\in\Lambda\) and \(\operatorname{pr}(z)=y\).

(3) The string coordinates of \(y\) vanish. Condition 3 of the criterion at the middle index says
\(\pi^{-1}y_e\in\widehat{\mathcal{O}}\); it implies condition 2,
\(\bar\pi y_e=N\cdot\pi^{-1}y_e\in\widehat{\mathcal{O}}\). \(\blacksquare\)

## References

1. Lean: `New.Grading.SpansLattice.mem_latticeMinus_iff`, `New.Grading.SpansLattice.mem_latticePlus_iff`, `New.Grading.SpansLattice.mem_lattice_and_stringProj_eq_zero_iff` in `src/New/UpperBound/Seesaw/StandardLines.lean`.
