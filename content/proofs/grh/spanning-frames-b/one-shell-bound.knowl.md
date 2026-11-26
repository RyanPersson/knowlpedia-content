+++
id = "proofs/grh/spanning-frames-b/one-shell-bound"
title = "The integral over one shell"
kind = "lemma"
summary = "A function with gain e on a shell of height h has integral at most e times a power of the loss, a power of h and the shell normalization."
aliases = ["bound on one shell"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.Gauge.IsShell.setLIntegral_le"]
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
proof_status = "full"
+++

**Lemma (one shell).** In the [[proofs/grh/spanning-frames-b/frames-setting|standing notation]], suppose that the group measure \(\mathsf{M}\) of \(F\) is a [[harmonic-analysis/haar-measure|Haar measure]] on \(G\). Let \(S\) be a [[proofs/grh/spanning-frames-b/shell|shell]] of height \(h\) for \((\Gamma,j,p,q,W)\), with \(j\le\varrho\), \(W\) a cut Bessel function and \(q\) a head of length \(j\) for \(\Gamma\) (nothing is assumed of \(p\)). Let \(f\colon G\to[0,\infty]\) and \(e\in[0,\infty]\) satisfy
\[
f(x)^2\le e^2\,\mathsf{P}^{\Gamma}_j(p,q;W;x)\qquad(x\in S).
\]
Then
\[
\kappa_j(p,q)\int_S f\,d\mathsf{M}\;\le\;e\,\Lambda^{2\cdot10^6n^3}\,h^{10^5n^2}\,\mathsf{c}_F(W),
\]
with \(\mathsf{c}_F(W)\) the [[proofs/grh/spanning-frames-b/shell-normalization|shell normalization]].

## Proof

Let \(\mathcal{G}\) be the set of gauges given by the definition of a shell. For \(\Gamma'\in\mathcal{G}\) the set \(S\cap\mathcal{P}(\Gamma')\) lies in the position ball of \(\Gamma'\) and \(f\) has the gain \(e\) on it, so [[?lean:New.Floors.Gauge.headDensity_mul_lintegral_le_mul_pairingNormSq|the gain on a position ball]] (applied with the pair of gauges \(\Gamma,\Gamma'\)) gives
\[
\kappa_j(p,q)\int_{S\cap\mathcal{P}(\Gamma')}f\,d\mathsf{M}\le e\,\Lambda^{1500000n^3+1}\,\Lambda_{\Gamma'}^{25000n^2}\,\mathsf{c}_F(W)\le B,\qquad B:=e\,\Lambda^{1500000n^3+25000n^2+1}\,h^{50000n^2}\,\mathsf{c}_F(W),
\]
using \(\Lambda_{\Gamma'}\le\Lambda h^2\). The sets \(S\cap\mathcal{P}(\Gamma')\) cover \(S\), so by subadditivity of the integral over a finite union
\[
\kappa_j(p,q)\int_S f\,d\mathsf{M}\le\#\mathcal{G}\cdot B\le 2h^{9n}B\le\Lambda\,h^{9n}B .
\]
Since \(\Lambda\ge1\), \(h\ge1\) and \(n\ge1\), we have \(1500000n^3+25000n^2+2\le2\cdot10^6n^3\) and \(50000n^2+9n\le10^5n^2\), which gives the claim.

## References

1. Lean: `New.Floors.Gauge.IsShell.setLIntegral_le` in `src/New/Spanning/Frames/Shells.lean`.
