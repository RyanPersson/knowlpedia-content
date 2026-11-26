+++
id = "proofs/grh/spanning-mainterm/archimedean-weight-sum-over-integer-coset"
title = "Sum of archimedean weights over numbers that differ by integers"
kind = "lemma"
summary = "For a finite set of elements of a totally complex field any two of which differ by an algebraic integer, the weights prod_v max(1,|nu|_v)^(-6) sum to at most (64*38)^f."
aliases = ["sum_coset_weight_le", "sum_weight_corner_le", "squareIndex", "squareCorner"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.sum_coset_weight_le", "New.sum_weight_corner_le", "New.weight_le_weight_corner", "New.pairwise_half_le_norm_squareCorner_sub", "New.norm_sub_lt_one_of_squareIndex_eq", "New.squareIndex", "New.squareCorner", "New.squareIndex_squareCorner"]
lean_files = ["src/New/Spanning/MainTerm/Frequencies.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:Totally complex number field|totally complex number field]] with
\(f\) [[?c:Infinite place of a number field|infinite places]], and for each infinite place \(v\)
let \(\Phi_v\colon E\to\mathbb C\) be a chosen complex embedding inducing \(v\). Let
\(X\subseteq E\) be a finite set such that \(\nu-\nu'\) is an algebraic integer for all
\(\nu,\nu'\in X\). Then

\[
  \sum_{\nu\in X}\ \prod_{v}\max\bigl(1,\lvert\Phi_v(\nu)\rvert\bigr)^{-6}\;\le\;(64\cdot38)^{f}.
\]

## Proof

Tile \(\mathbb C\) by the half-open squares
\(Q_m=[\tfrac a2,\tfrac{a+1}2)\times[\tfrac b2,\tfrac{b+1}2)\), \(m=(a,b)\in\mathbb Z^2\), with
lower left corners \(c_m=\tfrac a2+\tfrac b2i\). For \(z\in\mathbb C\) let \(m(z)\) be the index
of the square containing \(z\).

*(i) Two points of one square have distance \(<1\):* their real and imaginary parts differ by
less than \(\tfrac12\), and \(\lvert z\rvert\le\lvert\operatorname{Re}z\rvert+\lvert\operatorname{Im}z\rvert\).

*(ii) \(\max(1,\lvert z\rvert)^{-6}\le64\,\max(1,\lvert c_{m(z)}\rvert)^{-6}\):* by (i),
\(\lvert c_{m(z)}\rvert\le\lvert z\rvert+1\), so \(\max(1,\lvert c_{m(z)}\rvert)\le2\max(1,\lvert z\rvert)\),
and \(2^6=64\).

*(iii) \(\sum_{m\in s}\max(1,\lvert c_m\rvert)^{-6}\le38\) for every finite \(s\subset\mathbb Z^2\):*
distinct corners have distance at least \(\tfrac12\). The
[[?lean:New.tsum_le_of_separated|packing bound for separated points]] states: if points \(f_i\) of
a real normed space of dimension \(d\) have mutual distances \(\ge m>0\), and
\(\lVert f_i\rVert\le Ru_i\) with \(u_i\ge1\), \(R\ge0\), then for \(A>d\) and \(A\le c(A-d)\)
one has \(\sum_iu_i^{-A}\le(1+2R/m)^dc\). With \(d=2\), \(m=\tfrac12\), \(R=1\),
\(u_m=\max(1,\lvert c_m\rvert)\), \(A=6\), \(c=\tfrac32\) (so \(6\le\tfrac32\cdot4\)) the bound is
\(5^2\cdot\tfrac32=37.5\le38\).

*(iv) Injectivity.* Map \(\nu\in X\) to the tuple of indices
\(\operatorname{cell}(\nu)=(m(\Phi_v\nu))_v\). This map is injective on \(X\): if
\(\nu\ne\nu'\) had the same tuple, then by (i) \(0<\lvert\Phi_v(\nu-\nu')\rvert<1\) for all
\(v\), so \(\prod_v\lvert\Phi_v(\nu-\nu')\rvert<1\); but \(\nu-\nu'\) is a nonzero algebraic
integer, and for such a number the product of the \(\lvert\Phi_v(\cdot)\rvert\) over the
infinite places of a totally complex field is at least \(1\), its square being the absolute
value of the norm, a nonzero rational integer
([[?lean:New.one_le_prod_norm_Φ|product of the absolute values of an integer]]).

*(v) Conclusion.* Put \(w(m)=64\max(1,\lvert c_m\rvert)^{-6}\) and let \(S_v\) be the finite set
of indices \(m(\Phi_v\nu)\), \(\nu\in X\). By (ii), injectivity, and nonnegativity of \(w\),

\[
  \sum_{\nu\in X}\prod_v\max(1,\lvert\Phi_v\nu\rvert)^{-6}
  \le\sum_{\nu\in X}\prod_vw(m(\Phi_v\nu))
  \le\sum_{(m_v)\in\prod_vS_v}\prod_vw(m_v)
  =\prod_v\sum_{m\in S_v}w(m)\le(64\cdot38)^f,
\]

using (iii) in the last step. \(\blacksquare\)

## References

1. Lean: `New.sum_coset_weight_le` and the lemmas on squares listed in the front matter, in
   `src/New/Spanning/MainTerm/Frequencies.lean`.
