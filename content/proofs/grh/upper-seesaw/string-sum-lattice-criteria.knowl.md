+++
id = "proofs/grh/upper-seesaw/string-sum-lattice-criteria"
title = "The string lattices in the basis of string powers"
kind = "lemma"
summary = "For the scale u = (a/a-bar)^floor((s+2)/2), a combination of the string powers lies in Lambda-minus or Lambda-plus iff each coefficient lies in an explicit fractional ideal."
aliases = ["power ideles"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.powerIdele", "New.lineIdele_divStar_pow", "New.Grading.lineIdele_inv_mul_stringSum_mem_iff", "New.Grading.SpansLattice.stringSum_mem_latticeMinus_iff", "New.Grading.SpansLattice.stringSum_mem_latticePlus_iff"]
lean_files = ["src/New/UpperBound/Seesaw/StandardLines.lean"]
proof_status = "full"
+++

Keep the notation of
[[proofs/grh/upper-seesaw/string-lattices-line-by-line|the string lattices]]. Let
\(\mathfrak{e}^{0},\dots,\mathfrak{e}^{s-1}\) be the
[[?lean:New.Grading.stringPower|string powers]] of the grading \(Y\): \(\mathfrak{e}^{i}\) is a
multiple \(p_iz_i\) of \(z_i\), where \(p_i=c^{\,i-\lfloor s/2\rfloor}\) if \(2i<s\) and \(p_i=-N\,c^{\,i-\lfloor(s-1)/2\rfloor}\) if \(2i\ge s\), with \(c=c_Y\in E^{\times}\) the constant of the grading. For \(t\colon\mathbb{N}\to\mathbb{A}_{E,f}\) write
\(\sum_i t_i\mathfrak{e}^{i}\) for the [[?lean:New.Grading.stringSum|string sum]] (over \(i<s\)).
Define the **power ideles**
\[
\ell_i=a^{\,s-i}\,\bar a^{\,-1-i}\qquad(i\ge0).
\]

**Lemma.** Suppose \(Y\) spans the lattice of \((a,\pi,u)\) with the scale
\(u=(a/\bar a)^{\lfloor(s+2)/2\rfloor}\), and that \(c\) has the valuation of \(a\bar a\) at every
[[algebra-fields-galois/place-of-global-field|finite place]]. Then:

1. \(\sum_it_i\mathfrak{e}^{i}\in\Lambda^{-}\) iff for all \(i<s\):
   \(t_i\in\ell_i\widehat{\mathcal{O}}\) if \(2i<s\) (grade \(>0\), or the middle), and
   \(t_i\in N^{-1}\ell_i\widehat{\mathcal{O}}\) if \(2i\ge s\) (negative grade).
2. If moreover \((P,N,\pi)\) is a
   [[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree factorisation]]:
   \(\sum_it_i\mathfrak{e}^{i}\in\Lambda^{+}\) iff for all \(i<s\):
   \(t_i\in\ell_i\widehat{\mathcal{O}}\) if \(2i+1<s\) (positive grade), and
   \(t_i\in N^{-1}\ell_i\widehat{\mathcal{O}}\) if \(2i+1\ge s\) (grade \(\le0\)).

So the two criteria differ exactly at the middle index \(2i+1=s\).

## Proof

*The string powers.* By definition \(\mathfrak{e}^{i}=p_i\,z_i\) with
\[
p_i=c^{\,i-\lfloor s/2\rfloor}\ \ (2i<s),\qquad p_i=-N\,c^{\,i-\lfloor(s-1)/2\rfloor}\ \ (2i\ge s),
\]
so the \(z_b\)-coordinate of \(\sum_it_i\mathfrak{e}^{i}\) is \(p_bt_b\).

*Exponent bookkeeping.* For the scale \(u=(a/\bar a)^{k}\), \(k=\lfloor(s+2)/2\rfloor\), the line
idele of [[proofs/grh/upper-seesaw/standard-lattice-membership|the membership criterion]] is
\[
\lambda_b=\ell_b\cdot(a\bar a)^{\,n_b},\qquad n_b=b-\lfloor s/2\rfloor\ (2b<s),\quad n_b=b-\lfloor(s-1)/2\rfloor\ (2b\ge s).
\]
Check: \(\ell_b(a\bar a)^{n}=a^{\,s-b+n}\bar a^{\,-1-b+n}\). If \(s=2j+1\): \(k=j+1\),
\(\lambda_b=u=a^{j+1}\bar a^{-(j+1)}\), and \(n_b=b-j\) in both cases gives
\(a^{j+1}\bar a^{-1-j}\). If \(s=2j\) and \(2b<s\): \(\lambda_b=ua^{-1}=a^{j}\bar a^{-(j+1)}\) and
\(n_b=b-j\) gives \(a^{j}\bar a^{-1-j}\). If \(s=2j\) and \(2b\ge s\):
\(\lambda_b=u\bar a=a^{j+1}\bar a^{-j}\) and \(n_b=b-j+1\) gives \(a^{j+1}\bar a^{-j}\).

*Comparison.* Hence \(\lambda_b^{-1}p_bt_b=\ell_b^{-1}t_b\cdot(c/(a\bar a))^{n_b}\) for \(2b<s\),
and \(-N\,\ell_b^{-1}t_b\cdot(c/(a\bar a))^{n_b}\) for \(2b\ge s\). By hypothesis
\(c/(a\bar a)\) is a unit at every finite place, so: \(\lambda_b^{-1}\) times the
\(z_b\)-coordinate of \(\sum t_i\mathfrak{e}^{i}\) is integral iff \(\ell_b^{-1}t_b\), times \(N\)
when \(2b\ge s\), is integral.

(1) and (2) now follow from parts 1 and 2 of
[[proofs/grh/upper-seesaw/string-lattices-line-by-line|the line-by-line description]]; in (2) the
extra factor \(N\) at the middle index \(2b+1=s\) merges the two cases into \(2b+1\ge s\).
\(\blacksquare\)

## References

1. Lean: `New.Grading.lineIdele_inv_mul_stringSum_mem_iff`, `New.Grading.SpansLattice.stringSum_mem_latticeMinus_iff`, `New.Grading.SpansLattice.stringSum_mem_latticePlus_iff` in `src/New/UpperBound/Seesaw/StandardLines.lean`.
