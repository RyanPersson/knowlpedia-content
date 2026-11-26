+++
id = "proofs/grh/spanning-frames-b/sum-over-shells"
title = "The sum over the shells"
kind = "theorem"
summary = "If the support of a function is covered by shells of heights 2^i, its integral over the group is bounded by the mass bound, a power of the gain, a power of the loss and the shell normalization."
aliases = ["sum over the shells", "dyadic shells"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.Gauge.lintegral_le_of_shells"]
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
proof_status = "full"
+++

**Theorem (the sum over the shells).** In the [[proofs/grh/spanning-frames-b/frames-setting|standing notation]], suppose that \(\mathsf{M}\) is a Haar measure on \(G\). Let \(j\le\varrho\), let \(W\) be a cut Bessel function, let \(p,q\) be heads of length \(j\) for \(\Gamma\), and let \(V\ge1\) bound the mass of floor \(j\). Let \(S_0,S_1,\dots\subseteq G\) be such that \(S_i\) is a [[proofs/grh/spanning-frames-b/shell|shell]] of height \(2^i\) for \((\Gamma,j,p,q,W)\), and let \(f\colon G\to[0,\infty]\) and \(e\in[0,\infty]\) satisfy:

1. \(\{x: f(x)\ne0\}\subseteq\bigcup_iS_i\);
2. \(f(x)\le\mathsf{N}_j(p,q;W;x)\) for all \(x\in G\);
3. if \(e<1\), then \(f(x)^2\le(Ve^{s})^2\,\mathsf{P}^\Gamma_j(p,q;W;x)\) for every position \(x\) of \(F\).

Let \(r\ge0\) be an integer with \(9\cdot10^7n^4+r\le s\). Then
\[
\kappa_j(p,q)\int_Gf\,d\mathsf{M}\;\le\;V\cdot\min(1,e)^{r}\cdot\Lambda^{4\cdot10^8n^4}\cdot\mathsf{c}_F(W).
\]

## Proof

Put \(e'=\min(1,e)\) and \(B=V e'^{\,r}\Lambda^{3\cdot10^8n^4}\mathsf{c}_F(W)\).

*The gain with \(e'\) on each shell.* Let \(x\in S_i\); then \(x\) is a position. If \(e<1\), then \(e'=e\) and hypothesis 3 gives \(f(x)^2\le(Ve'^{s})^2\mathsf{P}^\Gamma_j(p,q;W;x)\). If \(e\ge1\), then \(e'=1\), and by hypothesis 2 and the bound with no gain, [[?lean:New.Floors.Gauge.formMajorant_sq_le_of_floorMassLe|\(\mathsf{N}_j^2\le V^2\mathsf{P}^\Gamma_j\) at positions]],
\[
f(x)^2\le\mathsf{N}_j(p,q;W;x)^2\le V^2\,\mathsf{P}^\Gamma_j(p,q;W;x).
\]

*Each shell.* By [[proofs/grh/spanning-frames-b/shell-inverse-height|the bound with the inverse height]], applied with \(e'\le1\),
\[
\kappa_j(p,q)\int_{S_i}f\,d\mathsf{M}\le2^{-i}B .
\]

*Summation.* As \(f\) vanishes off \(\bigcup_iS_i\), countable subadditivity and the [[real-analysis/geometric-series|geometric series]] \(\sum_{i\ge0}2^{-i}=2\) give
\[
\kappa_j(p,q)\int_Gf\,d\mathsf{M}\le\sum_{i\ge0}\kappa_j(p,q)\int_{S_i}f\,d\mathsf{M}\le2B\le\Lambda^{10^8n^4}B,
\]
because \(2\le\Lambda\le\Lambda^{10^8n^4}\). This is the claim.

## Remarks

The same statement serves a real place and the finite places; only the construction of the shells differs ([[proofs/grh/spanning-frames-b/real-shells|real shells]] and [[proofs/grh/spanning-frames-b/finite-shells|finite shells]]).

## References

1. Lean: `New.Floors.Gauge.lintegral_le_of_shells` in `src/New/Spanning/Frames/Shells.lean`.
