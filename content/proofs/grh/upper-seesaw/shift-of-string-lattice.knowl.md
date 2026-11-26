+++
id = "proofs/grh/upper-seesaw/shift-of-string-lattice"
title = "The shift takes Lambda-plus onto a times Lambda-minus of the shorter string"
kind = "lemma"
summary = "The shift from a string of length s to one of length s-1 maps the projected string lattice onto a times the intersected string lattice."
aliases = ["sh Lambda+ = a Lambda'-"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.SpansLattice.map_stringMapFin_latticePlus", "New.powerIdele_eq_mul"]
lean_files = ["src/New/UpperBound/Seesaw/StandardLines.lean"]
proof_status = "full"
+++

**Lemma.** Let \(V,V'\) be [[?c:Hermitian space|hermitian spaces]] over \(E\) with gradings \(Y,Y'\) having strings of
\(s\ge1\) and \(s-1\) vectors, the same parameter \(N\) and the same constant \(c\), which has the
valuation of \(a\bar a\) at every [[algebra-fields-galois/place-of-global-field|finite place]]. Let \((P,N,\pi)\) be a
[[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree factorisation]], and
suppose \(Y\) and \(Y'\) [[proofs/grh/upper-seesaw/graded-lattice-basis|span the lattices]] of
\((a,\pi,(a/\bar a)^{\lfloor(s+2)/2\rfloor})\) and \((a,\pi,(a/\bar a)^{\lfloor(s+1)/2\rfloor})\).
Let \(\operatorname{sh}\) be the [[?lean:New.Grading.stringMapFin|shift]], the
\(\mathbb{A}_{E,f}\)-linear map that kills \(X\sqcup\{y_0\}\) and sends
\(\mathfrak{e}^{i}\mapsto\mathfrak{e}'^{\,i}\) for \(i<s-1\) and \(\mathfrak{e}^{s-1}\mapsto0\). Then
\[
\operatorname{sh}(\Lambda^{+})=a\cdot\Lambda'^{-}.
\]

## Proof

By [[proofs/grh/upper-seesaw/string-sum-lattice-criteria|the criteria in the basis of string powers]],
with \(\ell_i=a^{s-i}\bar a^{-1-i}\) for \(V\) and \(\ell'_i=a^{s-1-i}\bar a^{-1-i}=a^{-1}\ell_i\) for
\(V'\):

* \(\sum t_i\mathfrak{e}^{i}\in\Lambda^{+}\) iff \(t_i\in\ell_i\widehat{\mathcal{O}}\) for
  \(2i+1<s\) and \(t_i\in N^{-1}\ell_i\widehat{\mathcal{O}}\) for \(2i+1\ge s\);
* \(\sum t'_i\mathfrak{e}'^{\,i}\in\Lambda'^{-}\) iff \(t'_i\in\ell'_i\widehat{\mathcal{O}}\) for
  \(2i<s-1\) and \(t'_i\in N^{-1}\ell'_i\widehat{\mathcal{O}}\) for \(2i\ge s-1\) (\(i<s-1\)).

The conditions \(2i+1<s\) and \(2i<s-1\) coincide. Hence for \(i<s-1\): \(t_i\) satisfies the
condition for \(\Lambda^{+}\) iff \(a^{-1}t_i\) satisfies the condition for \(\Lambda'^{-}\).

"\(\subseteq\)": every element of \(\Lambda^{+}\) lies in the span of the string, so it is a string
sum \(\sum t_i\mathfrak{e}^{i}\); its image is
\(\sum_{i<s-1}t_i\mathfrak{e}'^{\,i}=a\sum_{i<s-1}(a^{-1}t_i)\mathfrak{e}'^{\,i}\in a\Lambda'^{-}\).

"\(\supseteq\)": an element of \(\Lambda'^{-}\) is \(\sum_{i<s-1}t_i\mathfrak{e}'^{\,i}\); put
\(t'_i=at_i\) for \(i<s-1\) and \(t'_{s-1}=0\). Then \(\sum t'_i\mathfrak{e}^{i}\in\Lambda^{+}\) and
its shift is \(a\sum t_i\mathfrak{e}'^{\,i}\). \(\blacksquare\)

## References

1. Lean: `New.Grading.SpansLattice.map_stringMapFin_latticePlus` in `src/New/UpperBound/Seesaw/StandardLines.lean`.
