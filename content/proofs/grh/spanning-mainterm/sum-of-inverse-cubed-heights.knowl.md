+++
id = "proofs/grh/spanning-mainterm/sum-of-inverse-cubed-heights"
title = "Sum of inverse cubes of heights over a totally complex field"
kind = "theorem"
summary = "For any finite subset of a totally complex field with f infinite places, the sum of prod_v max(1,|nu|_v)^(-6) times N(denominator)^(-3) is at most (64*38*e^4)^f."
aliases = ["sum_height_inv_cube_le", "sum over frequencies of inverse cubed heights"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.sum_height_inv_cube_le", "New.sum_weight_filter_denominator_eq_le"]
lean_files = ["src/New/Spanning/MainTerm/Frequencies.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:Totally complex number field|totally complex number field]]
with \(f\) infinite places and chosen embeddings \(\Phi_v\colon E\to\mathbb C\). For every
finite set \(X\subseteq E\),

\[
  \sum_{\nu\in X}\ \Bigl(\prod_{v}\max\bigl(1,\lvert\Phi_v(\nu)\rvert\bigr)^{-6}\Bigr)\cdot
  \bigl(N\mathfrak d(\nu)\bigr)^{-3}\;\le\;\bigl(64\cdot38\cdot e^{4}\bigr)^{f},
\]

where \(\mathfrak d(\nu)\) is the
[[proofs/grh/spanning-mainterm/denominator-ideal|denominator ideal]] of \(\nu\) and \(N\) the
absolute norm.

With \([\nu]_v=\max(1,\lvert\nu\rvert_v)^2\) at an infinite place (the normalised absolute value
of a complex place is the square of the usual one) and the finite places together contributing
\(N\mathfrak d(\nu)\), the summand is the inverse cube of the height \(\prod_v[\nu]_v\) of
\(\nu\).

## Proof

Group the elements of \(X\) by their denominator ideal \(\mathfrak b\), which is nonzero. The
elements \(\nu\in X\) with \(\mathfrak d(\nu)=\mathfrak b\) fall, by the
[[proofs/grh/spanning-mainterm/coset-labels-for-bounded-denominator|coset labels]], into at most
\(N\mathfrak b\) classes within each of which any two elements differ by an algebraic integer;
each class contributes at most \((64\cdot38)^f\) to the sum of the archimedean weights by the
[[proofs/grh/spanning-mainterm/archimedean-weight-sum-over-integer-coset|bound over an integer coset]].
Hence

\[
  \sum_{\nu\in X,\ \mathfrak d(\nu)=\mathfrak b}\prod_v\max(1,\lvert\Phi_v\nu\rvert)^{-6}\le N\mathfrak b\,(64\cdot38)^f ,
\]

and the whole sum is at most
\((64\cdot38)^f\sum_{\mathfrak b}N\mathfrak b\cdot N\mathfrak b^{-3}=(64\cdot38)^f\sum_{\mathfrak b}N\mathfrak b^{-2}\),
the sum over the finitely many denominators that occur. By the
[[proofs/grh/spanning-mainterm/sum-of-inverse-squared-ideal-norms|bound for inverse squares of norms]]
this is at most \((64\cdot38)^f\exp(2[E:\mathbb Q])\). Since \(E\) is totally complex,
\([E:\mathbb Q]=2f\), so \(\exp(2[E:\mathbb Q])=(e^4)^f\). \(\blacksquare\)

## References

1. Lean: `New.sum_height_inv_cube_le`, `New.sum_weight_filter_denominator_eq_le` in
   `src/New/Spanning/MainTerm/Frequencies.lean`.
