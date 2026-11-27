+++
id = "proofs/grh/spanning-unfolding-a/colouring-bound-for-weighted-sums"
title = "Colouring bounds for weighted sums"
kind = "lemma"
summary = "A weighted sum over a set coloured with at most N colours is at most N times the bound for one colour; colours may be residue classes modulo a subgroup of finite index."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_le_of_encard_range_le", "New.Filling.tsum_le_relIndex_pow_mul"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Lemma (colouring).** Let \(A\) be a set, \(w:A\to[0,\infty]\) a weight, \(R\) a relation on \(A\), and \(\varphi:A\to\beta\) a map ("colouring") such that \(\varphi(a)=\varphi(b)\) implies \(R(a,b)\). Let \(N,x\in[0,\infty]\). Suppose the image of \(\varphi\) has at most \(N\) elements, and that every nonempty subset \(B\subseteq A\) whose elements are pairwise \(R\)-related has \(\sum_{a\in B}w(a)\le x\). Then
\[
\sum_{a\in A}w(a)\le N\,x .
\]

**Corollary (residue classes).** Let \(\beta\) be an abelian group with subgroups \(K,K'\) such that \(K\cap K'\) has finite index in \(K'\), let \(\iota\) be a finite set, and let \(f:A\to\beta^{\iota}\) take values with all entries in \(K'\). If every nonempty \(B\subseteq A\) on which \(f\) is constant modulo \(K\) (that is, \(f(a)_i-f(b)_i\in K\) for all \(a,b\in B\), \(i\in\iota\)) has \(\sum_{a\in B}w(a)\le x\), then
\[
\sum_{a\in A}w(a)\le [K':K\cap K']^{\lvert\iota\rvert}\,x .
\]

## Proof

Sums of nonnegative extended reals may be grouped freely. Group \(A\) by the fibres of \(\varphi\): each fibre is nonempty and its elements are pairwise \(R\)-related, so it has weight at most \(x\); there are at most \(N\) fibres. Hence the total is at most \(Nx\).

For the corollary, colour \(a\) by the tuple of classes of the \(f(a)_i\) in \(K'/(K\cap K')\). There are at most \([K':K\cap K']^{\lvert\iota\rvert}\) colours, and two elements of the same colour have \(f(a)_i-f(b)_i\in K\) for all \(i\).

## References

1. Lean: `New.Filling.tsum_le_of_encard_range_le` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
2. Lean: `New.Filling.tsum_le_relIndex_pow_mul` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
