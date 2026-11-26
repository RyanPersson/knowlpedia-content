+++
id = "proofs/grh/spanning-frames-b/remote-shell-gain"
title = "The gain on a remote shell"
kind = "lemma"
summary = "On a shell whose height exceeds a power of the loss, the form majorant gains a power of the inverse height, because every active point has a deep vector."
aliases = ["remote shell"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.Gauge.IsShell.setLIntegral_formMajorant_le"]
lean_files = ["src/New/Spanning/Frames/Shells.lean"]
proof_status = "full"
+++

**Lemma (remote shell).** In the [[proofs/grh/spanning-frames-b/frames-setting|standing notation]], suppose that \(\mathsf{M}\) is a Haar measure on \(G\). Let \(S\) be a [[proofs/grh/spanning-frames-b/shell|shell]] of height \(h\) for \((\Gamma,j,p,q,W)\), with \(j\le\varrho\), \(W\) a cut Bessel function and \(p,q\) heads of length \(j\) for \(\Gamma\). Let \(V\ge1\) bound the mass of floor \(j\). Suppose
\[
h>\Lambda^{2400n^2},\qquad \tau\in[0,\infty],\quad\tau^{800n^2}=h^{-1}.
\]
Then, with \(s\) the volume exponent of \(F\),
\[
\kappa_j(p,q)\int_S\mathsf{N}_j(p,q;W;x)\,d\mathsf{M}(x)\;\le\;V\,\tau^{s}\,\Lambda^{2\cdot10^6n^3}\,h^{10^5n^2}\,\mathsf{c}_F(W).
\]

## Proof

Since \(h>\Lambda^{2400n^2}\ge1\), \(\tau^{800n^2}=h^{-1}<1\), so \(\tau<1\). Moreover
\[
\bigl(\Lambda^{1200n^2}\bigr)^2=\Lambda^{2400n^2}\le h=\tau^{800n^2}h\cdot h=\bigl(\tau^{400n^2}h\bigr)^2,
\]
so \(\Lambda^{1200n^2}\le\tau^{400n^2}h\). By the third property of a shell, every \(x\in S\) has a deep vector of depth \(\tau^{-2}\) after the head. As \(x\) is a position, [[?lean:New.Floors.Gauge.formMajorant_sq_le_of_hasDeepVector|the gain from a deep vector]] (with \(\sigma=\tau^2\)) gives
\[
\mathsf{N}_j(p,q;W;x)^2\le(\tau^2)^{s}V^2\,\mathsf{P}^\Gamma_j(p,q;W;x)=\bigl(V\tau^{s}\bigr)^2\,\mathsf{P}^\Gamma_j(p,q;W;x)\qquad(x\in S).
\]
Thus \(f=\mathsf{N}_j(p,q;W;\cdot)\) has the gain \(e=V\tau^s\) on \(S\), and [[proofs/grh/spanning-frames-b/one-shell-bound|the bound on one shell]] gives the claim.

## References

1. Lean: `New.Floors.Gauge.IsShell.setLIntegral_formMajorant_le` in `src/New/Spanning/Frames/Shells.lean`.
